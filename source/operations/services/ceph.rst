====
Ceph
====

Node reboot
===========

.. code-block:: console

   $ ceph osd set noout
   noout is set
   $ ceph osd set norebalance
   norebalance is set
   $ ceph -s
     cluster:
       id:     xxx
       health: HEALTH_WARN
               noout,norebalance flag(s) set
   [...]
   $ sudo reboot
   $ ceph osd unset noout
   noout is unset
   $ ceph osd unset norebalance
   norebalance is unset
   $ ceph -s
     cluster:
       id:     xxx
       health: HEALTH_OK
   [...]

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
   set pool x pg_num to {pg_num}
   $ ceph osd pool set {pool-name} pgp_num {pgp_num}
   set pool x pgp_num to {pgp_num}

.. note::

   The new number of PGs should also be updated in ``environments/ceph/configuration.yml``.

1 pools have many more objects per pg than average
==================================================

* https://www.spinics.net/lists/ceph-devel/msg41403.html
* https://www.suse.com/de-de/support/kb/doc/?id=7018414

* set ``mon pg warn max object skew = 0``

.. code-block:: console

   $ ceph tell mon.* injectargs '--mon_pg_warn_max_object_skew 0'

* restart the active manager service (http://lists.ceph.com/pipermail/ceph-users-ceph.com/2018-July/027856.html)

.. code-block:: console

   $ sudo systemctl restart ceph-mgr\*.service

* ``environments/ceph/configuration.yml``

.. code-block:: yaml

   ##########################
   # custom

   ceph_conf_overrides:
     global:
       mon pg warn max object skew: 0

Logging
=======

* Ceph daemons are configured to log to the console instead of log files. OSDs are configured to log to MONs.

.. code-block:: console

   $ docker logs ceph-mon-ceph01

* Logs can become very big. ``docker logs`` provides some useful parameters to only show newest logs and to see new log messages when they appear.

.. code-block:: console

   $ docker logs --tail 100 --follow ceph-mon-ceph01

Replace defect OSD
==================

* Locate defect OSD

.. code-block:: console

   $ ceph osd metadata osd.22
     "bluefs_slow_dev_node": "sdk",
     "hostname": "ceph04",

   $ ssh ceph04
   $ dmesg -T | grep sdk | grep -i error
     ...
     blk_update_request: I/O error, dev sdk, sector 7501476358
     Buffer I/O error on dev sdk1, logical block 7470017030, async page read
     blk_update_request: I/O error, dev sdk, sector 7501476359
     Buffer I/O error on dev sdk1, logical block 7470017031, async page read

* Find and replace actual hardware

.. code-block:: console

   $ sudo udevadm info --query=all --name=/dev/sdk
   $ sudo hdparm -I /dev/sdk

* Prepare new OSD

.. code-block:: console

   $ docker start -ai ceph-osd-prepare-ceph04-sdk

* Add OSD to tree

.. code-block:: console

   $ ceph osd df tree
      CLASS WEIGHT REWEIGHT SIZE   USE    AVAIL  %USE  VAR TYPE NAME
               7.4       -  3709G  2422G  1287G 65.30 1.06  hdd ceph04-hdd
       hdd     3.7       0      0      0      0     0    0        osd.22
       hdd     3.7 1.00000  3709G  2422G  1287G 65.30 1.08        osd.6
       ...
       hdd     0.0       0      0      0      0     0    0 osd.27

   $ ceph osd crush create-or-move osd.27 3.7 hdd=ceph04-hdd
   $ ceph osd purge osd.22
   $ ceph osd df tree
      CLASS WEIGHT REWEIGHT SIZE   USE    AVAIL  %USE  VAR TYPE NAME
               7.4       -  3709G  2422G  1287G 65.30 1.06  hdd ceph04-hdd
       hdd     3.7 1.00000  3709G      0  3709G     0    0        osd.27
       hdd     3.7 1.00000  3709G  2422G  1287G 65.30 1.08        osd.6

Export image
============

.. code-block:: console

   $ rbd export --pool=volumes volume-035f3636-ad68-4562-88f5-11d7e295d03e /home/dragon/035f3636-ad68-4562-88f5-11d7e295d03e.img
   $ docker cp cephclient_cephclient_1:/home/dragon/035f3636-ad68-4562-88f5-11d7e295d03e.img /tmp

.. code-block:: console

   $ docker exec -it cephclient_cephclient_1 rm -f /home/dragon/035f3636-ad68-4562-88f5-11d7e295d03e.img
   $ rm -f /tmp/035f3636-ad68-4562-88f5-11d7e295d03e.img
