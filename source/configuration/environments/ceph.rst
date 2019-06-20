.. _configuration-environment-ceph:

====
Ceph
====

Base directory: ``environments/ceph``

.. note ::

   The documentation for ``ceph-ansible`` can be found on http://docs.ceph.com/ceph-ansible/master/.

Generic
=======

* ``environments/ceph/configuration.yml``

  .. code-block:: yaml

     ##########################
     # generic

     containerized_deployment: true
     generate_fsid: false
     fsid: 3e9d257e-aaf7-4471-ad41-aa97a81c736f

     ##########################
     # osd

     osd_objectstore: bluestore
     osd_scenario: collocated

Devices
=======

.. note::

   It is recommended to place the configuration of the devices in the inventory.

.. code-block:: yaml

   ##########################################################
   # ceph

   devices:
     - /dev/sdd
     - /dev/sde

Network
=======

* ``environments/ceph/configuration.yml``

  .. code-block:: yaml

     ##########################
     # network

     public_network: 10.200.250.0/24
     cluster_network: 10.200.251.0/24

* ``environments/kolla/configuration.yml``

  .. code-block:: yaml

     ##########################################################
     # external ceph

     ceph_public_network: 10.200.250.0/24

.. note::

   It is recommended to place the configuration of the network interfaces in the inventory.

.. code-block:: yaml

   ##########################################################
   # ceph

   monitor_interface: eth0

Pools & Keys
============

* ``environments/ceph/configuration.yml``

.. note::

   Remove unneeded pools & keys accordingly.

.. note::

   It is mandatory to choose the value of ``pg_num`` because it cannot be calculated automatically.

   More details in http://docs.ceph.com/docs/mimic/rados/operations/placement-groups/#a-preselection-of-pg-num.

   http://ceph.com/pgcalc can be used to calculate the number of PGs.

.. code-block:: yaml

   ##########################
   # pools & keys

   openstack_config: true

   openstack_glance_pool:
     name: images
     pg_num: 32
     rule_name: ""
     application: "rbd"
   openstack_cinder_pool:
     name: volumes
     pg_num: 32
     rule_name: ""
     application: "rbd"
   openstack_nova_pool:
     name: vms
     pg_num: 32
     rule_name: ""
     application: "rbd"
   openstack_cinder_backup_pool:
     name: backups
     pg_num: 32
     rule_name: ""
     application: "rbd"
   openstack_gnocchi_pool:
     name: metrics
     pg_num: 32
     rule_name: ""
     application: "rbd"


   openstack_pools:
     - "{{ openstack_glance_pool }}"
     - "{{ openstack_cinder_pool }}"
     - "{{ openstack_nova_pool }}"
     - "{{ openstack_cinder_backup_pool }}"
     - "{{ openstack_gnocchi_pool }}"

   openstack_keys:
     - name: client.glance
       caps:
         mon: "allow r"
         osd: "allow class-read object_prefix rbd_children, allow rwx pool={{ openstack_glance_pool.name }}"
       mode: "0600"
     - name: client.cinder
       caps:
         mon: "allow r"
         osd: "allow class-read object_prefix rbd_children, allow rwx pool={{ openstack_cinder_pool.name }}, allow rwx pool={{ openstack_nova_pool.name }}, allow rx pool={{ openstack_glance_pool.name }}"  # yamllint disable-line rule:line-length
       mode: "0600"
     - name: client.cinder-backup
       caps:
         mon: "allow r"
         osd: "allow class-read object_prefix rbd_children, allow rwx pool={{ openstack_cinder_backup_pool.name }}"
       mode: "0600"
     - name: client.gnocchi
       caps:
         mon: "allow r"
         osd: "allow class-read object_prefix rbd_children, allow rwx pool={{ openstack_gnocchi_pool.name }}"
       mode: "0600"
     - name: client.nova
       caps:
         mon: "allow r"
         osd: "allow class-read object_prefix rbd_children, allow rwx pool={{ openstack_glance_pool.name }}, allow rwx pool={{ openstack_nova_pool.name }}, allow rwx pool={{ openstack_cinder_pool.name }}, allow rwx pool={{ openstack_cinder_backup_pool.name }}"  # yamllint disable-line rule:line-length
       mode: "0600"

Custom
======

* https://github.com/ceph/ceph-ansible#configuring-ceph

* ``environments/ceph/configuration.yml``

  .. code-block:: yaml

     ##########################
     # custom

     ceph_conf_overrides:
       mon:
         mon allow pool delete: true

Dashboard
=========

* http://docs.ceph.com/docs/luminous/mgr/dashboard/

* manual activation

.. code-block:: console

   $ ceph mgr module enable dashboard

* ``environments/ceph/configuration.yml``

.. code-block:: yaml

   ##########################
   # custom

   ceph_conf_overrides:
     mon:
       mgr initial modules: dashboard

NUMA
====

.. code-block:: console

   $ lscpu | grep NUMA
   NUMA nodes(s):          2
   NUMA node0 CPU(s)   :   0-13,28-41
   NUMA node1 CPU(s)   :   14-27,42-55

.. code-block:: console

   $ cat /sys/class/net/ens1f0/device/numa_node
   0
   $ cat /sys/class/net/ens2f0/device/numa_node
   0

.. code-block:: yaml
   :caption: inventory/host_vars/STORAGE_NODE.yml

   ceph_osd_docker_cpuset_cpus: "0-13"
   ceph_osd_docker_cpuset_mems: "0"
