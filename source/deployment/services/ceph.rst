====
Ceph
====

.. contents::
   :depth: 2

Preparations
============

Prior to the deployment make sure NTP works correctly. In case of problems
https://chrony.tuxfamily.org/faq.html#_computer_is_not_synchronising
is a good entry point.

Execute the following commands to verify NTP is using the configured
ntp servers.

.. code-block:: console

   osism-ansible generic all -m shell -a 'chronyc sources'
   osism-ansible generic all -m shell -a 'chronyc tracking'

If ``multipath`` devices are in use, please use ``lvm_volume`` instead of ``devices``.

* Collect data of ``wwns`` of ``OSD`` disks

* Comment/delete the unnecessary bindings in ``/etc/multipath/bindings``, e.g.

.. code-block:: console

   $ ls -1 /dev/disk/by-id/wwn-* | grep part
   /dev/disk/by-id/wwn-0x5000039578c910c8-part1
   /dev/disk/by-id/wwn-0x5000039578c910c8-part2
   /dev/disk/by-id/wwn-0x5000039578c910c8-part3

   $ ls -1 /dev/disk/by-id/wwn-* | grep -v 0x5000039578c910c8
   /dev/disk/by-id/wwn-0x5000039588cb6e0c
   /dev/disk/by-id/wwn-0x5000039588cbe660
   /dev/disk/by-id/wwn-0x5000039588cbe668
   /dev/disk/by-id/wwn-0x5000039588d0c2ac
   /dev/disk/by-id/wwn-0x50000395a8cbd140
   /dev/disk/by-id/wwn-0x5000c50057486733
   /dev/disk/by-id/wwn-0x5000c50084059257
   /dev/disk/by-id/wwn-0x5000c5008405a007
   /dev/disk/by-id/wwn-0x5000c5008405b1b3
   /dev/disk/by-id/wwn-0x5000c5008405be57
   /dev/disk/by-id/wwn-0x5000c5008405ce0b
   /dev/disk/by-id/wwn-0x5000c5008405d21b
   /dev/disk/by-id/wwn-0x5000c5008405fdc3
   /dev/disk/by-id/wwn-0x5000c5008405fe7b
   /dev/disk/by-id/wwn-0x5000c50084bc36c7
   /dev/disk/by-id/wwn-0x5000c50084bc7923
   /dev/disk/by-id/wwn-0x5000c50084bc7973
   /dev/disk/by-id/wwn-0x5000c50084bcae5b
   /dev/disk/by-id/wwn-0x5000c50084bff5f7
   /dev/disk/by-id/wwn-0x5000c50084bff6cf
   /dev/disk/by-id/wwn-0x5000c50084c01f5b
   /dev/disk/by-id/wwn-0x5000cca05d6cc7c0
   /dev/disk/by-id/wwn-0x5000cca05d6d637c
   /dev/disk/by-id/wwn-0x5000cca05d6db0f0
   /dev/disk/by-id/wwn-0x5000cca07387d2e4
   /dev/disk/by-id/wwn-0x5000cca073ad15d0
   /dev/disk/by-id/wwn-0x5000cca073b5d618

write these information in, e.g. /dev/shm/wwns and create PV and LV with the following script

.. code-block:: console

   #!/usr/bin/env bash

   # creating lv config for ceph osds

   WWNLIST="/dev/shm/wwns"

   for WWN in `cat $WWNLIST`; do
       for LN in `grep -n $WWN $WWNLIST | awk -F":" '{ print $1 }'`; do
           vgcreate vg-drive-${LN} $WWN
           lvcreate -n lv-drive-${LN}-01 -l 100%FREE /dev/vg-drive-${LN}
       done
   done

* edit ``host_vars`` file of storage node

.. code-block:: console

   lvm_volumes:
     - data: lv-drive-1-01
       data_vg: vg-drive-1
     - data: lv-drive-2-01
       data_vg: vg-drive-2
       ...

Management services
===================

