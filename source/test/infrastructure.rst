==============
Infrastructure
==============

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

Alternatively, log in to the web interface and check the status of the nodes there.

.. image:: /images/rabbitmq-nodes.png

MariaDB
=======

* http://galeracluster.com/documentation-webpages/monitoringthecluster.html

Login to the mariadb databaserver (run ``docker exec -it mariadb mysql -u root -p`` on one of the
database nodes or use phpMyAdmin running on the manager node on port ``8110``) and run the following
query.

.. code-block:: console

   MariaDB [(none)]> SHOW GLOBAL STATUS LIKE 'wsrep_%';
   +------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
   | Variable_name                | Value                                                                                                                       |
   +------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
   | wsrep_local_state_uuid       | cbea24b0-c30d-11e7-8c66-4610c364bc83                                                                                        |
   | wsrep_protocol_version       | 7                                                                                                                           |
   | wsrep_last_committed         | 1206                                                                                                                        |
   | wsrep_replicated             | 1                                                                                                                           |
   | wsrep_replicated_bytes       | 452                                                                                                                         |
   | wsrep_repl_keys              | 2                                                                                                                           |
   | wsrep_repl_keys_bytes        | 39                                                                                                                          |
   | wsrep_repl_data_bytes        | 349                                                                                                                         |
   | wsrep_repl_other_bytes       | 0                                                                                                                           |
   | wsrep_received               | 7                                                                                                                           |
   | wsrep_received_bytes         | 1220                                                                                                                        |
   | wsrep_local_commits          | 0                                                                                                                           |
   | wsrep_local_cert_failures    | 0                                                                                                                           |
   | wsrep_local_replays          | 0                                                                                                                           |
   | wsrep_local_send_queue       | 0                                                                                                                           |
   | wsrep_local_send_queue_max   | 2                                                                                                                           |
   | wsrep_local_send_queue_min   | 0                                                                                                                           |
   | wsrep_local_send_queue_avg   | 0.250000                                                                                                                    |
   | wsrep_local_recv_queue       | 0                                                                                                                           |
   | wsrep_local_recv_queue_max   | 1                                                                                                                           |
   | wsrep_local_recv_queue_min   | 0                                                                                                                           |
   | wsrep_local_recv_queue_avg   | 0.000000                                                                                                                    |
   | wsrep_local_cached_downto    | 1206                                                                                                                        |
   | wsrep_flow_control_paused_ns | 0                                                                                                                           |
   | wsrep_flow_control_paused    | 0.000000                                                                                                                    |
   | wsrep_flow_control_sent      | 0                                                                                                                           |
   | wsrep_flow_control_recv      | 0                                                                                                                           |
   | wsrep_cert_deps_distance     | 1.000000                                                                                                                    |
   | wsrep_apply_oooe             | 0.200000                                                                                                                    |
   | wsrep_apply_oool             | 0.000000                                                                                                                    |
   | wsrep_apply_window           | 3.080000                                                                                                                    |
   | wsrep_commit_oooe            | 0.000000                                                                                                                    |
   | wsrep_commit_oool            | 0.000000                                                                                                                    |
   | wsrep_commit_window          | 1.760000                                                                                                                    |
   | wsrep_local_state            | 4                                                                                                                           |
   | wsrep_local_state_comment    | Synced                                                                                                                      |
   | wsrep_cert_index_size        | 2                                                                                                                           |
   | wsrep_causal_reads           | 0                                                                                                                           |
   | wsrep_cert_interval          | 0.000000                                                                                                                    |
   | wsrep_incoming_addresses     | 10.49.20.11:3306,10.49.20.10:3306,10.49.20.12:3306                                                                          |
   | wsrep_desync_count           | 0                                                                                                                           |
   | wsrep_evs_delayed            | dd51fef5-c30d-11e7-a68b-0e08fa503a3b:tcp://10.49.20.11:4567:1,e6249c55-c30d-11e7-a09a-9643934a39d2:tcp://10.49.20.12:4567:1 |
   | wsrep_evs_evict_list         |                                                                                                                             |
   | wsrep_evs_repl_latency       | 0/0/0/0/0                                                                                                                   |
   | wsrep_evs_state              | OPERATIONAL                                                                                                                 |
   | wsrep_gcomm_uuid             | ae9125e1-c34a-11e7-841c-d70befaca075                                                                                        |
   | wsrep_cluster_conf_id        | 6                                                                                                                           |
   | wsrep_cluster_size           | 3                                                                                                                           |
   | wsrep_cluster_state_uuid     | cbea24b0-c30d-11e7-8c66-4610c364bc83                                                                                        |
   | wsrep_cluster_status         | Primary                                                                                                                     |
   | wsrep_connected              | ON                                                                                                                          |
   | wsrep_local_bf_aborts        | 0                                                                                                                           |
   | wsrep_local_index            | 1                                                                                                                           |
   | wsrep_provider_name          | Galera                                                                                                                      |
   | wsrep_provider_vendor        | Codership Oy <info@codership.com>                                                                                           |
   | wsrep_provider_version       | 25.3.20(r3703)                                                                                                              |
   | wsrep_ready                  | ON                                                                                                                          |
   | wsrep_thread_count           | 5                                                                                                                           |
   +------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
   58 rows in set (0.00 sec)
