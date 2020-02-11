=======
MariaDB
=======

.. contents::
   :local:

Cluster start and stop
======================

http://galeracluster.com/documentation-webpages/restartingcluster.html

Stop
----

Ensure that any services using MariaDB are stopped.

Carry out the following steps on all controller nodes (one by one).

1. Ensure that ``wsrep_local_state_comment`` is ``synced``

   The password for MariaDB can be found in the file ``environments/kolla/secrets.yml`` in
   the variable ``database_password``.

   .. code-block:: console

      $ docker exec -it mariadb mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_local_state_comment'"
      Enter password: qNpdZmkKuUKBK3D5nZ08KMZ5MnYrGEe2hzH6XC0i
      +---------------------------+--------+
      | Variable_name             | Value  |
      +---------------------------+--------+
      | wsrep_local_state_comment | Synced |
      +---------------------------+--------+

2. Stop the ``mariadb`` container

   .. code-block:: console

      $ docker stop mariadb

Start
-----

On the manager node run the recovery process.

.. code-block:: console

   $ osism-kolla deploy mariadb_recovery

Check
-----

.. code-block:: console

   $ docker exec -it mariadb mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_%'"
   Enter password: qNpdZmkKuUKBK3D5nZ08KMZ5MnYrGEe2hzH6XC0i
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

Cluster recovery
================

http://galeracluster.com/2016/11/introducing-the-safe-to-bootstrap-feature-in-galera-cluster/

On the controller nodes stop the ``mariadb`` containers.

.. code-block:: console

   $ docker stop mariadb

On the manager node run the recovery process.

.. code-block:: console

   $ osism-kolla deploy mariadb_recovery

If this does not work check the grastate.dat file on all controller nodes.

.. code-block:: console

   $ docker cp mariadb:/var/lib/mysql/grastate.dat /tmp/kolla_mariadb_grastate.dat
   $ cat /tmp/kolla_mariadb_grastate.dat
   # GALERA saved state
   version: 2.1
   uuid:    5ae8bce5-5ccd-4f8b-b56f-cfa601e7060e
   seqno:   -1
   safe_to_bootstrap: 0

If seqno is -1 and safe_to_bootstrap is 0 on all nodes you have to overwrite this file on one of the nodes. Set safe_to_bootstrap to 1 and copy the file into the data volume.

.. code-block:: console

   $ docker cp /tmp/kolla_mariadb_grastate.dat mariadb:/var/lib/mysql/grastate.dat

Cleanup and run the playbook again.

.. code-block:: console

   $ rm /tmp/kolla_mariadb_grastate.dat

[ERROR] Found 1 prepared transactions!
======================================

https://bugzilla.redhat.com/show_bug.cgi?id=1195226

Description
-----------

.. code-block:: console

   2016-06-01 00:25:35 7f72f56147c0  InnoDB: Starting recovery for XA transactions...
   2016-06-01 00:25:35 7f72f56147c0  InnoDB: Transaction 44054 in prepared state after recovery
   2016-06-01 00:25:35 7f72f56147c0  InnoDB: Transaction contains changes to 1 rows
   2016-06-01 00:25:35 7f72f56147c0  InnoDB: 1 transactions in prepared state after recovery
   160601  0:25:35 [Note] Found 1 prepared transaction(s) in InnoDB
   160601  0:25:35 [ERROR] Found 1 prepared transactions! It means that mysqld was not shut down properly last time and critical recovery information (last binlog or tc.log file) was manually deleted after a crash. You have to start mysqld with --tc-heuristic-recover switch to commit or rollback pending transactions.
   160601  0:25:35 [ERROR] Aborting
   160601  0:25:35 [Note] InnoDB: FTS optimize thread exiting.
   160601  0:25:35 [Note] InnoDB: Starting shutdown...
   160601  0:25:37 [Note] InnoDB: Shutdown completed; log sequence number 20410674
   160601  0:25:37 [Note] /usr/sbin/mysqld: Shutdown complete'

Notes
-----

* A restart of the mariadb container is not working, it will result in the same issue.
* Run a manual backup of the mariadb volume, located at ``/var/lib/docker/volumes/mariadb``.

Solution
--------

To solve this issue first ensure that the mariadb container is stopped.

Now start an temporary mariadb container and attach the volumes of the stopped mariadb container. The used image has to be checked, check the value of the attribute ``Image`` in the output of ``docker inspect mariadb``.

.. code::

   $ docker run --volumes-from mariadb -it osism/mariadb:rocky-latest /bin/bash

Inside the container run the command ``mysqld --tc-heuristic-recover=ROLLBACK`` to rollback the transactions.

