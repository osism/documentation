=========
OpenStack
=========

Cleanup neutron-ns-metadata-proxy logfiles
==========================================

* check number of logfiles on network node

.. code-block:: console

   $ docker exec -it kolla_toolbox bash
   (kolla-toolbox)[ansible@30-10 /] $ ls -1 /var/log/kolla/neutron/neutron-ns-metadata-proxy-* | wc -l
   10638

* remove all log files for which there are no running processes

.. code-block:: shell

   #!/usr/bin/env bash

   tmpfile=$(mktemp)

   pgrep -af "haproxy -f /var/lib/neutron/ns-metadata-proxy"| while read process; do
       tmp=${process##*/}
       uuid=${tmp%.conf}
       echo $uuid >> $tmpfile
   done

   docker exec -t neutron_openvswitch_agent ls -1 /var/log/kolla/neutron/ | grep ns-metadata-proxy | while read logfile; do
       tmp=${logfile#*neutron-ns-metadata-proxy-}
       uuid=${tmp%.log*}

       if ! grep -Fxq "$uuid" $tmpfile; then
           docker exec -t neutron_openvswitch_agent rm /var/log/kolla/neutron/neutron-ns-metadata-proxy-$uuid.log
       fi
   done

   rm $tmpfile

* recheck number of logfiles on network node

.. code-block:: console

   $ docker exec -it kolla_toolbox bash
   (kolla-toolbox)[ansible@30-10 /] $ ls -1 /var/log/kolla/neutron/neutron-ns-metadata-proxy-* | wc -l
   29

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
