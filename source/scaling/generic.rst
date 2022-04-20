.. _scaling_generic:

=======
Generic
=======

The steps described in this section are performed for each node regardless of its type.

Provisioning
============

The system is provisioned with the tool of choice.

Inventory
=========

* Add the node to the ``hosts`` inventory file. As ``ansible_host`` use the management IP address.

  .. code-block:: ini

    [control]
    [...]
    testbed-node-2.osism.local ansible_host=192.168.40.12

* Add the network configuration to the node vars file ``inventory/host_vars/testbed-node-2.osism.local.yml``.

Initialization
==============

Prepare the node for the bootstrap. This will add a operator user, will prepare the network configuration,
and will reboot the system to change the network configuration.

.. note::

   Of course it is also possible to add more than one new system at a time. Therefore work with pattern at
   ``limit`` accordingly. See also

   https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html.

* Depending on the environment you may need to install Python first.

  .. note::

     ``apt`` must be usable accordingly. Alternatively install Python already during the provisioning of the node.

  .. code-block:: console

     $ osism-generic python3 \
         --limit testbed-node-2.osism.local \
         -u ubuntu \
         --ask-pass \
         --ask-become-pass

* Creation of the necessary operator user

  .. code-block:: console

     $ osism-generic operator \
         --limit testbed-node-2.osism.local \
         -u ubuntu \
         --ask-pass \
         --ask-become-pass

* Configuration of the network

  .. code-block:: console

     $ osism-generic network \
         --limit testbed-node-2.osism.local

  * The network configuration already present on a system should be saved before this step.
  * We are currently still using ``/etc/network/interfaces``. Therefore rename all files below ``/etc/netplan`` to ``X.unused``.

    The default file ``01-netcfg.yaml`` with the following content can remain as it is.

    .. code-block:: yaml

      # This file describes the network interfaces available on your system
      # For more information, see netplan(5).
      network:
        version: 2
        renderer: networkd

* A reboot is performed to activate and test the network configuration.
  The reboot must be performed before the bootstrap is performed.

  .. code-block:: console

     $ osism-generic reboot \
         --limit testbed-node-2.osism.local

* Check if system is reachable

  .. code-block:: console

     $ osism-generic ping --limit testbed-node-2.osism.local

* Refresh facts.

  .. code-block:: console

     $ osism-generic facts

* Bootstrap the node.

  .. code-block:: console

     $ osism-generic bootstrap --limit testbed-node-2.osism.local

* Further reboot of the node

  .. code-block:: console

     $ osism-generic reboot --limit testbed-node-2.osism.local

Update hosts file
=================

After adding a new node, the ``/etc/hosts`` file on all nodes must be updated.

.. code-block:: console

   $ osism-generic hosts

Deploy common services
======================

* Common services

  .. code-block:: console

     $ osism-kolla deploy common --limit testbed-node-2.osism.local
