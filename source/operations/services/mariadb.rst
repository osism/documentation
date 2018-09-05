=======
MariaDB
=======

Cluster start and stop
======================

* http://galeracluster.com/documentation-webpages/restartingcluster.html

**Stop**

.. warning::

   Ensure that any services using MariaDB are stopped.

Carry out the following steps on all nodes (one by one) and note the order of the nodes.

1. Ensure that ``wsrep_local_state_comment`` is ``synced``

.. code-block:: console

   $ docker exec -it mariadb mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_local_state_comment'"
   Enter password: 
   +---------------------------+--------+
   | Variable_name             | Value  |
   +---------------------------+--------+
   | wsrep_local_state_comment | Synced |
   +---------------------------+--------+

2. Stop the ``mariadb`` container

.. code-block:: console

   $ docker stop mariadb

**Start**

1. Identify the node with the most advanced ``seqno`` (this should be the last stopped node)

.. code-block:: console

   $ docker cp mariadb:/var/lib/mysql/grastate.dat -

2. Start the most advanced node as the first node of the cluster

.. code-block:: console

   $ docker start mariadb

3. Start the rest of the nodes (one by one)

.. code-block:: console

   $ docker start mariadb

**Check**

.. code-block:: console

   $ docker exec -it mariadb mysql -u root -p -e "SHOW STATUS LIKE 'wsrep_%'"
