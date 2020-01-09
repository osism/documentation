==============
Infrastructure
==============

.. contents::
   :local:

Network
=======

Jumbo frames
------------

* https://blah.cloud/hardware/test-jumbo-frames-working/

.. code-block:: console

   $ ping -M do -s 8972 -c 3 10.30.50.11
   PING 10.30.50.11 (10.30.50.11) 8972(9000) bytes of data.
   8980 bytes from 10.30.50.11: icmp_seq=1 ttl=64 time=0.255 ms
   8980 bytes from 10.30.50.11: icmp_seq=2 ttl=64 time=0.206 ms
   8980 bytes from 10.30.50.11: icmp_seq=3 ttl=64 time=0.191 ms

   --- 10.30.50.11 ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms
   rtt min/avg/max/mdev = 0.191/0.217/0.255/0.029 ms

Libvirtd
========

.. code-block:: console

   $ docker exec -it nova_libvirt virsh nodeinfo
   CPU model:           x86_64
   CPU(s):              32
   CPU frequency:       800 MHz
   CPU socket(s):       1
   Core(s) per socket:  8
   Thread(s) per core:  2
   NUMA cell(s):        2
   Memory size:         263784260 KiB

.. code-block:: console

   $ docker exec -it nova_libvirt virsh sysinfo
   <sysinfo type='smbios'>
     <bios>
       <entry name='vendor'>American Megatrends Inc.</entry>
       <entry name='version'>2.0b</entry>
       <entry name='date'>02/28/2018</entry>
       <entry name='release'>5.12</entry>
     </bios>
     <system>
       <entry name='manufacturer'>Supermicro</entry>
   [...]

.. code-block:: console

   $ docker exec -it nova_libvirt virsh capabilities
   <capabilities>

     <host>
       <uuid>00000000-0000-0000-0000-ac1f6b09a1de</uuid>
       <cpu>
         <arch>x86_64</arch>
         <model>Skylake-Client-IBRS</model>
         <vendor>Intel</vendor>
   [...]

Memcached
=========

.. code-block:: console

   $ echo stats | nc 10.49.20.10 11211
   STAT pid 7
   STAT uptime 2524
   STAT time 1528967802
   STAT version 1.4.25 Ubuntu
   STAT libevent 2.0.21-stable
   STAT pointer_size 64
   STAT rusage_user 0.044000
   STAT rusage_system 0.088000
   STAT curr_connections 1
   STAT total_connections 2
   STAT connection_structures 2
   STAT reserved_fds 20
   [...]

Open vSwitch
============

.. code-block:: console

   $ docker exec -it openvswitch_vswitchd ovs-vsctl -V
   ovs-vsctl (Open vSwitch) 2.8.1
   DB Schema 7.15.0

On network nodes and compute nodes with provider networks, after the initial start of
the service, a ``br-ex`` exists with the external interfaces.

.. code-block:: console

   $ docker exec -it openvswitch_vswitchd ovs-vsctl show
   a2f9dbad-519e-4873-aea4-0719abcd9e2a
       Bridge br-ex
           Port br-ex
               Interface br-ex
                   type: internal
           Port "enp24s0f1"
               Interface "enp24s0f1"

RabbitMQ
========

* https://www.rabbitmq.com/clustering.html

.. code-block:: console

   dragon@20-10:~$ docker exec -it rabbitmq rabbitmqctl cluster_status
   Cluster status of node 'rabbit@20-10'
   [{nodes,[{disc,['rabbit@20-10','rabbit@20-11','rabbit@20-12']}]},
    {running_nodes,['rabbit@20-12','rabbit@20-11','rabbit@20-10']},
    {cluster_name,<<"rabbit@20-10.betacloud.xyz">>},
    {partitions,[]},
    {alarms,[{'rabbit@20-12',[]},{'rabbit@20-11',[]},{'rabbit@20-10',[]}]}]

