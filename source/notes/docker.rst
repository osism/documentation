======
Docker
======

Stop / start all containers
===========================

When using the live restore (https://docs.docker.com/engine/admin/live-restore/) feature, not all
containers will be stopped when the docker service is stopped.

.. code-block:: shell

   $ docker stop $(docker ps -q)

.. code-block:: shell

   $ docker start $(docker ps -a -q)

.. note::

   Make sure that any containers intentionally stopped on the system are also started. This can lead to unintended side effects.
   Therefore, in many cases it is better to save the output of ``docker ps -q`` before the stop and, based on this, start the containers later.
