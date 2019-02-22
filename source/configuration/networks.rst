========
Networks
========

The configuration of the individual networks is distributed across all environments and the inventory
and is summarized here.

The following networks are used:

* Management / Console
* Internal
* Monitoring
* Tunnel
* Migration
* External
* External API
* Storage Frontend
* Storage Backend

Managment / Console
===================

The managment or console network is there to access all nodes via SSH as well as some infrastructure and helper
services. It is configured with the ``console_interface`` variable in the host inventory:

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ---
   [...]
   console_interface: eth0

Internal
========

The internal network is used for internal communication between different hosts. It is also used for
traffic that has no dedicated network.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ---
   [...]
   managment_interface: eth1
   internal_address: 10.0.1.2

   [...]
   ##########################
   # kolla

   network_interface: eth1

.. code-block:: yaml
   :caption: environments/kolla/configuration.yml

   ---
   [...]
   ##########################
   # haproxy

   kolla_internal_fqdn: internal-api.betacloud.xyz

.. code-block:: yaml
   :caption: environments/configuration.yml

   ---
   [...]
   ##########################
   # hosts

   host_additional_entries:
     internal-api.betacloud.xyz: 10.0.1.10

   [...]
   ##########################
   # kolla

   kolla_internal_vip_address: 10.0.1.10

Monitoring
==========

The monitoring network normally falls together with the internal network. Those can be further separated
at ``environments/monitorning/configuration.yml``.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ---
   [...]
   fluentd_host: 10.0.1.2

   [...]
   ##########################
   # monitoring

   prometheus_scaper_interface: eth1

Tunnel
======

Traffic between guest virtual machines on different compute nodes or between layer 3 networking
components such as virtual routers are usually tunneled through VXLAN or GRE tunnels over the tunnel
network.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ---
   [...]
   ##########################
   # kolla

   tunnel_interface: eth2

External API
============

External API endpoints are in this network.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ---
   [...]
   ##########################
   # kolla

   kolla_external_vip_interface: eth3

.. code-block:: yaml
   :caption: environments/kolla/configuration.yml

   ---
   [...]
   ##########################
   # haproxy

   kolla_external_fqdn: external-api.betacloud.xyz

.. code-block:: yaml
   :caption: environments/configuration.yml

   ---
   [...]
   ##########################
   # hosts

   host_additional_entries:
     external-api.betacloud.xyz: 10.0.3.10

   [...]
   ##########################
   # kolla

   kolla_external_vip_address: 10.0.3.10

External
========

The external network connects virtual machines to the outside.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ---
   [...]
   ##########################
   # kolla

   neutron_external_interface: eth4

Storage Frontend
================

The storage frontend network is the connection between ceph nodes and all other nodes.

.. code-block:: yaml
   :caption: inventory/host_vars/<hostname>.yml

   ---
   [...]
   ##########################
   # kolla

   storage_interface: eth5

   [...]
   ##########################
   # ceph

   monitor_interface: eth5

.. code-block:: yaml
   :caption: environments/kolla/configuration.yml

   ---
   [...]
   ##########################
   # external_ceph

   ceph_public_network: 10.0.5.0/24

.. code-block:: yaml
   :caption: environments/ceph/configuration.yml

   ---
   [...]
   ##########################
   # network

   public_network: 10.0.5.0/24

.. code-block:: yaml
   :caption: environments/monitoring/configuration.yml

   ---
   [...]
   ##########################
   # exporter

   prometheus_exporter_ceph_public_network: 10.0.5.0/24

Storage Backend
===============

The storage backend network is the internal connection between ceph nodes.

.. code-block:: yaml
   :caption: environments/ceph/configuration.yml

   ---
   [...]
   ##########################
   # network

   cluster_network: 10.0.6.0/24
