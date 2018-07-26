====
Ceph
====

* base directory: ``environments/ceph``

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

.. note::

   It is recommended to place the configuration of the network interfaces in the inventory.

.. code-block:: yaml

   ##########################################################
   # ceph

   monitor_interface: eth0

Pools & Keys
============

.. note::

   Remove unneeded pools & keys accordingly.

.. note::

   http://ceph.com/pgcalc can be used to calculate the number of PGs.

.. code-block:: yaml

   ##########################
   # pools & keys

   openstack_config: true

   openstack_glance_pool:
     name: images
     pg_num: 32
     rule_name: ""
   openstack_cinder_pool:
     name: volumes
     pg_num: 32
     rule_name: ""
   openstack_nova_pool:
     name: vms
     pg_num: 32
     rule_name: ""
   openstack_cinder_backup_pool:
     name: backups
     pg_num: 32
     rule_name: ""
   openstack_gnocchi_pool:
     name: metrics
     pg_num: 32
     rule_name: ""

   openstack_pools:
     - "{{ openstack_glance_pool }}"
     - "{{ openstack_cinder_pool }}"
     - "{{ openstack_nova_pool }}"
     - "{{ openstack_cinder_backup_pool }}"
     - "{{ openstack_gnocchi_pool }}"

   openstack_keys:
     - name: client.glance
       key: "$(ceph-authtool --gen-print-key)"
       mon_cap: "allow r"
       osd_cap: "allow class-read object_prefix rbd_children, allow rwx pool={{ openstack_glance_pool.name }}"
       mode: "0600"
       acls: []
     - name: client.cinder
       key: "$(ceph-authtool --gen-print-key)"
       mon_cap: "allow r"
       osd_cap: "allow class-read object_prefix rbd_children, allow rwx pool={{ openstack_cinder_pool.name }}, allow rwx pool={{ openstack_nova_pool.name }}, allow rx pool={{ openstack_glance_pool.name }}"
       mode: "0600"
       acls: []
     - name: client.cinder-backup
       key: "$(ceph-authtool --gen-print-key)"
       mon_cap: "allow r"
       osd_cap: "allow class-read object_prefix rbd_children, allow rwx pool={{ openstack_cinder_backup_pool.name }}"
       mode: "0600"
       acls: []
     - name: client.gnocchi
       key: "$(ceph-authtool --gen-print-key)"
       mon_cap: "allow r"
       osd_cap: "allow class-read object_prefix rbd_children, allow rwx pool={{ openstack_gnocchi_pool.name }}"
       mode: "0600"
       acls: []
     - name: client.nova
       key: "$(ceph-authtool --gen-print-key)"
       mon_cap: "allow r"
       osd_cap: "allow class-read object_prefix rbd_children, allow rwx pool=images, allow rwx pool=vms, allow rwx pool=volumes, allow rwx pool=backups"
       mode: "0600"
       acls: []

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
