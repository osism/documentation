======
Docker
======

.. warning::

   When upgrading, the Docker service is restarted. As a result, it comes to a restart of the container.
   This can lead to interruptions in individual services.

* ``environments/manager/configuration.yml``

.. code-block:: yaml

   docker_version: 18.06.1

* ``environments/generic/configuration.yml``

.. code-block:: yaml

   docker_version: 18.06.1

.. note::

   It is recommended to update the Docker services one by one.

.. code-block:: console

   $ osism-generic docker
