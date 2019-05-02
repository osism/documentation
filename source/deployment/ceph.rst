====
Ceph
====

.. contents::
   :local:

Execute the following commands on the manager node.

Before deployment make sure that NTP works.

Management services
===================

.. code-block:: console

   $ osism-ceph mons
   $ osism-ceph mgrs

Client service
==============

* Set the ``ceph.client.admin.keyring`` in the ``environments/infrastructure/files/ceph/ceph.client.admin.keyring`` file

  * Key can be found in the directory ``/etc/ceph`` on the first Ceph monitor node
  * Update the configuration repository on the manager node

* Deploy the cephclient service on the monitor nodes

.. code-block:: console

   $ osism-infrastructure helper --tags cephclient

Storage services
================

.. code-block:: console

   $ osism-ceph mdss  # only when using cephfs
   $ osism-ceph osds

Post-processing
===============

After deploying Ceph, the remaining individual keys must be stored in the configuration repository.

.. code-block:: console

   $ find . -name 'ceph.client.*.keyring'
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

   $ ls -1 /etc/ceph/
   ceph.client.admin.keyring
   ceph.client.cinder-backup.keyring
   ceph.client.cinder.keyring
   ceph.client.glance.keyring
   ceph.client.gnocchi.keyring
   ceph.client.nova.keyring
   ceph.conf
   ceph.mon.keyring

Don't forget to update the configuration repository on the manager afterwards.
