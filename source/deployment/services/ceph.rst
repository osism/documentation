====
Ceph
====

.. contents::
   :local:

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
