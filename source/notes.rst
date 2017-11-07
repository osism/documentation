=====
Notes
=====

Reboot a system
===============

.. note:: Run this command on the manager node.

.. code-block:: shell

   $ osism-generic reboot --limit 20-12.betacloud.xyz

   PLAY [Reboot systems] **********************************************************

   TASK [Reboot system] ***********************************************************
   changed: [20-12.betacloud.xyz]

   PLAY RECAP *********************************************************************
   20-12.betacloud.xyz        : ok=1    changed=1    unreachable=0    failed=0

Update facts
============

.. note:: Run this command on the manager node.

.. code-block:: shell

   $ osism-generic facts

   PLAY [Gather facts for all hosts] **********************************************

   TASK [setup] *******************************************************************
   ok: [20-11.betacloud.xyz]
   ok: [20-10.betacloud.xyz]
   ok: [50-10.betacloud.xyz]
   ok: [50-11.betacloud.xyz]
   ok: [50-12.betacloud.xyz]
   ok: [10-11.betacloud.xyz]
   ok: [30-10.betacloud.xyz]
   ok: [20-12.betacloud.xyz]
   ok: [30-11.betacloud.xyz]

   PLAY [Gather facts for all hosts (if using --limit)] ***************************

   TASK [setup] *******************************************************************
   skipping: [30-11.betacloud.xyz] => (item=20-11.betacloud.xyz)
   skipping: [30-11.betacloud.xyz] => (item=20-10.betacloud.xyz)
   [...]

   PLAY RECAP *********************************************************************
   10-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   20-10.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   20-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   20-12.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   30-10.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   30-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   50-10.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   50-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   50-12.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0

Update configuration
====================

There are two possibilities to update the configuration repository on the manager node.

On the seed node change into the manager environment and use the following command. This will update the configuration repository on the manager node.

.. code-block:: shell

   $ ./run.sh configuration

On the manager node use the following command to update the configuration repository.

.. code-block:: shell

   $ osism-generic configuration

Generate self-signed certificates
=================================

.. note:: Run this command on the manager node.

.. note:: ``10-11.betacloud.xyz`` is the manager node.

.. code-block:: shell

   $ osism-kolla _ certificates --limit 10-11.betacloud.xyz
   PLAY [Apply role certificates] *************************************************

   TASK [certificates : Ensuring config directories exist] ************************
   ok: [10-11.betacloud.xyz] => (item=certificates/private)

   TASK [certificates : Creating SSL configuration file] **************************
   ok: [10-11.betacloud.xyz] => (item=openssl-kolla.cnf)

   TASK [certificates : Creating Key] *********************************************
   ok: [10-11.betacloud.xyz] => (item=/etc/kolla//certificates/private/haproxy.key)

   TASK [certificates : Creating Server Certificate] ******************************
   ok: [10-11.betacloud.xyz] => (item=/etc/kolla//certificates/private/haproxy.crt)

   TASK [certificates : Creating CA Certificate File] *****************************
   ok: [10-11.betacloud.xyz]

   TASK [certificates : Creating Server PEM File] *********************************
   ok: [10-11.betacloud.xyz]

   PLAY RECAP *********************************************************************
   10-11.betacloud.xyz        : ok=6    changed=0    unreachable=0    failed=0

On the manager node the self-signed certificate is located in ``/etc/kolla/certificates/haproxy.pem``.

Set ``kolla_enable_tls_external: "yes"`` in ``environments/kolla/configuration.yml`` and add the
content of the self-signed certificate to the ``kolla_external_fqdn_cert`` parameter in the
``environments/kolla/secrets.yml`` file.

Check MariaDB Galera cluster
============================

* http://galeracluster.com/documentation-webpages/monitoringthecluster.html

Login to the mariadb databaserver (run ``docker exec -it mariadb mysqlu -u root -p`` on one of the
database nodes or use phpMyAdmin running on the manager node on port ``8110``) and run the following
query.

.. code-block:: shell

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