Execute the following commands on the manager node.

ceph-mon is the cluster monitor daemon for the Ceph distributed file system

.. code-block:: console

   osism-ceph mons

ceph-mgr is the cluster manager daemon for the Ceph distributed file system

.. code-block:: console

   osism-ceph mgrs

Client service
==============

Copy the keyring file ``/etc/ceph/ceph.client.admin.keyring`` located on the
first Ceph monitor node to
``environments/infrastructure/files/ceph/ceph.client.admin.keyring`` in the
configuration repository.

.. note::

   Please be careful to add a newline at the end of the keyring file.

After committing the change to the configuration repository, update the
configuration repository on the manager node.

.. code-block:: console

   osism-generic configuration

Ensure ``cephclient_mons`` in
``environments/infrastructure/configuration.yml`` is set to the list of IP
addresses of the Ceph monitor nodes in the OS-Storage (Ceph frontend) network.

Deploy the cephclient service by executing the following command on the manager
node.

.. code-block:: console

   osism-infrastructure cephclient

Storage services
================

Execute the following commands on the manager node.

ceph-mds is the metadata server daemon for the Ceph distributed file system.

.. code-block:: console

   osism-ceph mdss  # only when using cephfs

ceph-osd is the object storage daemon for the Ceph distributed file system.

.. note::

   Block devices must be raw and not have any GPT, FS, or RAID signatures. Existing signatures can
   be removed with ``wipefs``.

   .. code-block:: console

      sudo wipefs -f -a /dev/sdX
      /dev/sdX: 8 bytes were erased at offset 0x00000200 (gpt): 45 46 49 20 50 41 52 54
      /dev/sdX: 8 bytes were erased at offset 0x2e934855e00 (gpt): 45 46 49 20 50 41 52 54
      /dev/sdX: 2 bytes were erased at offset 0x000001fe (PMBR): 55 aa
      /dev/sdX: calling ioctl to re-read partition table: Success

.. code-block:: console

   osism-ceph osds

Post-processing
===============

After successfull Ceph deployment, additional service keys need to be stored in
the configuration repository. The keyring files are stored at ``/etc/ceph`` on
the Ceph monitor nodes.

.. note::

   Please be careful to add a newline at the end of the keyring file.

* Copy from ``/etc/ceph/ceph.client.admin.keyring`` to

  .. code-block:: console

     environments/infrastructure/files/ceph/ceph.client.admin.keyring

* Copy from ``/etc/ceph/ceph.client.cinder-backup.keyring`` to

  .. code-block:: console

     environments/kolla/files/overlays/cinder/cinder-backup/ceph.client.cinder-backup.keyring

* Copy from ``/etc/ceph/ceph.client.cinder.keyring`` to

  .. code-block:: console

     environments/kolla/files/overlays/cinder/cinder-backup/ceph.client.cinder.keyring
     environments/kolla/files/overlays/cinder/cinder-volume/ceph.client.cinder.keyring
     environments/kolla/files/overlays/nova/ceph.client.cinder.keyring


* Copy from ``/etc/ceph/ceph.client.glance.keyring`` to

  .. code-block:: console

     environments/kolla/files/overlays/glance/ceph.client.glance.keyring


* Copy from ``/etc/ceph/ceph.client.gnocchi.keyring`` to

  .. code-block:: console

     environments/kolla/files/overlays/gnocchi/ceph.client.gnocchi.keyring


* Copy from ``/etc/ceph/ceph.client.nova.keyring`` to

  .. code-block:: console

     environments/kolla/files/overlays/nova/ceph.client.nova.keyring

Update the configuration repository on the manager after committing the changes
by using command ``osism-generic configuration`` on the manager node.

After the initial deployment of the Ceph cluster, the ``openstack_config``
parameter in the ``environments/ceph/configuration.yml`` can be set to
``false``. It must only be set to ``true`` when new pools or keys are added.

Testing Ceph
============

* See :ref:`how to test Ceph <test-ceph>`.
