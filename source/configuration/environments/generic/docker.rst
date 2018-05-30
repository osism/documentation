======
Docker
======

* role: ``osism.docker`` (https://github.com/osism/ansible-docker)

Version
=======

* ``environments/generic/configuration.yml`` & ``environments/manager/configuration.yml``

  .. code-block:: yaml

     ##########################
     # versions

     docker_version: 17.12.0

Storage driver
==============

* ``environments/configuration.yml``

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
