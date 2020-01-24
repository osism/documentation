====
Ceph
====

.. note::

   At least 3 monitor services are required to perform an upgrade.

Luminous -> Luminous
====================

* ``environments/configuration.yml``

.. code-block:: yaml

   ceph_manager_version: 20180807-0

* ``environments/manager/configuration.yml``

.. code-block:: yaml

   ceph_manager_version: 20180807-0

* update the manager with ``osism-manager manager``

* check versions

.. code-block:: console

   $ ceph versions
   {
       "mon": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 3
       },
       "mgr": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 3
       },
       "osd": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 12
       },
       "mds": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 3
       },
       "overall": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 21
       }
   }

* start the update

.. code-block:: console

   $ osism-ceph rolling_update -e @/ansible/group_vars/all/defaults.yml
   Are you sure you want to upgrade the cluster? [no]: yes
   [...]

* check versions during the update

.. code-block:: console

   $ ceph versions
   {
       "mon": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 2,
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 1
       },
       "mgr": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 3
       },
       "osd": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 12
       },
       "mds": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 3
       },
       "overall": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 20,
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 1
       }
   }

* check versions after the update

.. code-block:: console

   $ ceph versions

   {
       "mon": {
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 3
       },
       "mgr": {
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 3
       },
       "osd": {
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 12
       },
       "mds": {
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 3
       },
       "overall": {
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 21
       }
   }



Filestore -> Bluestore
======================

Migrating a Ceph cluster from filestore to bluestore is done host by host.
All of the following steps are necessary to migrate one single OSD host from filestore to bluestore.

Output in this section is shortened.

Stop all OSD daemons
--------------------

* Check which OSDs belong to host. Choose which OSD to shut down next and have a look at other OSDs that will take over the pgs from this OSD. Is enough capability available?

  .. code-block:: console

     $ ceph osd df tree
       REWEIGHT SIZE   USE    AVAIL  %USE  VAR TYPE NAME
             -      0      0      0     0    0  hdd ceph01
             0      0      0      0     0    0        osd.5
       1.00000  3725G  1922G  1803G 51.59 1.08        osd.1
             - 11127G  5629G  5498G 50.59 1.06  hdd ceph03
       1.00000  3709G  2116G  1592G 57.06 1.20        osd.3
       1.00000  3709G  1822G  1886G 49.13 1.03        osd.6

* Also check if data is distributed evenly between remaining OSDs. If not, reweight OSDs with a lot of data.
  In particular look for disks that are nearly full.

  .. code-block:: console

     $ ceph osd df tree
       REWEIGHT SIZE   USE    AVAIL  %USE  VAR TYPE NAME
             -  3725G  1922G  1803G 51.59 1.08  hdd ceph01-hdd
             0      0      0      0     0    0        osd.5
       1.00000  3725G  1922G  1803G 51.59 1.08        osd.1
             - 11127G  5629G  5498G 50.59 1.06  hdd ceph03-hdd
       1.00000  3709G  2116G  1592G 57.06 1.20        osd.3
       1.00000  3709G  1822G  1886G 49.13 1.03        osd.6

     $ ceph osd reweight osd.3 0.95
     $ ceph osd df tree
       REWEIGHT SIZE   USE    AVAIL  %USE  VAR TYPE NAME
             -      0      0      0     0    0  hdd ceph01-hdd
             0      0      0      0     0    0        osd.5
       1.00000  3725G  1922G  1803G 51.59 1.08        osd.1
             - 11127G  5629G  5498G 50.59 1.06  hdd ceph03-hdd
       0.95000  3709G  2116G  1592G 57.06 1.20        osd.3
       1.00000  3709G  1822G  1886G 49.13 1.03        osd.6

* Find out which OSD belongs to which real disk / parition.

  .. code-block:: console

     $ docker exec -it ceph-osd-ceph01-sdf ceph-disk list
        /dev/sdf :
         /dev/sdf1 ceph data, active, cluster ceph, osd.1, journal /dev/sdd3

