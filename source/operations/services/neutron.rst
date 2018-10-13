=======
Neutron
=======

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
