====
Ceph
====

Cluster start and stop
======================

* http://docs.ceph.com/docs/mimic/rados/operations/operating/#running-ceph-with-systemd
* https://www.openattic.org/posts/how-to-do-a-ceph-cluster-maintenanceshutdown/

**Stop**

.. warning::

   Ensure that any services/clients using Ceph are stopped and that the cluster is in a healthy state.

1. Set OSD flags

.. code-block:: console

   $ ceph osd set noout
   $ ceph osd set nobackfill
   $ ceph osd set norecover
   $ ceph osd set norebalance
   $ ceph osd set nodown
   $ ceph osd set pause

.. code-block:: console

   $ ceph -s
     cluster:
     [...]
       health: HEALTH_WARN
               pauserd,pausewr,nodown,noout,nobackfill,norebalance,norecover flag(s) set
 
     services:
     [...]
       osd: x osds: y up, z in
            flags pauserd,pausewr,nodown,noout,nobackfill,norebalance,norecover

2. Stop the services (manager, mds, ..) (one by one)

.. code-block:: console

   $ sudo systemctl stop ceph-mgr\*.service

3. Stop the osd servies (one by one)

.. code-block:: console

   $ sudo systemctl stop ceph-osd\*.service

4. Stop the monitor service (one by one)

.. code-block:: console

   $ sudo systemctl stop ceph-mon\*.service

**Start**

1. Start the monitor services (one by one)

.. code-block:: console

   $ sudo systemctl start ceph-mon\*.service

2. Start the osd services (one by one)

.. code-block:: console

   $ systemctl start ceph-osd@DEVICE.service              

3. Start the services (manager, mds, ..) (one by one)

.. code-block:: console

   $ sudo systemctl start ceph-mgr\*.service

4. Unset OSD flags

.. code-block:: console

   $ ceph osd unset pause
   $ ceph osd unset nodown
   $ ceph osd unset norebalance
   $ ceph osd unset norecover
   $ ceph osd unset nobackfill
   $ ceph osd unset noout

**Check**

.. code-block:: console

   $ sudo systemctl status ceph\*.service
   $ ceph -s
     cluster:
       id:     x
       health: HEALTH_OK
 
     services:
       mon: 3 daemons, quorum A,B,C
       mgr: A(active), standbys: B, C
       mds: cephfs-0/0/1 up 
       osd: x osds: y up, z in
 
     data:
       pools:   7 pools, 176 pgs
       objects: 2816 objects, 18856 MB
       usage:   69132 MB used, 44643 GB / 44711 GB avail
       pgs:     176 active+clean

Deep scrub distribution
=======================

* https://ceph.com/geen-categorie/deep-scrub-distribution/

Distribution per weekday:

.. code-block:: console

   $ for date in $(ceph pg dump | grep active | awk '{ print $20 })'; do date +%A -d $date; done | sort | uniq -c

Distribution per hours:

.. code-block:: console

   $ for date in $(ceph pg dump | grep active | awk '{ print $21 }'); do date +%H -d $date; done | sort | uniq -c

Set the number of placement groups
==================================

* http://docs.ceph.com/docs/mimic/rados/operations/placement-groups/#set-the-number-of-placement-groups

.. code-block:: console

   $ ceph osd pool set {pool-name} pg_num {pg_num}
   $ ceph osd pool set {pool-name} pgp_num {pgp_num}

.. note::

   The new number of PGs should also be updated in ``environments/ceph/configuration.yml``.
