=======
Horizon
=======

Dashboard broken                             
================

.. image:: /images/horizon-broken.png                      

You have to cleanup and restart all horizon containers.    

.. code-block:: shell                                      

   $ docker exec -it horizon rm /tmp/.local_settings.md5sum.txt && docker restart horizon                             
