=======
Neutron
=======

Multiple provider networks
==========================

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   network_interfaces:
   [...]
    - device: eth3
      auto: true
      family: inet
      method: manual
      mtu: 1500

    - device: eth4
      auto: true
      family: inet
      method: manual
      mtu: 1500

* ``environments/kolla/configuration.yml`` or ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   enable_neutron_provider_networks: "yes"

* ``environments/kolla/configuration.yml`` or ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   neutron_bridge_name: br-eth3,br-eth4
   neutron_external_interface: eth3,eth4

VLAN interfaces as flat provider networks
=========================================

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   network_interfaces:
   [...]
    - device: vlan100
      auto: true
      family: inet
      method: manual
      vlan:
        raw-device: bond0
      mtu: 1500

    - device: vlan100
      auto: true
      family: inet
      method: manual
      vlan:
        raw-device: bond0
      mtu: 1500

* ``environments/kolla/configuration.yml`` or ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   enable_neutron_provider_networks: "yes"

* ``environments/kolla/configuration.yml`` or ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   neutron_bridge_name: [...],br-vlan100,br-vlan200
   neutron_external_interface: [...],vlan100,vlan200

.. warning::

   After adding the bridges and before deploying/reconfiguring Neutron, a manual step is needed.

   * https://bugs.launchpad.net/neutron/+bug/1697243
   * https://review.openstack.org/#/c/587244/

   * Check the datapath ids of all bridges on all nodes with provider networks

   .. code-block:: console

      $ docker exec -it openvswitch_vswitchd ovs-vsctl get Bridge br-vlan100 datapath-id                                     
      $ docker exec -it openvswitch_vswitchd ovs-vsctl get Bridge br-vlan200 datapath-id

   * Eleminate duplicate datapath ids

   .. code-block:: console

      $ echo 0000$(uuidgen | awk -F- '{ print $5}')
      0000a046f5209e3f
      $ docker exec -it openvswitch_vswitchd ovs-vsctl set bridge br-vlan200 other-config:datapath-id=0000a046f5209e3f

   * Double check the new datapath ids

   .. code-block:: console

      $ docker exec -it openvswitch_vswitchd ovs-vsctl get Bridge br-vlan200 datapath-id
      "0000a046f5209e3f"
