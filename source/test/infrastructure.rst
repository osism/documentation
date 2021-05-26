==============
Infrastructure
==============

.. contents::
   :depth: 2

Network
=======

Jumbo frames
------------

* https://blah.cloud/hardware/test-jumbo-frames-working/

.. code-block:: console

   ping -M do -s 8972 -c 3 192.168.70.11
   PING 192.168.70.11 (192.168.70.11) 8972(9000) bytes of data.
   8980 bytes from 192.168.70.11: icmp_seq=1 ttl=64 time=0.255 ms
   8980 bytes from 192.168.70.11: icmp_seq=2 ttl=64 time=0.206 ms
   8980 bytes from 192.168.70.11: icmp_seq=3 ttl=64 time=0.191 ms

   --- 192.168.70.11 ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms
   rtt min/avg/max/mdev = 0.191/0.217/0.255/0.029 ms

Libvirtd
========

.. code-block:: console

   docker exec -it nova_libvirt virsh nodeinfo
   CPU model:           x86_64
   CPU(s):              32
   CPU frequency:       800 MHz
   CPU socket(s):       1
   Core(s) per socket:  8
   Thread(s) per core:  2
   NUMA cell(s):        2
   Memory size:         263784260 KiB

.. code-block:: console

   docker exec -it nova_libvirt virsh sysinfo
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

   docker exec -it nova_libvirt virsh capabilities
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

   echo stats | nc 192.168.50.10 11211
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

   docker exec -it openvswitch_vswitchd ovs-vsctl -V
   ovs-vsctl (Open vSwitch) 2.8.1
   DB Schema 7.15.0

On network nodes and compute nodes with provider networks, after the initial start of
the service, a ``br-ex`` exists with the external interfaces.

.. code-block:: console

   docker exec -it openvswitch_vswitchd ovs-vsctl show
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
* old RabbitMQ

.. code-block:: console

   docker exec -it rabbitmq rabbitmqctl cluster_status
   Cluster status of node 'rabbit@testbed-node-0'
   [{nodes,[{disc,['rabbit@testbed-node-0','rabbit@testbed-node-1']}]},
    {running_nodes,['rabbit@testbed-node-1','rabbit@testbed-node-0']},
    {cluster_name,<<"rabbit@testbed-node-0.osism.local">>},
    {partitions,[]},
    {alarms,[{'rabbit@testbed-node-1',[]},{'rabbit@testbed-node-0',[]}]}]

* new RabbitMQ

.. code-block:: console

   docker exec -it rabbitmq rabbitmqctl cluster_status
   Cluster status of node rabbit@node01 ...
   Basics

   Cluster name: rabbit@node03.osism.local

   Disk Nodes

   rabbit@node01
   rabbit@node02
   rabbit@node03

   Running Nodes

   rabbit@node01
   rabbit@node02
   rabbit@node03

   Versions

   rabbit@node01: RabbitMQ 3.8.16 on Erlang 23.3.3
   rabbit@node02: RabbitMQ 3.8.16 on Erlang 23.3.3
   rabbit@node03: RabbitMQ 3.8.16 on Erlang 23.3.3

   Maintenance status

   Node: rabbit@node01, status: not under maintenance
   Node: rabbit@node02, status: not under maintenance
   Node: rabbit@node03, status: not under maintenance

   Alarms

   (none)

   Network Partitions

   (none)

   Listeners

   Node: rabbit@node01, interface: [::], port: 15672, protocol: http, purpose: HTTP API
   Node: rabbit@node01, interface: [::], port: 15692, protocol: http/prometheus, purpose: Prometheus exporter API over HTTP
   Node: rabbit@node01, interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
   Node: rabbit@node01, interface: 10.2.8.11, port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0
   Node: rabbit@node02, interface: [::], port: 15672, protocol: http, purpose: HTTP API
   Node: rabbit@node02, interface: [::], port: 15692, protocol: http/prometheus, purpose: Prometheus exporter API over HTTP
   Node: rabbit@node02, interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
   Node: rabbit@node02, interface: 10.2.8.12, port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0
   Node: rabbit@node03, interface: [::], port: 15672, protocol: http, purpose: HTTP API
   Node: rabbit@node03, interface: [::], port: 15692, protocol: http/prometheus, purpose: Prometheus exporter API over HTTP
   Node: rabbit@node03, interface: [::], port: 25672, protocol: clustering, purpose: inter-node and CLI tool communication
   Node: rabbit@node03, interface: 10.2.8.13, port: 5672, protocol: amqp, purpose: AMQP 0-9-1 and AMQP 1.0

   Feature flags

   Flag: drop_unroutable_metric, state: enabled
   Flag: empty_basic_get_metric, state: enabled
   Flag: implicit_default_bindings, state: enabled
   Flag: maintenance_mode_status, state: enabled
   Flag: quorum_queue, state: enabled
   Flag: user_limits, state: enabled
   Flag: virtual_host_metadata, state: enabled

