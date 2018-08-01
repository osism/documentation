========
Overview
========

Files
=====

* ``configuration.yml``

  Default configuration parameters can be overwritten by this file.

* ``images.yml``

  This file can be used to overwrite default images.

* ``secrets.yml``

  Environment specific secrets can be deposited in this file.

* ``ansible.cfg``

  Ansible configuration file.

* ``playbook-*.yml``

  Playbook files for Ansible.

Directories
===========

* ``inventory``

  Ansible inventory directory. All host-specific details are managed here.

* ``environments``

  Directory for managing the individual environments. Each environment has its own subdirectory.

* ``docs``

  Optional directory to manage documents about an environment.

Ansible
=======

Configuration
-------------

* ``environments/ansible.cfg``
* ``environments/*/ansible.cfg``

Inventory
---------

* ``inventory``
* ``inventory/hosts``
* ``inventoyr/host_vars/*.yml``

Network Configuration Overview
==============================

Managment
---------

The managment network is there to access all nodes via SSH as well as some infrastructure and helper
services. It is configured with the ``console_interface`` variable in the host inventory:

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ---
   [...]
   console_interface: eth0

Internal
--------

The internal network is used for internal communication between different hosts. It is also used for
traffic that has no dedicated network.

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ---
   [...]
   managment_interface: eth1
   internal_address: 10.0.1.2

   [...]
   ##########################
   # kolla

   network_interface: eth1

* ``environments/kolla/configuration.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # haproxy

   kolla_internal_fqdn: internal-api.betacloud.xyz

* ``environments/configuration.yml``

.. code-block:: yaml

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
----------

The monitoring network normally falls together with the internal network. Those can be further separated
at ``environments/monitorning/configuration.yml``.

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ---
   [...]
   fluentd_host: 10.0.1.2

   [...]
   ##########################
   # monitoring

   prometheus_scaper_interface: eth1

* ``environments/monitoring/configuration.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # prometheus

   prometheus_scraper_ceph_target_host: 10.0.1.3

Tunnel
------

Traffic between guest virtual machines on different compute nodes or between layer 3 networking
components such as virtual routers are usually tunneled through VXLAN or GRE tunnels over the tunnel
network.

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # kolla

   tunnel_interface: eth2

External API
------------

External API endpoints are in this network.

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # kolla

   kolla_external_vip_interface: eth3

* ``environments/kolla/configuration.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # haproxy

   kolla_external_fqdn: external-api.betacloud.xyz

* ``environments/configuration.yml``

.. code-block:: yaml

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
--------

The external network connects virtual machines to the outside.

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # kolla

   neutron_external_interface: eth4

.. fixme::

   Add provider network from network overview or delete this fixme if not needed.

Storage Frontend
----------------

The storage frontend network is the connection between ceph nodes and all other nodes.

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # kolla

   storage_interface: eth5

   [...]
   ##########################
   # ceph

   monitor_interface: eth5

* ``environments/kolla/configuration.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # external_ceph

   ceph_public_network: 10.0.5.0/24

* ``environments/ceph/configuration.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # network

   public_network: 10.0.5.0/24

* ``environments/monitoring/configuration.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # exporter

   prometheus_exporter_ceph_public_network: 10.0.5.0/24

Storage Backend
----------------

The storage backend network is the internal connection between ceph nodes.

* ``environments/ceph/configuration.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # network

   cluster_network: 10.0.6.0/24
