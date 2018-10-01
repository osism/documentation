=======
Horizon
=======

Horizon webinterface broken
===========================

Description
-----------

.. image:: /images/horizon-broken.png

Solution
--------

You have to cleanup and restart all horizon containers.

.. code-block:: console

   $ docker exec -it horizon rm /var/lib/kolla/.local_settings.md5sum.txt && docker restart horizon
