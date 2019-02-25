====
Ceph
====

Execute the following commands on the manager node.

.. code-block:: console

   $ osism-ceph ROLE

* mons
* mgrs
* mdss (only when using cephfs)
* osds

After deploying Ceph, the individual keys must be stored in the configuration repository.

.. code-block:: console

   $ find . -name 'ceph.client.*.keyring'
   ./environments/kolla/files/overlays/cinder/cinder-volume/ceph.client.cinder.keyring
   ./environments/kolla/files/overlays/cinder/cinder-backup/ceph.client.cinder.keyring
   ./environments/kolla/files/overlays/cinder/cinder-backup/ceph.client.cinder-backup.keyring
   ./environments/kolla/files/overlays/gnocchi-statsd/ceph.client.gnocchi.keyring
   ./environments/kolla/files/overlays/nova/ceph.client.cinder.keyring
   ./environments/kolla/files/overlays/nova/ceph.client.nova.keyring
   ./environments/kolla/files/overlays/gnocchi-metricd/ceph.client.gnocchi.keyring
   ./environments/kolla/files/overlays/gnocchi-api/ceph.client.gnocchi.keyring
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

Client
======

.. code-block:: console

   $ osism-infrastructure helper --tags cephclient

Dashboard
=========

* http://docs.ceph.com/docs/luminous/mgr/dashboard/

* manual activation

.. code-block:: console

   $ ceph mgr module enable dashboard

* ``environments/ceph/configuration.yml``

.. code-block:: yaml

   ##########################
   # custom

   ceph_conf_overrides:
     mon:
       mgr initial modules: dashboard
