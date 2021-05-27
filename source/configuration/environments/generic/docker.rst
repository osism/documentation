====================
Docker Configuration
====================

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.docker``
   * - **Repository**
     - https://github.com/osism/ansible-docker
   * - **Documentation**
     - ---

Version
=======

Configuration file: ``environments/configuration.yml``

.. code-block:: yaml

   ##########################
   # versions

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

* :ref:`docker-pin-hold`

Storage driver
==============

Configuration file: ``environments/configuration.yml``

.. code-block:: yaml

   ##########################
   # docker

   docker_configure_storage_driver: yes
   docker_storage_driver: overlay2

.. note::

    * https://docs.docker.com/storage/storagedriver/overlayfs-driver/

    If ``/var/lib/docker`` is on an XFS file system and you want to use the ``overlay2`` storage driver,
    ``d_type`` (``ftype=1``) support must be enabled.

    * https://linuxer.pro/2017/03/what-is-d_type-and-why-docker-overlayfs-need-it/

   .. code-block:: shell

      $ sudo xfs_info /var/lib/docker
      meta-data=/dev/mapper/system-lv_docker isize=512    agcount=4, agsize=1310720 blks
               =                       sectsz=512   attr=2, projid32bit=1
               =                       crc=1        finobt=1 spinodes=0
      data     =                       bsize=4096   blocks=5242880, imaxpct=25
               =                       sunit=0      swidth=0 blks
      naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
      log      =internal               bsize=4096   blocks=2560, version=2
               =                       sectsz=512   sunit=0 blks, lazy-count=1
      realtime =none                   extsz=4096   blocks=0, rtextents=0
