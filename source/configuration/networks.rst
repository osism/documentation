========
Networks
========

The configuration of dedicated networks is distributed across all
environments and the inventory and is summarized here.

Not necessarily all of these networks have to be separate physical or
VLAN networks. Only the external network defined by the host specific variable
``neutron_external_interface`` should be a dedicated physical or VLAN network.

The following networks are used:

.. contents::
   :depth: 2

Console
=======

The ``console`` network is used to access all nodes via SSH for operations
purposes. It is also used by some infrastructure and helper services like
phpMyAdmin or the web interface for ARA.

This network is defined by ``console_interface`` in the host specific variable
file. The ip address belonging to this interface is defined by
``internal_address`` and for central logging by ``fluentd_host`` variables in ``inventory/host_vars/<hostname>.yml``.

.. code-block:: yaml

   ##########################################################
   # generic

   console_interface: eth0

   internal_address: 10.0.1.2
   fluentd_host: 10.0.1.2

Management (Internal)
=====================

The ``management`` or *internal* network is used for communication between
OpenStack services located on different hosts. It is also used for traffic
without a dedicated network. Ansible playbooks also use this network to access
target hosts. The interface is defined by ``management_interface``.
Additionally the interface need to be defined for *kolla-ansible* by
``network_interface`` and for *Cockpit* by ``cockpit_ssh_interface`` variables in ``inventory/host_vars/<hostname>.yml``.

.. code-block:: yaml

   ##########################################################
   # generic

   management_interface: eth1

   ##########################################################
   # kolla

   network_interface: eth1

   ##########################################################
   # cockpit

   cockpit_ssh_interface: eth1

The DNS name for the internal OpenStack API enpoints is defined by
``kolla_internal_fqdn``. The corresponding ip address for
this DNS name is defined by ``kolla_internal_vip_address`` in ``environments/kolla/configuration.yml``.

.. code-block:: yaml

   ##########################################################
   # haproxy

   kolla_internal_fqdn: internal-api.betacloud.xyz

   ##########################################################
   # hosts

   host_additional_entries:
     internal-api.betacloud.xyz: 10.0.1.10

   ##########################
   # kolla

   kolla_internal_vip_address: 10.0.1.10

Tunnel
======

Traffic between guest virtual machines on different compute nodes or between
layer 3 networking components such as virtual routers are usually routed through
VXLAN or GRE tunnels on the tunnel network in ``inventory/host_vars/<hostname>.yml``.

.. code-block:: yaml

   ##########################################################
   # kolla

   tunnel_interface: eth2

Migration
=========

Live migration of instances is performed over this network, configured in ``inventory/host_vars/<hostname>.yml``.

.. code-block:: yaml

   ##########################################################
   # kolla

   migration_interface: eth2

External API
============

External API endpoints are accessible on the external API network, exposing the
OpenStack API endpoints. This network is reachable by consumers of the cloud
services.

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ##########################################################
   # kolla

   kolla_external_vip_interface: eth3

* ``environments/kolla/configuration.yml``

.. code-block:: yaml

   ##########################################################
   # haproxy

   kolla_external_fqdn: external-api.betacloud.xyz

* ``environments/configuration.yml``

.. code-block:: yaml

   ##########################################################
   # hosts

   host_additional_entries:
     external-api.betacloud.xyz: 10.0.3.10

   ##########################################################
   # kolla

   kolla_external_vip_address: 10.0.3.10

External
========

The external network connects virtual machines to the outside world.

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ##########################################################
   # kolla

   neutron_external_interface: eth4

Loadbalancer
============

This network is used for accessing Loadbalancer as a Service public endpoints.

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ##########################################################
   # kolla

   octavia_network_interface: eth5

Storage Frontend
================

The storage frontend network is the connection between ceph nodes and all other
hosts which need access to storage services.

It is recommended to use an MTU of 9000 in this network.

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ##########################################################
   # kolla

   storage_interface: eth5

   ##########################################################
   # ceph

   monitor_interface: eth5

* ``environments/kolla/configuration.yml``

.. code-block:: yaml

   ##########################################################
   # external ceph

   ceph_public_network: 10.0.5.0/24

* ``environments/ceph/configuration.yml``

.. code-block:: yaml

   ##########################################################
   # network

   public_network: 10.0.5.0/24

Storage Backend
===============

The storage backend network is the internal connection between ceph nodes.

It is recommended to use an MTU of 9000 in this network.

* ``environments/ceph/configuration.yml``

.. code-block:: yaml

   ##########################################################
   # network

   cluster_network: 10.0.6.0/24

Monitoring
==========

The monitoring network normally shares the internal network. A separate network
for monitoring services related traffic can be configured at
``environments/monitorning/configuration.yml``.

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ##########################################################
   # monitoring

   prometheus_scraper_interface: eth1

* ``environments/monitoring/configuration.yml``

.. code-block:: yaml

   ##########################################################
   # exporter

   prometheus_exporter_ceph_public_network: 10.0.5.0/24

.. _host-vars-network-config-examples:

Host Network configuration examples
===================================

* simple example

.. code-block:: yaml

   - device: eno2
     auto: true
     family: inet
     method: static
     address: 192.168.1.10
     netmask: 255.255.255.0
     gateway: 192.168.1.254
     mtu: 1500

   - device: eno3
     auto: true
     family: inet
     method: manual
     mtu: 1500

* simple example with second IP on NIC

.. code-block:: yaml

   - device: eno2
     auto: true
     family: inet
     method: static
     address: 192.168.1.10
     netmask: 255.255.255.0
     gateway: 192.168.1.254
     mtu: 1500

   - device: eno2:1
     auto: true
     family: inet
     method: static
     address: 192.168.11.10
     netmask: 255.255.255.0

* bond example

.. code-block:: yaml

   network_interfaces:
   - device: ens1f0
     auto: true
     family: inet
     method: manual
     bond:
       master: bond0
     mtu: 1500

   - device: ens1f1
     auto: true
     family: inet
     method: manual
     bond:
       master: bond0
     mtu: 1500

   - device: bond0
     auto: true
     family: inet
     method: manual
     address: 192.168.1.10
     netmask: 255.255.255.0
     gateway: 192.168.1.254
     bond:
       mode: 802.3ad
       xmit-hash-policy: layer2+3
       miimon: 100
       slaves: ens1f0 ens1f1
       lacp-rate: 0
     mtu: 1500

* vlan example

.. code-block:: yaml

   - device: bond0
     auto: true
     family: inet
     method: manual
     bond:
       mode: 802.3ad
       xmit-hash-policy: layer2+3
       miimon: 100
       slaves: ens1f0 ens1f1
       lacp-rate: 0
     mtu: 1500

   - device: vlan10
     method: static
     address: 192.168.1.10
     netmask: 255.255.255.0
     vlan:
       raw-device: bond0
     up:
       - route add default gw 192.168.1.254
     mtu: 1500
