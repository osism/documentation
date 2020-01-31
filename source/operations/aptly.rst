=====
Aptly
=====

.. contents::
   :local:

Manual usage
============

This have to be done for the following repositories.

* docker https://download.docker.com/linux/ubuntu/ bionic stable
* bionic http://de.archive.ubuntu.com/ubuntu/ bionic main
* bionic-backports http://de.archive.ubuntu.com/ubuntu/ bionic-backports main
* bionic-security http://de.archive.ubuntu.com/ubuntu/ bionic-security main
* bionic-updates http://de.archive.ubuntu.com/ubuntu/ bionic-updates main

The manual use of Aptly is described below using the example of the Docker repository.

Execute the subsequent commands within the Aptly container on the mirror system.

.. code-block:: console

   $ docker exec -it aptly_aptly_1 bash

Import GPG key
--------------

.. code-block:: console

   # wget -O - https://download.docker.com/linux/ubuntu/gpg | gpg --no-default-keyring --keyring trustedkeys.gpg --import

Add repository
--------------

.. code-block:: console

   # aptly mirror create -architectures=amd64 bionic-docker https://download.docker.com/linux/ubuntu bionic stable

.. code-block:: console

   # aptly mirror list
   List of mirrors:
    * [bionic-docker]: https://download.docker.com/linux/ubuntu/ bionic

   To get more information about mirror, run `aptly mirror show <name>`.

Update repository
-----------------

.. code-block:: console

   # aptly mirror update -force=true -skip-existing-packages -max-tries=3 bionic-docker

Create snapshot
---------------

.. code-block:: console

   # aptly snapshot create bionic-docker-YYYYMMDD from mirror bionic-docker

Publish snapshot
----------------

.. code-block:: console

   # aptly publish snapshot -passphrase=$GPG_PASSWORD -batch=true -distribution=bionic-docker bionic-docker-YYYYMMDD ubuntu

If this takes too long, you can use the `-skip-contents` parameter.

Switch snapshot
---------------

.. code-block:: console

   # aptly publish switch -passphrase=$GPG_PASSWORD -batch=true bionic-docker ubuntu bionic-docker-YYYYMMDD

If this takes too long, you can use the `-skip-contents` parameter.

Copy GPG key
------------

.. code-block:: console

   # cp /opt/aptly/aptly.pub /opt/aptly/public/aptly.pub
