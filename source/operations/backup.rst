======
Backup
======

MariaDB
=======

The MariaDB images contain ``xtrabackup`` from Percona. To use the MariaDB configuration must first be prepared.

Create / extend the file ``environments/kolla/files/overlays/galera.cnf`` with the following content. Maybe you have to reconfigure MariaDB.

.. code-block:: ini

   [xtrabackup]
   host = {{ kolla_internal_fqdn }}
   password = {{ database_password }}
   port = {{ database_port }}
   user = root

To create a backup, the command ``innobackupex`` is now executed on one of the database nodes.

.. code-block:: shell

   $ docker exec -it mariadb innobackupex /tmp
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

The backup is stored on the data volume of the ``mariadb`` container. It can be picked up from there with the following call.

.. code-block:: shell

   $ sudo mkdir -p /opt/xtrabackup && sudo chown dragon: /opt/xtrabackup
   $ docker cp mariadb:/tmp/2018-01-11_09-44-20 /opt/xtrabackup

.. note::

   The directory ``/tmp/2018-01-11_09-44-20`` to be copied is output at the end of the execution of ``innobackupex``.

   .. code-block:: shell

      180111 09:45:40 Backup created in directory '/tmp/2018-01-11_09-44-20/'

Then the backup can be removed from the container.

.. code-block:: shell

   $ docker exec -it mariadb rm -rf /tmp/2018-01-11_09-44-20

Elasticsearch
=============

Prometheus
==========
