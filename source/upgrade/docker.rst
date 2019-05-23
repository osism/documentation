======
Docker
======

.. warning::

   When upgrading, the Docker service is restarted. As a result, it comes to a restart of the container.
   This can lead to interruptions in individual services.

* ``environments/configuration.yml``

.. code-block:: yaml

   docker_version: '5:18.09.2'

.. note::

   This ``5:`` must be prepended starting with version ``18.09``.

   Check available version under Ubuntu with ``apt-cache madison docker-ce``.

   .. code-block:: console

      # apt-cache madison docker-ce
       docker-ce | 5:18.09.2~3-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
       docker-ce | 5:18.09.1~3-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
       docker-ce | 5:18.09.0~3-0~ubuntu-xenial | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
       docker-ce | 18.06.3~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
       docker-ce | 18.06.2~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
       docker-ce | 18.06.1~ce~3-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
      [...]

.. note::

   It is recommended to update the Docker services one by one.

.. code-block:: console

   $ osism-generic docker
