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

   # aptly mirror create -architectures=amd64 docker https://download.docker.com/linux/ubuntu xenial stable
   # aptly mirror create -architectures=amd64 xenial http://de.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse
   # aptly mirror create -architectures=amd64 xenial-backports http://de.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse
   # aptly mirror create -architectures=amd64 xenial-security http://de.archive.ubuntu.com/ubuntu/ xenial-security main restricted universe multiverse
   # aptly mirror create -architectures=amd64 xenial-updates http://de.archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse

.. code-block:: shell

   # aptly mirror list
   List of mirrors:
    * [docker]: https://download.docker.com/linux/ubuntu/ xenial
    * [xenial-backports]: http://de.archive.ubuntu.com/ubuntu/ xenial-backports
    * [xenial-security]: http://de.archive.ubuntu.com/ubuntu/ xenial-security
    * [xenial-updates]: http://de.archive.ubuntu.com/ubuntu/ xenial-updates
    * [xenial]: http://de.archive.ubuntu.com/ubuntu/ xenial

   To get more information about mirror, run `aptly mirror show <name>`.

Update repositories
===================

.. code-block:: shell

   # aptly mirror update -force=true -skip-existing-packages -max-tries=3 docker
   # aptly mirror update -force=true -skip-existing-packages -max-tries=3 xenial-backports
   # aptly mirror update -force=true -skip-existing-packages -max-tries=3 xenial-security
   # aptly mirror update -force=true -skip-existing-packages -max-tries=3 xenial-updates
   # aptly mirror update -force=true -skip-existing-packages -max-tries=3 xenial

Create snapshots
================

.. code-block:: shell

   # aptly snapshot create docker-YYYYMMDD from mirror docker
   # aptly snapshot create xenial-backports-YYYYMMDD from mirror xenial-backports
   # aptly snapshot create xenial-security-YYYYMMDD from mirror xenial-security
   # aptly snapshot create xenial-updates-YYYYMMDD from mirror xenial-updates
   # aptly snapshot create xenial-YYYYMMDD from mirror xenial

Merge snapshots
===============

.. code-block:: shell

   # aptly snapshot merge -no-remove node-YYYYMMDD \
     docker-YYYYMMDD \
     xenial-backports-YYYYMMDD \
     xenial-security-YYYYMMDD \
     xenial-updates-YYYYMMDD \
     xenial-YYYYMMDD

   Snapshot node-YYYYMMDD successfully created.
   You can run 'aptly publish snapshot node-YYYYMMDD' to publish snapshot as Debian repository.

Publish snapshot
================

.. code-block:: shell

   # aptly publish snapshot -distribution xenial node-YYYYMMDD node-YYYYMMDD
