====================
Octavia Loadbalancer
====================

Prepare configuration repository
================================

Make sure Octavia is enabled in the configuration repository.

* enable Octavia in ``environments/kolla/configuration.yml``

.. code-block:: yaml

   enable_octavia: "yes"

If you have dedicated network nodes configured, the Octavia health-manager and housekeeping should run on the network nodes to be able to access the openvswitch integration bridge ``br-int``.

* configure Octavia to Control and Network Nodes in ``inventory/hosts`` or ``inventory/20-roles``

.. code-block:: yaml

   [octavia-api:children]
   control

   [octavia-health-manager:children]
   network

   [octavia-housekeeping:children]
   network

   [octavia-worker:children]
   network

Run Octavia deployment
======================

Run Octavia deployment to create the API endpoints and ``octavia`` user. The deployment may not run successfully at this point. It will be run after preparation again to finish the deployment successfully.

.. code-block:: console

   osism-kolla deploy octavia

Populate Octavia project
========================

Add *octavia* entry to `environments/openstack/clouds.yml`. The following openstack cli commands will use the ``octavia`` authentication configuration.

.. code-block:: yaml

   ---
   octavia:
     auth:
       username: octavia
       project_name: octavia
       auth_url: https://api.osism.local:5000/v3
       project_domain_name: default
       user_domain_name: default
     identity_api_version: 3
     verify: false

For authentication with openstack-client set the octavia keystone password in ``environments/openstack/secure.yml``. The password can be found in file ``environments/kolla/secrets.yml`` at ``octavia_keystone_password``.

.. code-block:: yaml

   ---
   clouds:
     octavia:
       auth:
         password: OCTAVIA_KEYSTONE_PASSWORD

Create Octavia project
----------------------

We will create a dedicated project where Octavia management network and amphora
instances are going to be created.

.. code-block:: console

   openstack --os-cloud admin project create --description 'Octavia Loadbalancer Service Project' octavia

Assign admin role to Octavia user in octavia project
----------------------------------------------------

.. code-block:: console

   openstack --os-cloud admin role add --project octavia --user octavia admin

Create security group for amphora instances
-------------------------------------------

.. code-block:: console

   openstack --os-cloud octavia security group create lb-mgmt-sec-grp
   openstack --os-cloud octavia security group rule create --protocol icmp lb-mgmt-sec-grp
   openstack --os-cloud octavia security group rule create --protocol tcp --dst-port 22 lb-mgmt-sec-grp
   openstack --os-cloud octavia security group rule create --protocol tcp --dst-port 9443 lb-mgmt-sec-grp

Create security group for Octavia health manager ports
------------------------------------------------------

.. code-block:: console

   openstack --os-cloud octavia security group create lb-health-mgr-sec-grp
   openstack --os-cloud octavia security group rule create --protocol udp --dst-port 5555 lb-health-mgr-sec-grp

Create keypair for starting amphora instances
---------------------------------------------

.. code-block:: console

   openstack --os-cloud octavia keypair create octavia_ssh_key

Create flavor for amphora instances
-----------------------------------

.. code-block:: console

   openstack --os-cloud octavia flavor create --private --id octavia --disk 2 --ram 512 --vcpus 1 octavia

Create amphora image
--------------------

Create the amphora disk image.

.. code-block:: console

   sudo apt-get install virtualenv qemu-utils git kpartx debootstrap
   git clone https://opendev.org/openstack/octavia.git
   cd octavia
   virtualenv --prompt "dib " .venv
   source .venv/bin/activate
   pip install -r diskimage-create/requirements.txt
   ./diskimage-create/diskimage-create.sh -t raw -o environments/openstack/amphora-x64-haproxy.raw -g stable/train

Create amphora image.

.. code-block:: console

   openstack --os-cloud octavia image create --container-format bare --disk-format raw --private --file /configuration/amphora-x64-haproxy.raw --tag amphora amphora-x64-haproxy

Cleanup.

.. code-block:: console

   cd ..
   rm -rf octavia
   rm -rf environments/openstack/amphora-x64-haproxy*

Create Octavia management network
---------------------------------

.. code-block:: console

   openstack --os-cloud octavia network create lb-mgmt

Create Octavia management subnet
--------------------------------

.. code-block:: console

   openstack --os-cloud octavia subnet create --subnet-range 10.250.0.0/16 --allocation-pool start=10.250.1.10,end=10.250.255.254 --network lb-mgmt lb-mgmt

Create Neutron ports for health manager access
----------------------------------------------

For each network node, create a Neutron port which will be the access port for the health manager, residing on the network node.

.. code-block:: console

   openstack --os-cloud octavia port create \
     --device-owner octavia:health-mgr \
     --security-group lb-health-mgr-sec-grp \
     --fixed-ip subnet=lb-mgmt,ip-address=10.250.0.10 \
     --network lb-mgmt \
     --host network1 \
     lb-mgmt-network1

Create interfaces for health manager on network nodes
-----------------------------------------------------

For each network node, note the port id and the mac address from the ports list.

.. code-block:: console

   openstack --os-cloud octavia port list --device-owner octavia:health-mgr -c Name -c "MAC Address" -c ID

