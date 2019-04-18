=====
Aptly
=====

.. note::

   Execute the subsequent commands within the aptly container on the mirror system.

   $ docker exec -it aptly_aptly_1 bash

Import GPG keys
===============

.. code-block:: shell

   # wget -O - https://download.docker.com/linux/ubuntu/gpg | gpg --no-default-keyring --keyring trustedkeys.gpg --import

Add repositories
================

.. code-block:: shell

   # aptly mirror create -architectures=amd64 bionic-docker https://download.docker.com/linux/ubuntu bionic stable
   # aptly mirror create -architectures=amd64 bionic http://de.archive.ubuntu.com/ubuntu/ bionic main restricted universe multiverse
   # aptly mirror create -architectures=amd64 bionic-backports http://de.archive.ubuntu.com/ubuntu/ bionic-backports main restricted universe multiverse
   # aptly mirror create -architectures=amd64 bionic-security http://de.archive.ubuntu.com/ubuntu/ bionic-security main restricted universe multiverse
   # aptly mirror create -architectures=amd64 bionic-updates http://de.archive.ubuntu.com/ubuntu/ bionic-updates main restricted universe multiverse

.. code-block:: shell

   # aptly mirror list
   List of mirrors:
    * [bionic-docker]: https://download.docker.com/linux/ubuntu/ bionic
    * [bionic-backports]: http://de.archive.ubuntu.com/ubuntu/ bionic-backports
    * [bionic-security]: http://de.archive.ubuntu.com/ubuntu/ bionic-security
    * [bionic-updates]: http://de.archive.ubuntu.com/ubuntu/ bionic-updates
    * [bionic]: http://de.archive.ubuntu.com/ubuntu/ bionic

   To get more information about mirror, run `aptly mirror show <name>`.

Update repositories
===================

.. code-block:: shell

   # aptly mirror update -force=true -skip-existing-packages -max-tries=3 bionic-docker
   # aptly mirror update -force=true -skip-existing-packages -max-tries=3 bionic-backports
   # aptly mirror update -force=true -skip-existing-packages -max-tries=3 bionic-security
   # aptly mirror update -force=true -skip-existing-packages -max-tries=3 bionic-updates
   # aptly mirror update -force=true -skip-existing-packages -max-tries=3 bionic

Create snapshots
================

.. code-block:: shell

   # aptly snapshot create bionic-docker-YYYYMMDD from mirror bionic-docker
   # aptly snapshot create bionic-backports-YYYYMMDD from mirror bionic-backports
   # aptly snapshot create bionic-security-YYYYMMDD from mirror bionic-security
   # aptly snapshot create bionic-updates-YYYYMMDD from mirror bionic-updates
   # aptly snapshot create bionic-YYYYMMDD from mirror bionic

Publish snapshots
=================

.. code-block:: shell

   # aptly publish snapshot -distribution bionic-docker bionic-docker-YYYYMMDD ubuntu
   # aptly publish snapshot -distribution bionic-backports bionic-backports-YYYYMMDD ubuntu
   # aptly publish snapshot -distribution bionic-security bionic-security-YYYYMMDD ubuntu
   # aptly publish snapshot -distribution bionic-updates bionic-updates-YYYYMMDD ubuntu
   # aptly publish snapshot -distribution bionic bionic-YYYYMMDD ubuntu

If this takes too long, you can use the `-skip-contents` parameter.

Switch snapshots
================

If you have updated your repository and want to publish a new snapshot, this will result
in an error.

.. code-block:: shell

   'some package' already used by another published repo.

You have to switch the published snapshot instead.

.. code-block:: shell

   # aptly publish snapshot bionic-docker ubuntu bionic-docker-YYYYMMDD
   # aptly publish snapshot bionic-backports ubuntu bionic-backports-YYYYMMDD
   # aptly publish snapshot bionic-security ubuntu bionic-security-YYYYMMDD
   # aptly publish snapshot bionic-updates ubuntu bionic-updates-YYYYMMDD
   # aptly publish snapshot bionic ubuntu bionic-YYYYMMDD

If this takes too long, you can use the `-skip-contents` parameter.
