=========
Bootstrap
=========

Add a new system
================

Add the host to the ``cobbler_systems`` parameter in ``infrastructure/configuration.yml``.

.. code-block:: yaml

   cobbler_systems:
   [...]
     - name: 20-12
       params:
         power_address: 172.16.20.12
         power_pass: password
         power_type: ipmilan
         power_user: openstack
         profile: ubuntu-server-xenial-controller
         interfaces:
           ip_address-enp5s0f0: 172.16.21.12
           mac_address-enp5s0f0: aa:bb:cc:dd:ee:ff
           management-enp5s0f0: true
         kernel_options:
           "netcfg/choose_interface": enp5s0f0

Add the host to the ``generic/hosts.installation`` inventory file. As ``ansible_host`` use the installation IP address.

.. code-block:: ini

   [cobbler]
   [...]
   20-12.betacloud.xyz ansible_host=172.16.21.12

Add the host to the ``hosts`` inventory file. As ``ansible_host`` use the management IP address.

.. code-block:: ini

   [control]
   [...]
   20-12.betacloud.xyz ansible_host=172.17.20.12

Add the network configuration to the host vars file ``generic/host_vars/20-12.betacloud.xyz.yml``.

.. todo::

   Add a sample network configuration here.

Prepare the host for the bootstrap. This will add a operator user, will prepare the network configuration, and will reboot the system to change the network configuration.

.. code-block:: shell

   $ osism-generic operator --limit 20-12.betacloud.xyz -u root --key-file /opt/ansible/secrets/id_rsa.cobbler -i hosts.installation
   $ osism-generic network --limit 20-12.betacloud.xyz -u root --key-file /opt/ansible/secrets/id_rsa.cobbler -i hosts.installation
   $ osism-generic reboot --limit 20-12.betacloud.xyz -u root --key-file /opt/ansible/secrets/id_rsa.cobbler -i hosts.installation

Refresh facts.

.. code-block:: shell

   $ osism-generic facts

Bootstrap the host.

.. code-block:: shell

   $ osism-generic bootstrap --limit 20-12.betacloud.xyz