Create virtual ethernet device on each network node, by running the following command on each network node, using the port id and mac address from the ports list.

.. code-block:: console

   docker exec -u root -ti openvswitch_vswitchd ovs-vsctl add-port br-int o-hm0 \
     -- set Interface o-hm0 mtu_request=1500 \
     -- set Interface o-hm0 external-ids:iface-status=active \
     -- set Interface o-hm0 external-ids:skip_cleanup=true \
     -- set Interface o-hm0 type=internal \
     -- set Interface o-hm0 external-ids:attached-mac=PORT_MAC_ADDRESS \
     -- set Interface o-hm0 external-ids:iface-id=PORT_ID

Verify the port status as ``ACTIVE`` from the ports list.

.. code-block:: console

   openstack --os-cloud octavia port list --device-owner octavia:health-mgr -c Name -c "MAC Address" -c ID -c Status

Add health manager interface configuration to config repository
---------------------------------------------------------------

Add the network device configuration for the newly created interfaces on each Network Node in ``inventory/host_vars/<networknodes>.yml``.

.. code-block:: yaml

   - device: o-hm0
     method: static
     address: 10.250.0.10
     netmask: 255.255.0.0
     up:
       - ip link set dev o-hm0 address PORT_MAC_ADDRESS
       - iptables -I INPUT -i o-hm0 -p udp --dport 5555 -j ACCEPT

Run network configuration
-------------------------

Deploy the network configuration to the network nodes.

.. code-block:: console

   osism-generic network -l network

Restart networking on network nodes
-----------------------------------

Restart networking on the network nodes to enable the network device configuration for the health manager interface.


.. code-block:: console

   sudo systemctl restart networking

Configure kolla-ansible
=======================

Note network id of the load balancer management network ``lb-mgmt`` and the id of the security group ``lb-mgmt-sec-grp``.

.. code-block:: console

   openstack --os-cloud octavia network show -f value -c id lb-mgmt
   openstack --os-cloud octavia security group show  -f value -c id lb-mgmt-sec-grp

Add both network id and security group id to the file ``environments/kolla/configuration.yml``.

.. code-block:: yaml

   octavia_service_auth_project: "octavia"
   octavia_loadbalancer_topology: "ACTIVE_STANDBY"
   octavia_network_type: "tenant"
   octavia_auto_configure: false

   octavia_amp_boot_network_list: OCTAVIA_MGMT_NETWORK_ID
   octavia_amp_secgroup_list: OCTAVIA_MGMT_SECURITY_GROUP_ID
   octavia_amp_flavor_id: octavia
   octavia_amp_image_tag: amphora

Configure global parts for ``environments/kolla/files/overlays/octavia.conf``.

.. code-block:: ini

   [controller_worker]
   amp_ssh_key_name = octavia

   [certificates]
   insecure = true

   [glance]
   insecure = true

   [keystone_authtoken]
   insecure = true

   [neutron]
   insecure = true

   [nova]
   insecure = true
   enable_anti_affinity = true
   anti_affinity_policy = anti-affinity
   availability_zone = ZONE_WHERE_AMPHORA_IMAGES_WILL_START

   [service_auth]
   insecure = true
   project_name = octavia

Configure network node specific parts for ``environments/kolla/files/overlays/octavia/<networknodes>/octavia.conf``.

.. code-block:: ini

   [health_manager]
   bind_ip = 10.250.0.10
   controller_ip_port_list = 10.250.0.10:5555

Create x509 certificates
------------------------

Add x509 certificates to configuration repository.
`See Octavia Certificate Configuration Guide <https://docs.openstack.org/octavia/train/admin/guides/certificates.html>`_

The password for the CA private key is located at ``environments/kolla/secrets.yml`` in the configuration repository at variable ``octavia_ca_password``. You need to encrypt the CA private key with this password. The password will be passed to the `octavia.conf` file and Octavia expects the CA private key to be encrypted with this password.

Add the generated files to the following locations in the configuration repository.

- ``environments/kolla/files/overlays/octavia/client.cert-and-key.pem``
- ``environments/kolla/files/overlays/octavia/client_ca.cert.pem``
- ``environments/kolla/files/overlays/octavia/server_ca.cert.pem``
- ``environments/kolla/files/overlays/octavia/server_ca.key.pem``

For releases prior to *Train* refer to the
`Octavia Certificate Configuration Guide <https://docs.openstack.org/octavia/stein/contributor/guides/dev-quick-start.html#create-octavia-keys-and-certificates>`_
and add the certificates to the configuration repository.

* ``environments/kolla/files/overlays/octavia/ca_01.pem``
* ``environments/kolla/files/overlays/octavia/cakey.pem``
* ``environments/kolla/files/overlays/octavia/client.pem``

Run octavia deployment
======================

.. code-block:: console

   osism-kolla deploy octavia

Run haproxy deployment for endpoint creation
============================================

.. code-block:: console

   osism-kolla deploy loadbalancer

Enable loadbalancer menu in Horizon dashboard
=============================================

.. code-block:: console

   osism-kolla deploy horizon
