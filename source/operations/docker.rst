======
Docker
======

.. contents::
   :local:

Start / Stop all containers
===========================

When using the live restore (https://docs.docker.com/engine/admin/live-restore/) feature, not all
containers will be stopped when the docker service is stopped.

.. code-block:: console

   $ docker stop $(docker ps -q)

.. code-block:: console

   $ docker start $(docker ps -a -q)

Make sure that any containers intentionally stopped on the system are also started. This can lead to
unintended side effects. Therefore, in many cases it is better to save the output of
``docker ps -q`` before the stop and, based on this, start the containers later.

Start / Stop all containers of a service
========================================

.. code-block:: bash

   #!/usr/bin/env bash

   ACTION=${1:-start}
   SERVICE=${2:-keystone}
   OPENSTACK_RELEASE=queens

   case $ACTION in
     start)
       for container in $(docker ps -a | grep osism/$SERVICE | grep $OPENSTACK_RELEASE | grep Exited | awk '{ print $1 }'); do
         docker start $container
         sleep 1
       done
     ;;

     stop)
       for container in $(docker ps -a | grep osism/$SERVICE | grep $OPENSTACK_RELEASE | grep -v Exited | awk '{ print $1 }'); do
         docker stop $container
         sleep 1
       done
     ;;
   esac

Move /var/lib/docker to a block device
======================================

.. code-block:: yaml

   ##########################################################
   # docker

   docker_configure_storage_block_device: yes
   docker_storage_block_device: /dev/vdb
   docker_storage_filesystem: ext4

.. code-block:: console

   $ sudo mkfs.ext4 /dev/vdb
   $ echo "/dev/vdb /var/lib/docker ext4 defaults 0 0" | sudo tee -a /etc/fstab

.. code-block:: console

   $ docker ps -q > running.YYYYMMDD
   $ docker stop $(cat running.YYYYMMDD)
   $ sudo systemctl stop docker

.. code-block:: console

   $ sudo mv /var/lib/docker /var/lib/docker.YYYYMMDD
   $ sudo mkdir /var/lib/docker
   $ sudo mount /var/lib/docker
   $ sudo rsync -avz /var/lib/docker.YYYYMMDD/ /var/lib/docker/

.. code-block:: console

   $ sudo systemctl start docker
   $ docker start $(cat running.YYYYMMDD)
   $ rm running.YYYYMMDD
   $ sudo rm -rf /var/lib/docker.YYYYMMDD

unable to find user X: no matching entries in passwd file
=========================================================

- https://stackoverflow.com/questions/41636759/unable-to-find-user-root-no-matching-entries-in-passwd-file/41963861

.. code-block:: console

   $ docker exec -it kolla_toolbox bash
   unable to find user ansible: no matching entries in passwd file
   $ docker exec -it -u 0 kolla_toolbox bash
   (kolla-toolbox)[root@hostname /]#

.. code-block:: console

   $ docker stop CONTAINER
   $ docker start CONTAINER
   $ docker exec -it kolla_toolbox bash
   (kolla-toolbox)[root@hostname /]#

Do not use ``restart``. ``restart`` will not solve the issue.

Cleanup
=======

.. warning::

   Never use ``docker system prune`` on any of the nodes to free storage. This removes stopped containers.

Images that are no longer needed can be removed at any time to release storage.

.. code-block:: console

   $ docker image prune --all
   WARNING! This will remove all images without at least one container associated to them.
   Are you sure you want to continue? [y/N] y
   Deleted Images:
   untagged: osism/openvswitch-vswitchd:pike-20180807-0
   untagged: osism/keepalived:pike-latest
   untagged: osism/keepalived@sha256:59b611a3a84060f38b97dbbd68ab51a52c503a81309ed86c46a92fd0227b09e1

   [...]
   Total reclaimed space: 9.681GB

This can also be done on all systems by Ansible (included since 2020.01).

.. code-block:: console

   $ osism-generic cleanup-docker-images