* Stop ceph-osd daemon for this disk.

  .. code-block:: console

     $ sudo systemctl stop ceph-osd@sdf

* It is recommended to wait until the cluster is recovered, before you shutdown the next OSD.

Delete disks
------------

* After all OSD daemons are stopped, you overwrite the partition table, so Ceph can reuse the disk.
  Be careful not do delete data on disks that are not used by Ceph.

  .. code-block:: console

     $ parted /dev/sdf print
     $ parted /dev/sdf mklabel gpt

Adjust and apply configuration
------------------------------

* Double check order of parameters `devices` and `dedicated_devices` in `inventory/host_vars/ceph01.yml` .
  Add parameter `osd_objectstore: bluestore` there.

* Before applying the new configuration, tell Ceph not to automatically insert new OSDs into the tree.

  .. code-block:: console

     $ ceph osd set noin

* Roll out new configuration.

  .. code-block:: console

     $ osism-generic configuration
     $ osism-ceph osds --limit ceph01

Replace old OSDs by new ones
----------------------------

* Replace each old OSD in the tree by the corresponding new one. That is, pick a new OSD of correct size and type.
  You can find information about the new OSDs with the `ceph osd metadata` command.
  Also add the corresponding device class if necessary and set values for weight and reweight.
  Be sure to not to purge the old OSD too early or you won't know where to place which new OSD or which device class to set.

  .. code-block:: console

     $ ceph osd df tree
      CLASS WEIGHT REWEIGHT SIZE   USE    AVAIL  %USE  VAR TYPE NAME
               7.4       -      0      0      0     0    0  hdd ceph01-hdd
       hdd     3.7       0      0      0      0     0    0        osd.5
       hdd     3.7       0      0      0      0     0    0        osd.1
               7.4       - 11127G  7629G  3498G 68.56 1.06  hdd ceph03-hdd
       hdd     3.7 0.95000  3709G  2516G  1193G 67.83 1.10        osd.3
       hdd     3.7 1.00000  3709G  2422G  1287G 65.30 1.08        osd.6
       ...
       hdd     0.0       0      0      0      0     0    0 osd.26
       hdd     0.0       0      0      0      0     0    0 osd.27

     $ ceph osd metadata osd.26
        ...
        "bluefs_slow_type": "hdd",
        "bluefs_slow_dev_node": "sdf",
        ...
     $ ceph osd crush create-or-move osd.26 3.7 hdd=ceph01-hdd
     $ #ceph osd crush rm-device-class osd.26       # only for changing device-class
     $ #ceph osd crush set-device-class hdd osd.26  # only for changing device-class
     $ ceph osd reweight osd.26 1.0
     $ ceph osd purge osd.1
     $ ceph osd df tree
      CLASS WEIGHT REWEIGHT SIZE   USE    AVAIL  %USE  VAR TYPE NAME
               7.4       -  3709G      0  3709G     0    0  hdd ceph01-hdd
       hdd     3.7       0      0      0      0     0    0        osd.5
       hdd     3.7     1.0  3709G      0  3709G     0    0        osd.26
               7.4       - 11127G  7629G  3498G 68.56 1.06  hdd ceph03-hdd
       hdd     3.7 0.95000  3709G  2516G  1193G 67.83 1.10        osd.3
       hdd     3.7 1.00000  3709G  2422G  1287G 65.30 1.08        osd.6
       ...
       hdd     0.0       0      0      0      0     0    0 osd.27

* Once you're done wih all OSDs, clear the `noin` flag.

  .. code-block:: console

     $ ceph osd unset noin

* You should wait for the cluster to rebalance completely, before starting with the next host.

Cleanup
-------

* Once you have migrated all OSD hosts in the cluster, you can remove the `osd_objectstore: bluestore` parameter from
  the host files in `inventory/host_vars` and instead updated in `environments/ceph/configuration.yml` .

.. code-block:: yaml

   ##########################
   # generic

   osd_objectstore: bluestore
