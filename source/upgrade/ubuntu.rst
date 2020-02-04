======
Ubuntu
======

.. contents::
   :local:

Xenial -> Bionic
================

Preparations
------------

* aptly - see :ref:`aptlyhandling`
* or online repositories
* disable netplan

.. code-block:: console

   # vim /etc/default/grub
   ...
   GRUB_CMDLINE_LINUX="netcfg/do_not_use_netplan=true"
   # update-grub

* the following MACs entry should be in ``/etc/ssh/sshd_config``, delete the other entries

.. code-block:: console

   # V-72253
   MACs hmac-sha2-256,hmac-sha2-512

* look in systemd service unit files for something like and change it

.. code-block:: console

   $(command -v mkdir) => /bin/mkdir

Upgrade
-------

* add the following to ``environments/configuration.yml`` for online repositories

.. code-block:: console

   repositories:
     - name: docker
       repository: "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
     - name: "bionic"
       repository: "deb [arch=amd64] http://de.archive.ubuntu.com/ubuntu/ bionic main restricted universe multiverse"
     - name: "bionic-backports"
       repository: "deb [arch=amd64] http://de.archive.ubuntu.com/ubuntu/ bionic-backports main restricted universe multiverse"
     - name: "bionic-security"
       repository: "deb [arch=amd64] http://de.archive.ubuntu.com/ubuntu/ bionic-security main restricted universe multiverse"
     - name: "bionic-updates"
       repository: "deb [arch=amd64] http://de.archive.ubuntu.com/ubuntu/ bionic-updates main restricted universe multiverse"

* add the following to ``environments/configuration.yml`` for local aptly repositories

.. code-block:: console

   repositories:
     - name: "node"
       repository: "deb [arch=amd64] http://repository.betacloud.xyz:8080/node-2020-01-31 bionic main"

* roll out the new repositories, upgrade and reboot

.. code-block:: console

   # osism-generic repository (-l 20-10.betacloud.xyz)
   # osism-generic upgrade-packages (-l 20-10.betacloud.xyz)
   # osism-generic check-reboot (-l 20-10.betacloud.xyz)
   # osism-generic reboot (-l 20-10.betacloud.xyz)

