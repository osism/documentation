======
Cinder
======

* https://docs.openstack.org/cinder/latest/man/cinder-manage.html

Remove service
==============

.. note::

   This command is executed on a controller node.

.. code-block:: shell

   $ docker exec -it cinder_api cinder-manage service remove cinder-volume 50-10@rbd-volumes
   Service cinder-volume on host 50-10@rbd-volumes removed.

Purge deleted rows
==================

.. note::

   This command is executed on a controller node.

.. code-block:: console

   $ docker exec -it cinder_api cinder-manage db purge 90

ImageBusy error raised while deleting rbd volume
================================================

* https://der-jd.de/blog/2018/2018-12-27-openstack-ceph-luminous-upgrade/

.. code::

   WARNING cinder.volume.drivers.rbd [req-...] ImageBusy error raised while deleting rbd volume. This may have been caused by a connection from a client that has crashed and, if so, may be resolved by retrying the delete after 30 seconds has elapsed.: ImageBusy: [errno 16] error removing image
   ERROR cinder.volume.manager [req-...] Unable to delete busy volume.: VolumeIsBusy: ImageBusy error raised while deleting rbd volume. This may have been caused by a connection from a client that has crashed and, if so, may be resolved by retrying the delete after 30 seconds has elapsed.

.. code-block:: console

   $ rbd lock list -p volumes volume-604dfc80-7626-4e6b-b7fd-5c90de36015a
   There is 1 exclusive lock on this image.
   Locker           ID                   Address
   client.118718703 auto 140588574332144 a.b.c.d:0/42644142

Make sure that the instance belonging to the volume no longer exists. If this is the case,
the lock can be deleted manually.

.. code-block:: console

   $ rbd lock rm -p volumes volume-604dfc80-7626-4e6b-b7fd-5c90de36015a "auto 140588574332144" client.118718703

There are still untyped volumes unmigrated
==========================================

* http://heiterbiswolkig.blogs.nde.ag/2020/08/28/openstack-ha-upgrade-part-ii/

.. code-block:: none

   Error during database migration: Migration cannot continue until all volumes have been migrated
   to the `__DEFAULT__` volume type. Please run `cinder-manage db online_data_migrations`.
   There are still untyped volumes unmigrated.

Get the ID of the ``__DEFAULT__`` volume type:

.. code-block:: sql

   SELETE id, name from volume_types WHERE deleted=0

Set the ``volume_type_id`` where the ``volume_type_id`` is not set:

.. code-block:: sql

   UPDATE cinder.snapshots SET volume_type_id='<UUID>' WHERE volume_type_id IS NULL;
   UPDATE cinder.volumes SET volume_type_id='<UUID>' WHERE volume_type_id IS NULL;

Cinder and Redis
================

.. code:: console

   INFO cinder.service [-] Starting cinder-volume node (version 17.1.1)
   ERROR oslo_service.service [-] Error starting thread.: tooz.coordination.ToozConnectionError: No master found for 'kolla'
   ERROR oslo_service.service Traceback (most recent call last):
   ...
   ERROR oslo_service.service     raise MasterNotFoundError("No master found for %r" % (service_name,))
   ERROR oslo_service.service redis.sentinel.MasterNotFoundError: No master found for 'kolla'
   ERROR oslo_service.service The above exception was the direct cause of the following exception:
   ERROR oslo_service.service Traceback (most recent call last):
   ...
   ERROR oslo_service.service tooz.coordination.ToozConnectionError: No master found for 'kolla'

Make sure Redis is installed (:ref:`deploymentservicesopenstackinfrastructure`), up and running (:ref:`testinfrastructureredis`).
