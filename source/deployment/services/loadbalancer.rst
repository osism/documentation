====================
Octavia Loadbalancer
====================

Populate Octavia project
========================

For authentication with openstack-client set the octavia keystone password. The
password can be found in file
``/opt/configuration/environments/kolla/secrets.yml`` at
``octavia_keystone_password``.

.. code-block:: yaml
   :caption: /opt/configuration/environments/openstack/secure.yml

   ---
   clouds:
     octavia:
       auth:
         password: OCTAVIA_PASS

Create Octavia project
----------------------

.. code-block:: console

   openstack --os-cloud admin project create octavia

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

   openstack --os-cloud octavia keypair create octavia

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
   ./diskimage-create/diskimage-create.sh -t raw -o /opt/configuration/environments/openstack/amphora-x64-haproxy -g stable/train

.. note::

   When building image from branch ``stable/rocky`` and before, the environment
   variable ``DIB_REPOLOCATION_upper_constraints`` needs to be set to ``stein``
   or higher release because of a bug in the python package ``MarkupSafe==1.0``.

.. code-block:: shell

   export DIB_REPOLOCATION_upper_constraints="https://opendev.org/openstack/requirements/raw/branch/stable/stein/upper-constraints.txt"

Create amphora image.

.. code-block:: console

   openstack --os-cloud octavia image create --container-format bare --disk-format raw --private --file /configuration/amphora-x64-haproxy.raw --tag amphora amphora

Cleanup.

.. code-block:: console

   cd ..
   rm -rf octavia
   rm -rf /opt/configuration/environments/openstack/amphora-x64-haproxy*

Create Octavia management network
---------------------------------

.. code-block:: console

   openstack --os-cloud octavia network create lb-mgmt

Create Octavia management subnet
--------------------------------

For each load balancer there will be at least one amphora instance in the
Octavia management network created. If the load balancer is configured as
``ACTIVE_STANDBY`` there will be two amphora instances for each load balancer.
Therefore the network should allow enough host addresses. If you expect more
than 100 load balancers to be configured on your cloud, use a ``/16`` network.

.. code-block:: console

   openstack --os-cloud octavia subnet create --subnet-range 10.1.250.1/24 --allocation-pool start=10.1.250.20,end=10.1.250.254 --network lb-mgmt lb-mgmt

Create Neutron ports for health manager access
----------------------------------------------

For each control node, create a Neutron port which will be the access port
for the health manager, residing on the control node.

.. code-block:: console

   openstack --os-cloud octavia port create \
     --device-owner octavia:health-mgr \
     --security-group lb-health-mgr-sec-grp \
     --fixed-ip subnet=lb-mgmt,ip-address=10.1.250.10 \
     --network lb-mgmt \
     --host control1 \
     lb-mgmt-control1

Create interfaces for health manager on control nodes
-----------------------------------------------------

For each control node, note the port id and the mac address from the ports list.

.. code-block:: console

   openstack --os-cloud octavia port list --device-owner octavia:health-mgr -c Name -c "MAC Address" -c ID

Create virtual ethernet device on each control node, by running the following
command on each control node, using the port id and mac address from the ports
list.

.. code-block:: console

   docker exec -u root -ti openvswitch_vswitchd ovs-vsctl add-port br-int ohm0 \
     -- set Interface ohm0 external-ids:iface-status=active \
     -- set Interface ohm0 external-ids:skip_cleanup=true \
     -- set Interface ohm0 type=internal \
     -- set Interface ohm0 external-ids:attached-mac=PORT_MAC_ADDRESS \
     -- set Interface ohm0 external-ids:iface-id=PORT_ID

Verify the port status as ``ACTIVE`` from the ports list.

.. code-block:: console

   openstack --os-cloud octavia port list --device-owner octavia:health-mgr -c Name -c "MAC Address" -c ID -c Status

Add health manager interface configuration to config repository
---------------------------------------------------------------

Add the network device configuration for the newly created interfaces on each
control node in configuration repository.

.. code-block:: yaml
   :caption: /opt/configuration/inventory/host_vars/control1.yml

   - device: ohm0
     method: static
     address: 10.1.250.10
     netmask: 255.255.255.0
     up:
       - ip link set dev ohm0 address PORT_MAC_ADDRESS
       - iptables -I INPUT -i ohm0 -p udp --dport 5555 -j ACCEPT

Run network configuration
-------------------------

Deploy the network configuration to the control nodes.

.. code-block:: console

   osism-generic network -l 'control'

Restart networking on control nodes
-----------------------------------

Restart networking on the control nodes to enable the network device
configuration for the health manager interface.


.. code-block:: console

   sudo systemctl restart networking

Configure ansible-kolla
=======================

Note network id of the load balancer management network ``lb-mgmt``
and the id of the security group ``lb-mgmt-sec-grp``.

.. code-block:: console

   openstack --os-cloud octavia network show -f value -c id lb-mgmt
   openstack --os-cloud octavia security group show  -f value -c id lb-mgmt-sec-grp

Add both network id and security group id to the configuration repository.

.. code-block:: yaml
   :caption: /opt/configuration/environments/kolla/configuration.yml
   
   octavia_amp_boot_network_list: OCTAVIA_MGMT_NETWORK_ID
   octavia_amp_secgroup_list: OCTAVIA_MGMT_SECURITY_GROUP_ID
   octavia_amp_flavor_id: octavia

Configure global parts for *octavia.conf*.

.. code-block:: ini
   :caption: /opt/configuration/environments/kolla/files/overlays/octavia.conf

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
   
   [service_auth]
   project_name = octavia

Configure control node specific parts for *octavia.conf* for each control node.

.. code-block:: ini
   :caption: /opt/configuration/environments/kolla/files/overlays/octavia/control1/octavia.conf

   [health_manager]
   bind_ip = 10.1.250.10
   controller_ip_port_list = 10.1.250.10:5555

Add x509 certificates to configuration repository.

- The CA certificate ``/opt/configuration/environments/kolla/files/overlays/octavia/ca_01.pem``
- The CA private key ``/opt/configuration/environments/kolla/files/overlays/octavia/cakey.pem``
- The HAProxy client certificate ``/opt/configuration/environments/kolla/files/overlays/octavia/client.pem``

Run octavia deployment
======================

.. code-block:: console

   osism-kolla deploy octavia
