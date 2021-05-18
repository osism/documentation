====
Ceph
====

.. contents::
   :local:

Node reboot
===========

1. Disable rebalancing temporarily

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

2. Reboot the node

   .. code-block:: console

      $ sudo reboot

3. When the reboot is complete enable cluster rebalancing again

   .. code-block:: console

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

Stop
----

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

2. Stop the management services (manager, mds, ..) (node by node)

   .. code-block:: console

      $ sudo systemctl stop ceph-mgr\*.service

3. Stop the osd services (node by node)

   .. code-block:: console

      $ sudo systemctl stop ceph-osd\*.service

4. Stop the monitor service (node by node)

   .. code-block:: console

      $ sudo systemctl stop ceph-mon\*.service

Start
-----

1. Start the monitor services (node by node)

   .. code-block:: console

      $ sudo systemctl start ceph-mon\*.service

2. Start the osd services (node by node)

   .. code-block:: console

      $ systemctl start ceph-osd@DEVICE.service

3. Start the management services (manager, mds, ..) (node by node)

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

Check
-----

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

- https://ceph.com/geen-categorie/deep-scrub-distribution/

* Distribution per weekday:

  .. code-block:: console

     $ for date in $(ceph pg dump | grep active | awk '{ print $20 })'; do date +%A -d $date; done | sort | uniq -c

* Distribution per hours:

  .. code-block:: console

     $ for date in $(ceph pg dump | grep active | awk '{ print $21 }'); do date +%H -d $date; done | sort | uniq -c

Set the number of placement groups
==================================

- http://docs.ceph.com/docs/mimic/rados/operations/placement-groups/#set-the-number-of-placement-groups
- http://ceph.com/pgcalc

.. code-block:: console

   $ ceph osd pool set {pool-name} pg_num {pg_num}
   set pool x pg_num to {pg_num}
   $ ceph osd pool set {pool-name} pgp_num {pgp_num}
   set pool x pgp_num to {pgp_num}

The new number of PGs should also be updated in ``environments/ceph/configuration.yml``.

1 pools have many more objects per pg than average
==================================================

- https://www.spinics.net/lists/ceph-devel/msg41403.html
- https://www.suse.com/de-de/support/kb/doc/?id=7018414

* Set ``mon pg warn max object skew = 0``

  .. code-block:: console

     $ ceph tell mon.* injectargs '--mon_pg_warn_max_object_skew 0'

* Restart the active manager service (http://lists.ceph.com/pipermail/ceph-users-ceph.com/2018-July/027856.html)

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

* Ceph daemons are configured to log to the console instead of log files.
  OSDs are configured to log to MONs.

  .. code-block:: console

     $ docker logs ceph-mon-ceph01

* Logs can become very big. ``docker logs`` provides some useful parameters
  to only show newest logs and to see new log messages when they appear.

  .. code-block:: console

     $ docker logs --tail 100 --follow ceph-mon-ceph01

Add new OSD
===========

* Add the new device to the ``devices`` list in the inventory of the corresponding host

* Execute ``osism-ceph osds -l HOST`` on the manager node

Remove OSD
==========

* Determine the OSD ID for the OSD to be removed

  .. code-block:: console

     ID CLASS WEIGHT  TYPE NAME               STATUS REWEIGHT PRI-AFF
     -1       0.03918 root default
     -3       0.01959     host testbed-node-0
      1   hdd 0.00980         osd.1               up  1.00000 1.00000
      3   hdd 0.00980         osd.3               up  1.00000 1.00000
     -5       0.01959     host testbed-node-1
      0   hdd 0.00980         osd.0               up  1.00000 1.00000
      2   hdd 0.00980         osd.2               up  1.00000 1.00000

* Determine the block device serverd by the OSD

  .. code-block:: console

     $ docker exec -it ceph-osd-3 ls -la /var/lib/ceph/osd/ceph-3/block
     lrwxrwxrwx 1 ceph ceph 92 Apr  2 15:10 /var/lib/ceph/osd/ceph-3/block -> /dev/ceph-f27fa071-baa4-4ee5-ba26-3b8a5d7231ec/osd-data-e5d0fe7f-c7dd-443d-9630-bf54ffba443e

  .. code-block:: console

     dragon@testbed-node-0:~$ sudo lvs -o +devices
       LV                                            VG                                        Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert Devices
       osd-data-c5c106dd-7461-40ad-b5cc-28137fb639fc ceph-01de26c3-61fb-4f6c-9fb9-1f3cdfcba444 -wi-ao---- <10.00g                                                     /dev/sdb(0)
       osd-data-e5d0fe7f-c7dd-443d-9630-bf54ffba443e ceph-f27fa071-baa4-4ee5-ba26-3b8a5d7231ec -wi-ao---- <10.00g                                                     /dev/sdc(0)

* Remove the device from the ``devices`` list in the inventory of the corresponding host

* Mark the OSD as out

  .. code-block:: console

     dragon@testbed-manager:~$ ceph osd out osd.3
     marked out osd.3.

* Stop the ceph-osd service with ``sudo systemctl stop ceph-osd@3``

* Purge the OSD

  .. code-block:: console

     dragon@testbed-node-0:~$ ceph osd purge osd.3 --yes-i-really-mean-it
     purged osd.3

* Verify the OSD is removed from the node in the CRUSH map

  .. code-block:: console

     dragon@testbed-node-0:~$ ceph osd tree
     ID CLASS WEIGHT  TYPE NAME               STATUS REWEIGHT PRI-AFF
     -1       0.02939 root default
     -3       0.00980     host testbed-node-0
      1   hdd 0.00980         osd.1               up  1.00000 1.00000
     -5       0.01959     host testbed-node-1
      0   hdd 0.00980         osd.0               up  1.00000 1.00000
      2   hdd 0.00980         osd.2               up  1.00000 1.00000

* Zap the block device

  .. code-block:: console

     dragon@testbed-node-0:~$ sudo sgdisk --zap-all /dev/sdc
     Creating new GPT entries.
     GPT data structures destroyed! You may now partition the disk using fdisk or
     other utilities.

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

* disable defect OSD/disk

  .. code-block:: console

     $ ceph osd out 22
     $ sudo systemctl stop ceph-osd@sdk.service
     $ ceph osd purge osd.22

* Prepare new OSD

  .. code-block:: console

     $ docker start -ai ceph-osd-prepare-ceph04-sdk
     $ sudo systemctl start ceph-osd@sdk.service

* Add OSD to tree

  .. code-block:: console

     $ ceph osd df tree
        CLASS WEIGHT REWEIGHT SIZE   USE    AVAIL  %USE  VAR TYPE NAME
                 7.4       -  3709G  2422G  1287G 65.30 1.06  hdd ceph04-hdd
         hdd     3.7       0      0      0      0     0    0        osd.22
         hdd     3.7 1.00000  3709G  2422G  1287G 65.30 1.08        osd.6
         ...
         hdd     0.0       0      0      0      0     0    0 osd.27

     $ ceph osd crush create-or-move osd.22 3.7 hdd=ceph04-hdd
     $ ceph osd df tree
        CLASS WEIGHT REWEIGHT SIZE   USE    AVAIL  %USE  VAR TYPE NAME
                 7.4       -  3709G  2422G  1287G 65.30 1.06  hdd ceph04-hdd
         hdd     3.7 1.00000  3709G      0  3709G     0    0        osd.22
         hdd     3.7 1.00000  3709G  2422G  1287G 65.30 1.08        osd.6

Add new pool
============

* http://docs.ceph.com/docs/mimic/rados/operations/pools/

.. code-block:: console

   $ ceph osd pool create sample 32 32
   pool 'sample' created
   $ ceph osd pool application enable sample rbd
   enabled application 'rbd' on pool 'sample'

* http://docs.ceph.com/docs/mimic/rados/operations/user-management/

.. code-block:: console

   $ ceph auth get client.cinder
   [client.cinder]
      key = ...
      caps mon = "allow r"
      caps osd = "allow class-read object_prefix rbd_children, allow rwx pool=volumes, allow rwx pool=vms, allow rx pool=images"
   exported keyring for client.cinder
   $ ceph auth caps client.cinder mon 'allow r' osd 'allow class-read object_prefix rbd_children, allow rwx pool=images, allow rwx pool=vms, allow rwx pool=volumes, allow rwx pool=backups, allow rwx pool=sample'
   updated caps for client.cinder

.. code-block:: console

   $ ceph auth get client.nova
   [client.nova]
      key = ...
      caps mon = "allow r"
      caps osd = "allow class-read object_prefix rbd_children, allow rwx pool=images, allow rwx pool=vms, allow rwx pool=volumes, allow rwx pool=backups"
   exported keyring for client.nova
   $ ceph auth caps client.nova mon 'allow r' osd 'allow class-read object_prefix rbd_children, allow rwx pool=images, allow rwx pool=vms, allow rwx pool=volumes, allow rwx pool=backups, allow rwx pool=sample'
   updated caps for client.nova

Export image
============

.. code-block:: console

   $ rbd export --pool=volumes volume-035f3636-ad68-4562-88f5-11d7e295d03e /home/dragon/035f3636-ad68-4562-88f5-11d7e295d03e.img
   $ docker cp cephclient_cephclient_1:/home/dragon/035f3636-ad68-4562-88f5-11d7e295d03e.img /tmp

.. code-block:: console

   $ docker exec -it cephclient_cephclient_1 rm -f /home/dragon/035f3636-ad68-4562-88f5-11d7e295d03e.img
   $ rm -f /tmp/035f3636-ad68-4562-88f5-11d7e295d03e.img

Repair PGs
==========

* Health of Ceph cluster

.. code-block:: console

   $ sudo ceph status
     cluster:
       id:     0155072f-6a71-4f5c-8967-f86e5307033f
       health: HEALTH_ERR
               4 scrub errors
               Possible data damage: 1 pg inconsistent

   $ sudo ceph health detail
   HEALTH_ERR 4 scrub errors; Possible data damage: 1 pg inconsistent
   OSD_SCRUB_ERRORS 4 scrub errors
   PG_DAMAGED Possible data damage: 1 pg inconsistent
       pg 54.76 is active+clean+inconsistent, acting [39,6,15]

* Repair the PG

.. code-block:: console

   $ sudo ceph pg repair 54.76
   instructing pg 54.76 on osd.39 to repair

* give the Ceph cluster some time for repair and check health

.. code-block:: console

   $ sudo ceph health detail
   HEALTH_OK

   $ sudo ceph status
     cluster:
       id:     0155072f-6a71-4f5c-8967-f86e5307033f
       health: HEALTH_OK

Rebalance the cluster
=====================

* https://docs.ceph.com/docs/master/rados/operations/control/

1. Test what OSDs would be affected by teh reweight

.. code-block:: console

    $ sudo ceph osd test-reweight-by-utilization
    no change
    moved 6 / 4352 (0.137868%)
    avg 51.8095
    stddev 12.3727 -> 12.3621 (expected baseline 7.15491)
    min osd.10 with 30 -> 30 pgs (0.579044 -> 0.579044 * mean)
    max osd.68 with 92 -> 92 pgs (1.77574 -> 1.77574 * mean)

    oload 120
    max_change 0.05
    max_change_osds 4
    average_utilization 0.4187
    overload_utilization 0.5025
    osd.14 weight 0.9500 -> 0.9000
    osd.27 weight 0.9500 -> 0.9000
    osd.37 weight 0.9500 -> 0.9000
    osd.29 weight 1.0000 -> 0.9500

2. If the OSDs match your "fullest" OSDs execute the reweight

.. code-block:: console

    $ sudo ceph osd reweight-by-utilization
    no change
    moved 6 / 4352 (0.137868%)
    avg 51.8095
    stddev 12.3727 -> 12.3621 (expected baseline 7.15491)
    min osd.10 with 30 -> 30 pgs (0.579044 -> 0.579044 * mean)
    max osd.68 with 92 -> 92 pgs (1.77574 -> 1.77574 * mean)

    oload 120
    max_change 0.05
    max_change_osds 4
    average_utilization 0.4187
    overload_utilization 0.5025
    osd.14 weight 0.9500 -> 0.9000
    osd.27 weight 0.9500 -> 0.9000
    osd.37 weight 0.9500 -> 0.9000
    osd.29 weight 1.0000 -> 0.9500

3. Wait for the cluster to rebalance itself and check disk usage again. Repeat above if necessary

HEALTH_WARN application not enabled on 1 pool(s)
================================================

.. code-block:: console

   $ ceph health detail
   HEALTH_WARN application not enabled on 1 pool(s)
   POOL_APP_NOT_ENABLED application not enabled on 1 pool(s)
       application not enabled on pool 'default.rgw.log'
       use 'ceph osd pool application enable <pool-name> <app-name>', where <app-name> is 'cephfs', 'rbd', 'rgw', or freeform for custom applications.
   $ ceph osd pool application enable default.rgw.log rgw
   enabled application 'rgw' on pool 'default.rgw.log'

3 monitors have not enabled msgr2
=================================

Normal during upgrade from Luminous to Nautilus.

* https://docs.ceph.com/en/latest/rados/configuration/msgr2/

.. code-block:: none

   cluster:
     id:     11111111-1111-1111-1111-111111111111
     health: HEALTH_WARN
             3 monitors have not enabled msgr2
