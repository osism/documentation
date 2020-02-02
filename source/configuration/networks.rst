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
   :local:

Management / Console
====================

The ``management`` or ``console`` network is used to access all nodes via SSH.
It is also used by some infrastructure and helper services like phpMyAdmin or
the web interface for ARA.

This network is defined by ``console_interface`` in the host specific variable
file:

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ##########################################################
   # generic

   console_interface: eth0

Internal
========

The internal network is used for communication between services located on
different hosts. It is also used for traffic that has no dedicated network.
Ansible playbooks also use this network to access target hosts.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ##########################################################
   # generic

   management_interface: eth1
   internal_address: 10.0.1.2
   fluentd_host: 10.0.1.2

   ##########################################################
   # kolla

   network_interface: eth1

   ##########################################################
   # cockpit

   cockpit_ssh_interface: eth1

.. code-block:: yaml
   :caption: environments/kolla/configuration.yml

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
VXLAN or GRE tunnels on the tunnel network.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ##########################################################
   # kolla

   tunnel_interface: eth2

Migration
=========

Live migration of instances is performed over this network.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ##########################################################
   # kolla

   migration_interface: eth2

External API
============

External API endpoints are accessible on the external API network. This network
is reachable by consumers of the cloud services.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ##########################################################
   # kolla

   kolla_external_vip_interface: eth3

.. code-block:: yaml
   :caption: environments/kolla/configuration.yml

   ##########################################################
   # haproxy

   kolla_external_fqdn: external-api.betacloud.xyz

.. code-block:: yaml
   :caption: environments/configuration.yml

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

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ##########################################################
   # kolla

   neutron_external_interface: eth4

Loadbalancer
============

This network is used for accessing Loadbalancer as a Service public endpoints.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ##########################################################
   # kolla

   octavia_network_interface: eth5

Storage Frontend
================

The storage frontend network is the connection between ceph nodes and all other
hosts which need access to storage services.

It is recommended to use an MTU of 9000 in this network.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ##########################################################
   # kolla

   storage_interface: eth5

   ##########################################################
   # ceph

   monitor_interface: eth5

.. code-block:: yaml
   :caption: environments/kolla/configuration.yml

   ##########################################################
   # external ceph

   ceph_public_network: 10.0.5.0/24

.. code-block:: yaml
   :caption: environments/ceph/configuration.yml

   ##########################################################
   # network

   public_network: 10.0.5.0/24

Storage Backend
===============

The storage backend network is the internal connection between ceph nodes.

It is recommended to use an MTU of 9000 in this network.

.. code-block:: yaml
   :caption: environments/ceph/configuration.yml

   ##########################################################
   # network

   cluster_network: 10.0.6.0/24

Monitoring
==========

The monitoring network normally shares the internal network. A separate network
for monitoring services related traffic can be configured at
``environments/monitorning/configuration.yml``.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ##########################################################
   # monitoring

   prometheus_scraper_interface: eth1

.. code-block:: yaml
   :caption: environments/monitoring/configuration.yml

   ##########################################################
   # exporter

   prometheus_exporter_ceph_public_network: 10.0.5.0/24
