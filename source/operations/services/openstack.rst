=========
OpenStack
=========

Start/Stop all containers of a service
======================================

.. note::

   This script serves as an example. Do not use.

.. code-block:: bash

   #!/usr/bin/env bash                                        

   ACTION=${1:-start}                                         
   SERVICE=${2:-keystone}                                     
   OPENSTACK_RELEASE=pike                                     

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
