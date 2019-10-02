====
Ceph
====

* Output after deployment of mon services

  .. code-block:: console

     $ docker exec -it ceph-mon-HOSTNAME bash
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

* Output after deployment of mon and mgr services

  .. code-block:: console

     $ docker exec -it ceph-mon-HOSTNAME bash
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

* Output after deployment of mon, mgr and osd services

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

* List users (http://docs.ceph.com/docs/master/rados/operations/user-management/)

  .. code-block:: console

     $ ceph auth ls

* List pools (http://docs.ceph.com/docs/master/rados/operations/pools/)

  .. code-block:: console

     $ ceph osd lspools
     1 images,2 volumes,3 vms,4 backups,5 metrics

* List osd details (http://docs.ceph.com/docs/master/rados/operations/monitoring-osd-pg/)

  .. code-block:: console

     $ ceph osd stat
     $ ceph osd tree

* List cluster details (http://docs.ceph.com/docs/master/rados/operations/monitoring/)

  .. code-block:: console

     $ ceph status
     $ ceph health
     HEALTH_OK
     $ ceph df
     $ ceph mon_status | python -m json.tool
     $ ceph quorum_status | python -m json.tool