Alternatively, log in to the web interface and check the status of the nodes.
The web interface can be accessed via the internal API address
``http://internal-api.betacloud.xyz:15672/``. The username is ``openstack`` and
the password can be found at ``environments/kolla/secrects.yml`` in the variable
``rabbitmq_password``.

.. image:: /images/rabbitmq-nodes.png

MariaDB
=======

* http://galeracluster.com/documentation-webpages/monitoringthecluster.html

Login to the mariadb server (run ``docker exec -it mariadb mysql -u root -p`` on one of the
database nodes or use phpMyAdmin running on the manager node on port ``8110``) and run the following
query.

The password for MariaDB can be found in the file ``environments/kolla/secrets.yml`` in the variable
``database_password``.

.. code-block:: console

   MariaDB [(none)]> SHOW GLOBAL STATUS LIKE 'wsrep_%';
   +------------------------------+----------------------------------------------------+
   | Variable_name                | Value                                              |
   +------------------------------+----------------------------------------------------+
   [...]
   | wsrep_local_state_comment    | Synced                                             |
   | wsrep_incoming_addresses     | 10.49.20.10:3306,10.49.20.11:3306,10.49.20.12:3306 |
   | wsrep_evs_state              | OPERATIONAL                                        |
   | wsrep_cluster_size           | 3                                                  |
   | wsrep_cluster_status         | Primary                                            |
   | wsrep_connected              | ON                                                 |
   | wsrep_ready                  | ON                                                 |
   [...]
   +------------------------------+----------------------------------------------------+

Elasticsearch
=============

* https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html

.. note:: Run this command on the manager node.

.. code-block:: console

   $ curl -s http://10.49.0.100:9200/_cluster/health | python -m json.tool
   {
       "active_primary_shards": 321,
       "active_shards": 642,
       "active_shards_percent_as_number": 100.0,
       "cluster_name": "kolla_logging",
       "delayed_unassigned_shards": 0,
       "initializing_shards": 0,
       "number_of_data_nodes": 3,
       "number_of_in_flight_fetch": 0,
       "number_of_nodes": 3,
       "number_of_pending_tasks": 0,
       "relocating_shards": 0,
       "status": "green",
       "task_max_waiting_in_queue_millis": 0,
       "timed_out": false,
       "unassigned_shards": 0
   }

* ``number_of_data_nodes`` should be the number of available Elasticsearch nodes
* ``status`` should be ``green``
* ``active_shards_percent_as_number`` should be ``100.0``

Fluentd
=======

.. code-block:: console

   $ docker logs fluentd
   [...]
   2018-06-14 08:15:52 +0000 [info]: #0 listening syslog socket on 10.49.10.11:5140 with udp
   [...]
   2018-06-14 08:27:05 +0000 [info]: #0 Connection opened to Elasticsearch cluster => {:host=>"10.49.0.100", :port=>9200, :scheme=>"http"}

Redis
=====

The password for Redis is stored in the ``environments/kolla/secrets.yml`` file
in the ``redis_master_password`` variable. Use the IP address from the internal
network of the control node where Redis is running to connect to Redis.

.. code-block:: console

   $ docker exec -it redis redis-cli -h 10.49.20.10
   10.49.20.10:6379> auth password
   OK
   10.49.20.10:6379> ping
   PONG
   10.49.20.10:6379> info replication
   # Replication
   role:slave
   master_host:10.49.20.10
   master_port:6379
   master_link_status:up
   master_last_io_seconds_ago:0
   master_sync_in_progress:0
   slave_repl_offset:62561
   slave_priority:100
   slave_read_only:1
   connected_slaves:0
   master_replid:899e93628c8c8864efb0b80c9896ab2a9c6b4b4e
   master_replid2:0000000000000000000000000000000000000000
   master_repl_offset:62561
   second_repl_offset:-1
   repl_backlog_active:1
   repl_backlog_size:1048576
   repl_backlog_first_byte_offset:1
   repl_backlog_histlen:62561
