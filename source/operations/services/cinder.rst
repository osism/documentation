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
