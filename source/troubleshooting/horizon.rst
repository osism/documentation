=======
Horizon
=======

Dashboard broken                             
================

.. image:: /images/horizon-broken.png                      

You have to cleanup and restart all horizon containers.    

.. code-block:: console

   $ docker exec -it horizon rm /var/lib/kolla/.local_settings.md5sum.txt && docker restart horizon
