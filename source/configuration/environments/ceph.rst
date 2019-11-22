.. _configuration-environment-ceph:

====
Ceph
====

Base directory: ``environments/ceph``

.. note ::

   The documentation for ``ceph-ansible`` can be found at http://docs.ceph.com/ceph-ansible/master/.

Generic
=======

* ``environments/ceph/configuration.yml``

  .. code-block:: yaml

     ##########################
     # generic

     containerized_deployment: true

     ceph_origin: repository
     ceph_repository: community
     ceph_stable_release: luminous

     osd_objectstore: bluestore
     osd_scenario: lvm

     generate_fsid: false
     fsid: 3e9d257e-aaf7-4471-ad41-aa97a81c736f

* ``environments/configuration.yml``

  .. code-block:: yaml

     ##########################
     # ceph

     ceph_share_directory: /share
     ceph_cluster_fsid: 3e9d257e-aaf7-4471-ad41-aa97a81c736f

Devices
=======

.. note::

   It is recommended to place the configuration of the devices in the inventory.

Unlike other ``by-id`` links, WWNs (`World Wide Name <https://en.wikipedia.org/wiki/World_Wide_Name>`_) are
fully persistent and will not change depending on the used subsystem. For more details see
https://wiki.archlinux.org/index.php/Persistent_block_device_naming.

.. code-block:: yaml
   :caption: inventory/host_vars/STORAGE_NODE.yml

   ##########################################################
   # ceph

   devices:
     - /dev/disk/by-id/wwn-0x50014ee206985361
     - /dev/disk/by-id/wwn-0x50014ee2b1576368

When using NVMe devices, the EUI-64 (`64-Bit Extended Unique Identifier <https://tools.ietf.org/html/rfc4291#section-2.5.1>`_)
is used.

.. code-block:: yaml
   :caption: inventory/host_vars/STORAGE_NODE.yml

   ##########################################################
   # ceph

   devices:
     - /dev/disk/by-id/nvme-eui.343338304d1002630025384600000001
     - /dev/disk/by-id/nvme-eui.343338304d1002450025384600000001

Network
=======

Ceph uses a ``public_network`` which needs to be reachable by Ceph clients and
a separate network, which is used by OSDs. The network used by OSDs is called
``cluster_network``. When omitting the ``cluster_network`` variable, the
``public_network`` is used by OSDs as well.

* ``environments/ceph/configuration.yml``

  .. code-block:: yaml

     ##########################
     # network

     public_network: 10.200.250.0/24
     cluster_network: 10.200.249.0/24

* ``environments/kolla/configuration.yml``

  .. code-block:: yaml

     ##########################################################
     # external ceph

     ceph_public_network: 10.200.250.0/24

.. note::

   It is recommended to place the configuration of the network interfaces in the inventory.

.. code-block:: yaml
   :caption: inventory/host_vars/STORAGE_NODE.yml

   ##########################################################
   # ceph

   monitor_interface: eth0
   # monitor_address:

Pools & Keys
============

* ``environments/ceph/configuration.yml``

.. note::

   Add or remove unneeded pools & keys accordingly.

.. note::

   It is mandatory to choose the value of ``pg_num`` because it cannot be calculated automatically.

   More details in http://docs.ceph.com/docs/mimic/rados/operations/placement-groups/#a-preselection-of-pg-num.

   http://ceph.com/pgcalc can be used to calculate the number of PGs.

.. code-block:: yaml

   ##########################
   # pools & keys

   # NOTE: After the initial deployment of the Ceph Clusters, the following parameter can be
   #       set to false. It must only be set to true again when new pools or keys are added.
   openstack_config: true

   # Define pools for Openstack services
   openstack_cinder_backup_pool:
     name: backups
     pg_num: 32
     rule_name: ""
     application: "rbd"
   openstack_cinder_pool:
     name: volumes
     pg_num: 32
     rule_name: ""
     application: "rbd"
   openstack_glance_pool:
     name: images
     pg_num: 32
     rule_name: ""
     application: "rbd"
   openstack_gnocchi_pool:
     name: metrics
     pg_num: 32
     rule_name: ""
     application: "rbd"
   openstack_nova_pool:
     name: vms
     pg_num: 32
     rule_name: ""
     application: "rbd"

   openstack_pools:
     - "{{ openstack_cinder_backup_pool }}"
     - "{{ openstack_cinder_pool }}"
     - "{{ openstack_glance_pool }}"
     - "{{ openstack_gnocchi_pool }}"
     - "{{ openstack_nova_pool }}"

   # Define keys for Ceph clients
   openstack_keys:
     - name: client.glance
       caps:
         mon: "allow r"
         osd: >
           allow class-read object_prefix rbd_children,
           allow rwx pool={{ openstack_glance_pool.name }}
       mode: "0600"
     - name: client.cinder
       caps:
         mon: "allow r"
         osd: >
           allow class-read object_prefix rbd_children,
           allow rwx pool={{ openstack_cinder_pool.name }},
           allow rwx pool={{ openstack_nova_pool.name }},
           allow rx pool={{ openstack_glance_pool.name }}
       mode: "0600"
     - name: client.cinder-backup
       caps:
         mon: "allow r"
         osd: >
           allow class-read object_prefix rbd_children,
           allow rwx pool={{ openstack_cinder_backup_pool.name }}
       mode: "0600"
     - name: client.gnocchi
       caps:
         mon: "allow r"
         osd: >
           allow class-read object_prefix rbd_children,
           allow rwx pool={{ openstack_gnocchi_pool.name }}
       mode: "0600"
     - name: client.nova
       caps:
         mon: "allow r"
         osd: >
           allow class-read object_prefix rbd_children,
           allow rwx pool={{ openstack_glance_pool.name }},
           allow rwx pool={{ openstack_nova_pool.name }},
           allow rwx pool={{ openstack_cinder_pool.name }},
           allow rwx pool={{ openstack_cinder_backup_pool.name }}
       mode: "0600"

To define a new pool, add a new dictionary like following:

.. code-block:: yaml

   openstack_SERVICE_pool:
     name: SERVICE
     pg_num: 32
     rule_name: ""
     application: "rbd"

Add the new pool to ``openstack_pools`` list and define a new key at
``openstack_keys``. Keys are used by Ceph clients to access the pool.

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

   ceph_mgr_modules:
     - dashboard
     [...]

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
