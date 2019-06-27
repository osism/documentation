=========
Bootstrap
=========

.. contents::
   :local:

.. _initialize-nodes:

Initialization
==============

.. note:: Execute the following commands on the manager node.

The following steps are performed to initialize all nodes. :ref:`add-node` describes how to add a new node to an existing environment.

* Creation of the necessary operator user

  .. code-block:: console

     $ osism-generic operator -l 'all:!manager' -u ubuntu

  * The operator key has to be added in advance on all nodes to ``authorized_keys`` of the user
    specified with ``-u``.
  * Alternatively, you can work with the parameters ``--ask-pass`` and ``--ask-become-pass``.
  * If the error ``/bin/sh: 1: /usr/bin/python: not found`` occurs, Python must first be installed on
    the manager node with ``osism-generic python -l 'all:!manager' -u ubuntu``.

  .. warning::

     If the operator user was already created when the operating system was provisioned, this
     role must still be executed. ``ANSIBLE_USER`` is then adjusted accordingly.

     The UID and GID must also be checked. If it is not ``45000``, it must be adapted accordingly.

     .. code-block:: console

        # usermod -u 45000 dragon
        # groupmod -g 45000 dragon

        # chgrp dragon /home/dragon/
        # chown dragon /home/dragon/

        # find /home/dragon -group 1000 -exec chgrp -h dragon {} \;
        # find /home/dragon -user 1000 -exec chown -h dragon {} \;

* Configuration of the network

  .. code-block:: console

     $ osism-generic network -l 'all:!manager'

  * The network configuration already present on a system should be saved before this step.
  * We are currently still using ``/etc/network/interfaces``. Therefore rename all files below ``/etc/netplan`` to ``X.unused``.

    The default file ``01-netcfg.yaml`` with the following content can remain as it is.

    .. code-block:: yaml

      # This file describes the network interfaces available on your system
      # For more information, see netplan(5).
      network:
        version: 2
        renderer: networkd

* Reboot of the nodes

  .. code-block:: console

     $ osism-generic reboot -l 'all:!manager'

* Check if all systems are reachable

  .. code-block:: console

     $ osism-generic ping

* Refresh facts

  .. code-block:: console

     $ osism-generic facts

* Bootstrap of the nodes

  .. code-block:: console

     $ osism-generic bootstrap

  .. note::

     The re-execution of the bootstrap on the manager is intended.

* Further reboot of the nodes

  .. code-block:: console

     $ osism-generic reboot -l 'all:!manager'
     $ osism-generic reboot -l manager

.. _add-node:

Add node
========

.. note:: Execute the following commands on the manager node.

The following steps are performed to add a new node to the environment. :ref:`initialize-nodes` describes how to initialize all nodes in a new environment.

Provisioning
------------

This step is optional and only necessary when using Cobbler.

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
---------

* Add the node to the ``inventory/hosts.installation`` inventory file. As ``ansible_host`` use
  the installation IP address.

  .. code-block:: ini

     [cobbler]
     [...]
     20-12.betacloud.xyz ansible_host=172.16.21.12

* Add the node to the ``hosts`` inventory file. As ``ansible_host`` use the management IP address.

  .. code-block:: ini

     [control]
     [...]
     20-12.betacloud.xyz ansible_host=172.17.20.12

* Add the network configuration to the node vars file ``inventory/host_vars/20-12.betacloud.xyz.yml``.

  .. code-block:: yaml

     ##########################################################
     # network-interfaces

     network_allow_service_restart: no
     network_restart_method: nothing

     network_interfaces:
       - device: enp19s0f0
	 auto: true
	 family: inet
	 method: manual
	 bond:
	   master: bond0

       - device: enp19s0f1
	 auto: true
	 family: inet
	 method: manual
	 bond:
	   master: bond0

       - device: eno1
	 auto: true
	 family: inet
	 method: manual
	 bond:
	   master: bond1

       - device: eno2
	 auto: true
	 family: inet
	 method: manual
	 bond:
	   master: bond1

       - device: bond0
	 auto: true
	 family: inet
	 method: manual
	 bond:
	   mode: 802.3ad
	   lacp-rate: fast
	   miimon: 100
	   slaves: enp19s0f0 enp19s0f1

       - device: bond1
	 auto: true
	 family: inet
	 method: manual
	 mtu: 9000
	 bond:
	   mode: 802.3ad
	   lacp-rate: fast
	   miimon: 100
	   slaves: eno1 eno2

       - device: vlan101
	 method: static
	 address: 172.17.52.10
	 gateway: 172.17.40.10
	 netmask: 255.255.0.0
	 vlan:
	   raw-device: bond0
	 up:
	 - route add default gw 172.17.40.10

       - device: vlan299
	 method: static
	 address: 10.49.52.10
	 netmask: 255.255.0.0
	 vlan:
	   raw-device: bond0

       - device: vlan297
	 method: static
	 address: 10.47.52.10
	 netmask: 255.255.0.0
	 vlan:
	   raw-device: bond1

       - device: vlan298
	 method: static
	 address: 10.48.52.10
	 netmask: 255.255.0.0
	 vlan:
	   raw-device: bond1

       - device: vlan398
	 method: static
	 address: 10.30.52.10
	 netmask: 255.255.0.0
	 vlan:
	   raw-device: bond1

       - device: vlan399
	 method: static
	 address: 10.31.52.10
	 netmask: 255.255.0.0
	 vlan:
	   raw-device: bond1

Initialization
--------------

Prepare the node for the bootstrap. This will add a operator user, will prepare the network configuration,
and will reboot the system to change the network configuration.

.. note::

   Of course it is also possible to add more than one new system at a time. Therefore work with pattern at
   ``limit`` accordingly. See also https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html.

Depending on the environment you may need to install Python first.

.. code-block:: console

   $ osism-generic python \
       --limit 20-12.betacloud.xyz \
       -u root \
       --key-file /ansible/secrets/id_rsa.cobbler \
       -i /opt/configuration/inventory/hosts.installation

``apt`` must be usable accordingly. Alternatively install Python already during the provisioning of the node.

It is recommended to install Python on the systems during the provisioning process.

* Creation of the necessary operator user

  .. code-block:: console

     $ osism-generic operator \
         --limit 20-12.betacloud.xyz \
         -u root \
         --key-file /ansible/secrets/id_rsa.cobbler \
         -i /opt/configuration/inventory/hosts.installation

* Configuration of the network

  .. code-block:: console

     $ osism-generic network \
         --limit 20-12.betacloud.xyz \
         -i /opt/configuration/inventory/hosts.installation

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
         --limit 20-12.betacloud.xyz \
         -i /opt/configuration/inventory/hosts.installation

The use of the ``hosts.installation`` file is optional and is not available depending on the environment.

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
-----------------

After adding a new node, the ``/etc/hosts`` file on all nodes must be updated.

.. code-block:: console

   $ osism-generic hosts

Deploy services
---------------

* Common services

  .. code-block:: console

     $ osism-kolla deploy common --limit 20-12.betacloud.xyz

* Storage services (if it is a storage node)

  .. code-block:: console

     $ osism-ceph osds --limit 20-12.betacloud.xyz

* Compute services (If it is a compute node)

  .. code-block:: console

     $ osism-kolla deploy nova --limit 20-12.betacloud.xyz
     $ osism-kolla deploy openvswitch --limit 20-12.betacloud.xyz
     $ osism-kolla deploy neutron --limit 20-12.betacloud.xyz

* Monitoring services (if monitoring is used)

  .. code-block:: console

     $ osism-monitoring prometheus-exporter --limit 20-12.betacloud.xyz
     $ osism-monitoring prometheus
