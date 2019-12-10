.. _scaling_generic:

=======
Generic
=======

The steps described in this section are performed for each node regardless of its type.

Provisioning
============

.. note:: This step is optional and only necessary when using Cobbler.

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

.. code-block:: console

   $ osism-infrastructure cobbler

Then the new node can be started. The provisioning then starts automatically via PXE.

If the PXE boot does not start, this may be because of an error in the MAC address.
You might find some useful logs from dhcpd in the Cobbler container.

.. code-block:: console

   $ docker exec -it cobbler bash
   # service rsyslog start
   # tail -f /var/log/syslog

Inventory
=========

* Add the node to the ``inventory/hosts.installation`` inventory file. As ``ansible_host`` use
 the installation IP address.

 .. code-block:: ini

    [cobbler]
    [...]
    20-12.betacloud.xyz ansible_host=172.16.21.12

 .. note::

    The use of the inventory ``hosts.installation`` is only necessary if the IP address of the
    management interface differs from the IP address to be used later after the initial provisioning.

    This is usually the case when using Cobbler for provisioning.

* Add the node to the ``hosts`` inventory file. As ``ansible_host`` use the management IP address.

  .. code-block:: ini

    [control]
    [...]
    20-12.betacloud.xyz ansible_host=172.17.20.12

* Add the network configuration to the node vars file ``inventory/host_vars/20-12.betacloud.xyz.yml``.

Initialization
==============

.. note::

   The use of the inventory ``hosts.installation`` is only necessary if the IP address of the
   management interface differs from the IP address to be used later after the initial provisioning.

   This is usually the case when using Cobbler for provisioning.

Prepare the node for the bootstrap. This will add a operator user, will prepare the network configuration,
and will reboot the system to change the network configuration.

.. note::

   Of course it is also possible to add more than one new system at a time. Therefore work with pattern at
   ``limit`` accordingly. See also https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html.

* Depending on the environment you may need to install Python first.

  .. note::

     ``apt`` must be usable accordingly. Alternatively install Python already during the provisioning of the node.

  When using Cobbler:

  .. code-block:: console

     $ osism-generic python \
         --limit 20-12.betacloud.xyz \
         -u root \
         --key-file /ansible/secrets/id_rsa.cobbler \
         -i /opt/configuration/inventory/hosts.installation

  When not using Cobbler:

  .. code-block:: console

     $ osism-generic python \
         --limit 20-12.betacloud.xyz \
         -u ubuntu \
         --ask-pass \
         --ask-become-pass

* Creation of the necessary operator user

  When using Cobbler:

  .. code-block:: console

     $ osism-generic operator \
         --limit 20-12.betacloud.xyz \
         -u root \
         --key-file /ansible/secrets/id_rsa.cobbler \
         -i /opt/configuration/inventory/hosts.installation

  When not using Cobbler:

  .. code-block:: console

     $ osism-generic operator \
         --limit 20-12.betacloud.xyz \
         -u ubuntu \
         --ask-pass \
         --ask-become-pass

* Configuration of the network

  When using Cobbler:

  .. code-block:: console

     $ osism-generic network \
         --limit 20-12.betacloud.xyz \
         -i /opt/configuration/inventory/hosts.installation

  When not using Cobbler:

  .. code-block:: console

     $ osism-generic network \
         --limit 20-12.betacloud.xyz

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

  When using Cobbler:

  .. code-block:: console

     $ osism-generic reboot \
         --limit 20-12.betacloud.xyz \
         -i /opt/configuration/inventory/hosts.installation

  When not using Cobbler:

  .. code-block:: console

     $ osism-generic reboot \
         --limit 20-12.betacloud.xyz

* Check if system is reachable

  .. code-block:: console

     $ osism-generic ping --limit 20-12.betacloud.xyz

* Refresh facts.

  .. code-block:: console

     $ osism-generic facts

* Bootstrap the node.

  .. code-block:: console

     $ osism-generic bootstrap --limit 20-12.betacloud.xyz

* Further reboot of the node

  .. code-block:: console

     $ osism-generic reboot --limit 20-12.betacloud.xyz

Update hosts file
=================

After adding a new node, the ``/etc/hosts`` file on all nodes must be updated.

.. code-block:: console

   $ osism-generic hosts

Update cockpit machine files
============================

Only required if cockpit is used.

.. code-block:: console

   $ osism-generic cockpit --limit manager

Deploy common services
======================

* Common services

  .. code-block:: console

     $ osism-kolla deploy common --limit 20-12.betacloud.xyz
