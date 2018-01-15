=========
Bootstrap
=========

Prepare the seed system
=======================

.. note:: Run the commands on the seed node.

Prepare the manager system
==========================

.. note:: Run the commands on the seed node.

.. code-block:: shell

   $ cd environments/manager
   $ ANSIBLE_USER=ubuntu ./run.sh operator
   $ ./run.sh network
   $ ./run.sh bootstrap
   $ ./run.sh configuration
   $ ./run.sh manager

.. note::

   To cleanup created directories/files after a run set the environment variable
   ``CLEANUP=true`` or manually delete the ``roles`` and ``.venv`` directories
   as well as the ``id_rsa.operator`` file when you finished the preparations of
   the manager system.

.. note::

   Always carry out an update of the manager in this way.

Prepare infrastructure services
===============================

.. note:: Run the commands on the manager node.

Cobbler
-------

.. code-block:: shell

   $ osism-infrastructure cobbler

Mirror
------

.. code-block:: shell

   $ osism-infrastructure mirror

After the bootstrap of the mirror services they have to be synchronized. Depending on the bandwidth, this process will take several hours.

.. code-block:: shell

   $ osism-mirror files
   $ osism-mirror images
   $ osism-mirror packages

Add a new node
==============

Provisioning of the node with cobbler
-------------------------------------

Add the node definition to the ``cobbler_systems`` list parameter in ``infrastructure/configuration.yml``.

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

You have to update the cobbler configuration.

.. code-block:: shell

   $ osism-infrastructure cobbler

Then the new node can be started. The provisioning then starts automatically via PXE.

Add node to the inventory
=========================

Add the node to the ``inventory/hosts.installation`` inventory file. As ``ansible_host`` use the installation IP address.

.. code-block:: ini

   [cobbler]
   [...]
   20-12.betacloud.xyz ansible_host=172.16.21.12

Add the node to the ``hosts`` inventory file. As ``ansible_host`` use the management IP address.

.. code-block:: ini

   [control]
   [...]
   20-12.betacloud.xyz ansible_host=172.17.20.12

Add the network configuration to the node vars file ``inventory/host_vars/20-12.betacloud.xyz.yml``.

.. todo::

   Add a sample network configuration here.

Preparation of a node for the bootstrap
=======================================

Prepare the node for the bootstrap. This will add a operator user, will prepare the network configuration, and will reboot the system to change the network configuration.

.. note::

   Depending on the environment you may need to install Python first.

   .. code-block:: shell

      $ osism-generic python --limit 20-12.betacloud.xyz -u root --key-file /ansible/secrets/id_rsa.cobbler -i /opt/configuration/inventory/hosts.installation


   ``apt`` must be usable accordingly. Alternatively install Python already during the provisioning of the node.

.. code-block:: shell

   $ osism-generic operator --limit 20-12.betacloud.xyz -u root --key-file /ansible/secrets/id_rsa.cobbler -i /opt/configuration/inventory/hosts.installation
   $ osism-generic network --limit 20-12.betacloud.xyz -i /opt/configuration/inventory/hosts.installation
   $ osism-generic reboot --limit 20-12.betacloud.xyz -i /opt/configuration/inventory/hosts.installation

Bootstrap of a node
===================

Refresh facts.

.. code-block:: shell

   $ osism-generic facts

Bootstrap the node.

.. code-block:: shell

   $ osism-generic bootstrap --limit 20-12.betacloud.xyz

Update hosts file
=================

After adding a new node, the ``/etc/hosts`` file on all nodes must be updated.

.. code-block:: shell

   $ osism-generic hosts