Alternatively, log in to the web interface and check the status of the nodes.
The web interface can be accessed via the internal API address
``http://api-int.osism.local:15672/``. The username is ``openstack`` and
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

   docker exec -it mariadb mysql -u root -p
   Enter password: qNpdZmkKuUKBK3D5nZ08KMZ5MnYrGEe2hzH6XC0i
   Welcome to the MariaDB monitor.  Commands end with ; or \g.
   Your MariaDB connection id is 10324
   Server version: 10.1.43-MariaDB-0ubuntu0.18.04.1 Ubuntu 18.04

   Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

   Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

   MariaDB [(none)]> SHOW GLOBAL STATUS LIKE 'wsrep_%';
   +------------------------------+---------------------------------------+
   | Variable_name                | Value                                 |
   +------------------------------+---------------------------------------+
   [...]
   | wsrep_local_state_comment    | Synced                                |
   | wsrep_incoming_addresses     | 192.168.50.11:3306,192.168.50.10:3306 |
   | wsrep_evs_state              | OPERATIONAL                           |
   | wsrep_cluster_size           | 2                                     |
   | wsrep_cluster_status         | Primary                               |
   | wsrep_connected              | ON                                    |
   | wsrep_ready                  | ON                                    |
   [...]
   +------------------------------+---------------------------------------+

Elasticsearch
=============

* https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html

.. note:: Run this command on the manager node.

.. code-block:: console

   curl -s http://api-int.osism.local:9200/_cluster/health | python -m json.tool
   {
       "active_primary_shards": 75,
       "active_shards": 150,
       "active_shards_percent_as_number": 100.0,
       "cluster_name": "kolla_logging",
       "delayed_unassigned_shards": 0,
       "initializing_shards": 0,
       "number_of_data_nodes": 2,
       "number_of_in_flight_fetch": 0,
       "number_of_nodes": 2,
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

   docker logs fluentd
   [...]
   2020-01-25 15:26:07 +0000 [info]: #0 listening syslog socket on 192.168.50.10:5140 with udp
   [...]

.. _testinfrastructureredis:

Redis
=====

The password for Redis is stored in the ``environments/kolla/secrets.yml`` file
in the ``redis_master_password`` variable. Use the IP address from the internal
network of the control node where Redis is running to connect to Redis.

.. code-block:: console

   docker exec -it redis redis-cli -h testbed-node-0
   testbed-node-0:6379> auth QHNA1SZRlOKzLADhUd5ZDgpHfQe6dNfr3bwEdY24
   OK
   testbed-node-0:6379> ping
   PONG
   testbed-node-0:6379> info replication
   # Replication
   role:master
   connected_slaves:1
   slave0:ip=192.168.50.11,port=6379,state=online,offset=101675,lag=0
   master_replid:346a919c213428671d3295b02585494591c6fa4a
   master_replid2:0000000000000000000000000000000000000000
   master_repl_offset:101675
   second_repl_offset:-1
   repl_backlog_active:1
   repl_backlog_size:1048576
   repl_backlog_first_byte_offset:1
   repl_backlog_histlen:101675

.. code-block:: console

   nc testbed-node-0 6379
   auth QHNA1SZRlOKzLADhUd5ZDgpHfQe6dNfr3bwEdY24
   +OK
   ping
   +PONG
   info replication
   $392
   # Replication
   role:master
   connected_slaves:1
   slave0:ip=192.168.50.11,port=6379,state=online,offset=234561,lag=0
   master_replid:edf4914fb012c616077ad198919dbfba0ffd08e7
   master_replid2:0000000000000000000000000000000000000000
   master_repl_offset:234561
   second_repl_offset:-1
   repl_backlog_active:1
   repl_backlog_size:1048576
   repl_backlog_first_byte_offset:1
   repl_backlog_histlen:234561

Etcd
====

.. code-block:: console

   docker exec -it etcd etcdctl --endpoints http://testbed-node-0:2379  cluster-health
   member ac5b67ea9df5c86e is healthy: got healthy result from http://192.168.50.11:2379
   member f4befbb7afd08dda is healthy: got healthy result from http://192.168.50.10:2379
   cluster is healthy
