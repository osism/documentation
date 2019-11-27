====
Ceph
====

.. contents::
   :local:

Preparations
============

Before the deployment make sure that NTP really works. In case of problems
https://chrony.tuxfamily.org/faq.html#_computer_is_not_synchronising
is a good entry point.

.. code-block:: console

   osism-ansible generic all -m shell -a 'chronyc sources'
   osism-ansible generic all -m shell -a 'chronyc tracking'

Management services
===================

* ceph-mon is the cluster monitor daemon for the Ceph distributed file system

  .. code-block:: console

     osism-ceph mons

* ceph-mgr is the cluster manager daemon for the Ceph distributed file system

  .. code-block:: console

     osism-ceph mgrs

Client service
==============

* Set the ``ceph.client.admin.keyring`` in the
  ``environments/infrastructure/files/ceph/ceph.client.admin.keyring`` file in
  the configuration repository

  * Key can be found in the directory ``/etc/ceph`` on the first Ceph monitor
    node
  * Update the configuration repository on the manager node with
    ``osism-generic configuration``

* Ensure that ``cephclient_mons`` is set accordingly in the ``environments/infrastructure/configuration.yml`` file

* Deploy the cephclient service

.. code-block:: console

   osism-infrastructure helper --tags cephclient

Storage services
================

* ceph-mds is the metadata server daemon for the Ceph distributed file system

  .. code-block:: console

     osism-ceph mdss  # only when using cephfs

* ceph-osd is the object storage daemon for the Ceph distributed file system

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

  .. note::

     This workaround is only necessary when using OSISM <= 2019.3.0 (ceph-ansible 3.1.x). In newer
     versions (OSISM >= 2019.4.0, ceph-ansible >= 3.2.x) this problem has been fixed.

     Due to a bug the distribution of the Ceph keys fails in the first run. The following intermediate
     step is currently required.

     Execute the following command on the first Ceph monitor node. Then ``osism-ceph osds`` must be
     executed again.

     .. code-block:: console

        sudo cp /opt/cephclient/configuration/*.keyring /etc/ceph

Post-processing
===============

After deploying Ceph, the remaining individual keys must be stored in the configuration repository.

.. code-block:: console

   find . -name 'ceph.client.*.keyring'

.. code-block:: console

   ./environments/kolla/files/overlays/cinder/cinder-volume/ceph.client.cinder.keyring
   ./environments/kolla/files/overlays/cinder/cinder-backup/ceph.client.cinder.keyring
   ./environments/kolla/files/overlays/cinder/cinder-backup/ceph.client.cinder-backup.keyring
   ./environments/kolla/files/overlays/gnocchi/ceph.client.gnocchi.keyring
   ./environments/kolla/files/overlays/nova/ceph.client.cinder.keyring
   ./environments/kolla/files/overlays/nova/ceph.client.nova.keyring
   ./environments/kolla/files/overlays/glance-api/ceph.client.glance.keyring
   ./environments/infrastructure/files/ceph/ceph.client.admin.keyring

The keys can be found in the directory ``/etc/ceph`` on one of the Ceph monitor nodes.

.. code-block:: console

   ls -1 /etc/ceph/

.. code-block:: console

   ceph.client.admin.keyring
   ceph.client.cinder-backup.keyring
   ceph.client.cinder.keyring
   ceph.client.glance.keyring
   ceph.client.gnocchi.keyring
   ceph.client.nova.keyring
   ceph.conf
   ceph.mon.keyring

Don't forget to update the configuration repository on the manager afterwards
using command ``osism-generic configuration``.

After the initial deployment of the Ceph clusters, the ``openstack_config``
parameter in the ``environments/ceph/configuration.yml`` can be set to
``false``. It must only be set to ``true`` when new pools or keys are added.

Testing Ceph
============

* See :ref:`how to test Ceph <test-ceph>`.