.. code::

   ()[mysql@2eda39396d4a /]$ mysqld --tc-heuristic-recover=ROLLBACK
   160601  8:55:15 [Note] mysqld (mysqld 10.0.25-MariaDB-1~trusty-wsrep) starting as process 13 ...
   160601  8:55:15 [Note] InnoDB: Using mutexes to ref count buffer pool pages
   160601  8:55:15 [Note] InnoDB: The InnoDB memory heap is disabled
   160601  8:55:15 [Note] InnoDB: Mutexes and rw_locks use GCC atomic builtins
   160601  8:55:15 [Note] InnoDB: Memory barrier is not used
   160601  8:55:15 [Note] InnoDB: Compressed tables use zlib 1.2.8
   160601  8:55:15 [Note] InnoDB: Using Linux native AIO
   160601  8:55:15 [Note] InnoDB: Using CPU crc32 instructions
   160601  8:55:15 [Note] InnoDB: Initializing buffer pool, size = 256.0M
   160601  8:55:15 [Note] InnoDB: Completed initialization of buffer pool
   160601  8:55:15 [Note] InnoDB: Highest supported file format is Barracuda.
   InnoDB: Transaction 44054 was in the XA prepared state.
   InnoDB: 1 transaction(s) which must be rolled back or cleaned up
   InnoDB: in total 0 row operations to undo
   InnoDB: Trx id counter is 57856
   160601  8:55:16 [Note] InnoDB: 128 rollback segment(s) are active.
   InnoDB: Starting in background the rollback of uncommitted transactions
   2016-06-01 08:55:16 7f4a77fff700  InnoDB: Rollback of non-prepared transactions completed
   160601  8:55:16 [Note] InnoDB: Waiting for purge to start
   160601  8:55:16 [Note] InnoDB:  Percona XtraDB (http://www.percona.com) 5.6.29-76.2 started; log sequence number 20410684
   160601  8:55:16 [Note] Plugin 'FEEDBACK' is disabled.
   160601  8:55:16 [Note] Heuristic crash recovery mode
   2016-06-01 08:55:16 7f4aaac117c0  InnoDB: Starting recovery for XA transactions...
   2016-06-01 08:55:16 7f4aaac117c0  InnoDB: Transaction 44054 in prepared state after recovery
   2016-06-01 08:55:16 7f4aaac117c0  InnoDB: Transaction contains changes to 1 rows
   2016-06-01 08:55:16 7f4aaac117c0  InnoDB: 1 transactions in prepared state after recovery
   160601  8:55:16 [Note] Found 1 prepared transaction(s) in InnoDB
   160601  8:55:16 [Note] Please restart mysqld without --tc-heuristic-recover
   160601  8:55:16 [ERROR] Can't init tc log
   160601  8:55:16 [ERROR] Aborting
   160601  8:55:16 [Note] InnoDB: FTS optimize thread exiting.
   160601  8:55:16 [Note] InnoDB: Starting shutdown...
   160601  8:55:18 [Note] InnoDB: Shutdown completed; log sequence number 20410918
   160601  8:55:18 [Note] mysqld: Shutdown complete

Afterwards exit the temporary container and start the mariadb container with ``docker start mariadb``.

.. code-block:: console

   Running command: '/usr/bin/mysqld_safe --wsrep-new-cluster'
   160601 09:08:16 mysqld_safe Logging to '/var/log/kolla/mariadb/mariadb.log'.
   160601 09:08:16 mysqld_safe Starting mysqld daemon with databases from /var/lib/mysql/
   160601 09:08:16 mysqld_safe WSREP: Running position recovery with --log_error='/var/lib/mysql//wsrep_recovery.rNhhQs' --pid-file='/var/lib/mysql//testbed-node-0-recover.pid'
   160601 09:08:19 mysqld_safe WSREP: Recovered position d3027acb-2775-11e6-ad39-32cbcdbfec35:7557

Attach a shell to the mariadb container and login to the MariaDB server to check the status of the node.

.. code-block:: console

   # docker exec -it mariadb bash
   (mariadb)[mysql@testbed-node-0 /]$ mysql -u root -p
   Enter password: qNpdZmkKuUKBK3D5nZ08KMZ5MnYrGEe2hzH6XC0i
   Welcome to the MariaDB monitor.  Commands end with ; or \g.
   Your MariaDB connection id is 1171
   Server version: 10.0.25-MariaDB-1~trusty-wsrep

   Copyright (c) 2000, 2016, Oracle, MariaDB Corporation Ab and others.

   Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

   MariaDB [(none)]> SHOW STATUS LIKE 'wsrep_evs_state';
   +-----------------+-------------+
   | Variable_name   | Value       |
   +-----------------+-------------+
   | wsrep_evs_state | OPERATIONAL |
   +-----------------+-------------+
   1 row in set (0.01 sec)

Change binary logs days
=======================

https://www.percona.com/blog/2018/03/28/safely-purging-binary-logs-from-master/

.. code-block:: ini
   :caption: environments/kolla/files/overlays/galera.cnf

   [mysqld]
   expire_logs_days = 14

with restart of galera cluster
------------------------------

.. code-block:: console

   $ osism-kolla reconfigure mariadb

without restart of galera cluster
---------------------------------

* set in ``/etc/kolla/mariadb/galera.cnf`` on each galera cluster node

.. code-block:: ini

   [mysqld]
   expire_logs_days = 14

* set in DB on each galera cluster node

.. code-block:: console

   mysql> show global variables like 'expire%';
   +------------------+-------+
   | Variable_name    | Value |
   +------------------+-------+
   | expire_logs_days | 0     |
   +------------------+-------+
   1 row in set (0.00 sec)
   mysql> set global expire_logs_days=14
   Query OK, 0 rows affected (0.00 sec)
   mysql> show global variables like 'expire%';
   +------------------+-------+
   | Variable_name    | Value |
   +------------------+-------+
   | expire_logs_days | 14    |
   +------------------+-------+
   1 row in set (0.00 sec)

* purge binary logs

.. code-block:: console

   mysql> show binary logs;
   +------------------+------------+
   | Log_name         | File_size  |
   +------------------+------------+
   | mysql-bin.000161 |        365 |
   ...
   | mysql-bin.000249 |  358436195 |
   +------------------+------------+
   89 rows in set (0.00 sec)
   mysql> purge binary logs before '2018-10-16 00:00:00';
   Query OK, 0 rows affected (0.00 sec)
   mysql> show binary logs;
   +------------------+------------+
   | Log_name         | File_size  |
   +------------------+------------+
   | mysql-bin.000232 | 1073741921 |
   ...
   | mysql-bin.000249 |  359370671 |
   +------------------+------------+
   18 rows in set (0.00 sec)

Backup
======

>= Stein
--------

<= Rocky
--------

innobackupex
~~~~~~~~~~~~

The MariaDB images contain ``xtrabackup`` from Percona. To use the MariaDB configuration must first be prepared.

Create/extend the file ``environments/kolla/files/overlays/galera.cnf`` with the following content. Maybe you have to reconfigure MariaDB.

.. code-block:: ini

   [xtrabackup]
   password = {{ database_password }}
   user = root

To create a backup, the command ``innobackupex`` is now executed on one of the database nodes.

.. code-block:: console

   $ docker exec -it mariadb innobackupex --galera-info /tmp
   [...]
   180111 09:45:40 Executing UNLOCK TABLES
   180111 09:45:40 All tables unlocked
   180111 09:45:40 Backup created in directory '/tmp/2018-01-11_09-44-20/'
   MySQL binlog position: filename 'mysql-bin.000080', position '242412060', GTID of the last change '0-1-9072431'
   180111 09:45:40 [00] Writing backup-my.cnf
   180111 09:45:40 [00]        ...done
   180111 09:45:40 [00] Writing xtrabackup_info
   180111 09:45:40 [00]        ...done
   xtrabackup: Transaction log of lsn (10823062052) to (10823256961) was copied.
   180111 09:45:40 completed OK!

Instead of adjusting the configuration, user name and password can also be specified by parameter.
Note that the password is visible.

.. code-block:: console

   docker exec -it mariadb innobackupex \
     -u root -p qNpdZmkKuUKBK3D5nZ08KMZ5MnYrGEe2hzH6XC0i \
     --galera-info /tmp

It is also possible to backup only certain databases. The parameter ``--databases``
is used for this purpose. The format is ``databasename[.tablename]``. Multiple entries
are separated by a space.

.. code-block:: console

   docker exec -it mariadb innobackupex \
     -u root -p qNpdZmkKuUKBK3D5nZ08KMZ5MnYrGEe2hzH6XC0i \
     --galera-info \
     --databases "panko" /tmp

At the end of the backup process a short status change of the node takes place.

.. code-blone:: none

   SYNCED -> DONOR/DESYNCED -> JOINED -> SYNCED

The following entry can be found in ``/var/log/kolla/mariadb/mariadb.log`` on the node where the backup is created.

.. code-block:: none

   2020-02-10 22:55:00 140591107139328 [Note] WSREP: Member 0.0 (testbed-node-1) desyncs itself from group
   2020-02-10 22:55:00 140591107139328 [Note] WSREP: Shifting SYNCED -> DONOR/DESYNCED (TO: 1182)
   2020-02-10 22:55:00 140591322765056 [Note] WSREP: Provider paused at f0bbc6d1-4b81-11ea-acfb-5a3837714e6a:1182 (1565)
   2020-02-10 22:55:02 140591322765056 [Note] WSREP: resuming provider at 1565
   2020-02-10 22:55:02 140591322765056 [Note] WSREP: Provider resumed.
   2020-02-10 22:55:02 140591107139328 [Note] WSREP: Member 0.0 (testbed-node-1) resyncs itself to group
   2020-02-10 22:55:02 140591107139328 [Note] WSREP: Shifting DONOR/DESYNCED -> JOINED (TO: 1182)
   2020-02-10 22:55:02 140591107139328 [Note] WSREP: Member 0.0 (testbed-node-1) synced with group.
   2020-02-10 22:55:02 140591107139328 [Note] WSREP: Shifting JOINED -> SYNCED (TO: 1182)
   2020-02-10 22:55:02 140591391913728 [Note] WSREP: Synchronized with group, ready for connections

On the other nodes there is the following entry.

.. code-block:: none

   2020-02-10 22:55:00 139785272289024 [Note] WSREP: Member 0.0 (testbed-node-1) desyncs itself from group
   2020-02-10 22:55:02 139785272289024 [Note] WSREP: Member 0.0 (testbed-node-1) resyncs itself to group
   2020-02-10 22:55:02 139785272289024 [Note] WSREP: Member 0.0 (testbed-node-1) synced with group.

The backup is then prepared.

.. code-block:: console

   docke exec -it mariadb innobackupex --apply-log /tmp/2018-01-11_09-44-20/
   [...]
   200210 09:38:36 completed OK!

The backup is stored on the data volume of the ``mariadb`` container. It can be picked up from there with the following call.

.. code-block:: console

   $ sudo mkdir -p /opt/xtrabackup && sudo chown dragon: /opt/xtrabackup
   $ docker cp mariadb:/tmp/2018-01-11_09-44-20 /opt/xtrabackup

The directory ``/tmp/2018-01-11_09-44-20`` to be copied is output at the end of the execution of ``innobackupex``.

.. code-block:: none

   180111 09:45:40 Backup created in directory '/tmp/2018-01-11_09-44-20/'

Then the backup can be removed from the container.

.. code-block:: console

   $ docker exec -it mariadb rm -rf /tmp/2018-01-11_09-44-20

You can also use the integrated Ansible playbook.

.. code-block:: console

   $ osism-generic backup-mariadb -l testbed-node-1.osism.local

mariabackup
~~~~~~~~~~~

From Stein on, ``mariabackup`` is used in Kolla-Ansible.

.. code-block:: console

    mariabackup \
        --defaults-file=/etc/mysql/my.cnf \
        --backup \
        --stream=xbstream \
        --history=$(date +%d-%m-%Y) | gzip > \
        /tmp/mysqlbackup-$(date +%d-%m-%Y-%s).qp.xbc.xbs.gz

User name and password can also be specified by parameter. Note that the password is visible.

.. code-block:: console

    mariabackup \
        --defaults-file=/etc/mysql/my.cnf \
        -u root -p qNpdZmkKuUKBK3D5nZ08KMZ5MnYrGEe2hzH6XC0i \
        --backup \
        --stream=xbstream \
        --history=$(date +%d-%m-%Y) | gzip > \
        /tmp/mysqlbackup-$(date +%d-%m-%Y-%s).qp.xbc.xbs.gz

Optimize database
=================

.. note::

   Depending on the database/table, this process may take some time and
   generate a high load on the database.

The following example optimizes the database ``heat``. All tables are optimized one
after the other.

A single table (e.g. ``engine``) in the database ``heat`` can be optimized with
``heat engine`` instead of ``heat``.

Individual tables can be optimized with ``heat engine`` instead of ``heat``.

.. code-block:: console

   du -h /var/lib/docker/volumes/mariadb/_data/heat
   97M     /var/lib/docker/volumes/mariadb/_data/heat

.. code-block:: console

   docker exec -it mariadb mysqlcheck -u root -p --optimize --skip-write-binlog du
   Enter password: qNpdZmkKuUKBK3D5nZ08KMZ5MnYrGEe2hzH6XC0i
   heat.event
   note     : Table does not support optimize, doing recreate + analyze instead
   status   : OK
   heat.migrate_version
   note     : Table does not support optimize, doing recreate + analyze instead
   status   : OK
   [...]

.. code-block:: console

   du -h /var/lib/docker/volumes/mariadb/_data/heat
   7.1M    /var/lib/docker/volumes/mariadb/_data/heat
