====
Ceph
====

.. note::

   The subsequent commands are executed within the ``ceph-mon`` container on a Ceph monitor node.

   .. code-block:: console

      $ docker exec -it ceph-mon-cephmon1 bash
      dragon@e0e0987bd105:/$

Monitors
========

.. note::

   Output after deployment of mon services.

.. code-block:: console

   $ ceph -s
   cluster:
     id:     d950d67e-fd17-47c2-8620-cbc30d55ec0c
     health: HEALTH_OK

   services:
     mon: 3 daemons, quorum ceph1,ceph2,ceph3
     mgr: no daemons active
     mds: cephfs-0/0/1 up
     osd: 0 osds: 0 up, 0 in

   data:
     pools:   0 pools, 0 pgs
     objects: 0 objects, 0 bytes
     usage:   0 kB used, 0 kB / 0 kB avail
     pgs:

Managers
========

.. note::

   Output after deployment of mon and mgr services.

.. code-block:: console

   $ ceph -s
   cluster:
     id:     d950d67e-fd17-47c2-8620-cbc30d55ec0c
     health: HEALTH_WARN
             Reduced data availability: 176 pgs inactive
   services:
     mon: 3 daemons, quorum ceph1,ceph2,ceph3
     mgr: ceph1(active), standbys: ceph2, ceph2
     mds: cephfs-0/0/1 up
     osd: 0 osds: 0 up, 0 in

   data:
     pools:   7 pools, 176 pgs
     objects: 0 objects, 0 bytes
     usage:   0 kB used, 0 kB / 0 kB avail
     pgs:     100.000% pgs unknown
              176 unknown

OSDs
====

.. note::

   Output after deployment of mon, mgr and OSD services.

.. code-block:: console

   $ ceph -s
   cluster:
     id:     d950d67e-fd17-47c2-8620-cbc30d55ec0c
     health: HEALTH_OK

   services:
     mon: 3 daemons, quorum ceph1,ceph2,ceph3
     mgr: ceph1(active), standbys: ceph2, ceph2
     mds: cephfs-0/0/1 up
     osd: 6 osds: 6 up, 6 in

   data:
     pools:   7 pools, 176 pgs
     objects: 0 objects, 0 bytes
     usage:   6170 MB used, 12339 GB / 12345 GB avail
     pgs:     176 active+clean
