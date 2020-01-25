============
Control node
============

.. contents::
   :local:

Adding a control node
=====================

Inventory
---------

If the default inventory is used it is sufficient to add the new node to the ``control`` group.

.. warning::

   Always add the new control node as the last host in the group.

Infrastructure
--------------

HAProxy
~~~~~~~

.. code-block:: console

   osism-kolla deploy haproxy -e kolla_serial=1

Kibana
~~~~~~

.. code-block:: console

   osism-kolla deploy kibana -l testbed-node-2.osism.local

Elasticsearch
~~~~~~~~~~~~~

.. code-block:: console

   osism-kolla deploy elasticsearch -e kolla_serial=1

Redis
~~~~~

.. code-block:: console

   osism-kolla deploy redis -l testbed-node-2.osism.local

Memcached
~~~~~~~~~

.. code-block:: console

   osism-kolla deploy memcached -l testbed-node-2.osism.local

RabbitMQ
~~~~~~~~

.. note::

   OSISM Version 2020.1 is necessary for the scaling of RabbitMQ. Support only from Rocky on.

By default, ``rabbitmq_cluster_version`` is set to ``1``. This value must be incremented
with each change.

.. code-block:: yaml
   :caption: environments/kolla/configuration.yml

   # rabbitmq

   rabbitmq_cluster_version: 2

.. code-block:: console

   osism-kolla deploy rabbitmq

After deployment, the following commands are executed on the new node.

.. code-block:: console

   docker exec -it rabbitmq rabbitmqctl stop_app
   Stopping rabbit application on node 'rabbit@testbed-node-2'

.. code-block:: console

   docker exec -it rabbitmq rabbitmqctl reset
   Resetting node 'rabbit@testbed-node-2'

.. code-block:: console

   docker exec -it rabbitmq rabbitmqctl start_app
   Starting node 'rabbit@testbed-node-2'

MariaDB
~~~~~~~

* A backup should be created prior to execution.
* It is recommended that you first clean up the individual databases before you start.
* When adding a new node to the MariaDB Galera cluster, the new node is fully synchronized.
  Depending on the size of the database this may take some time.
* When adding the new node, the existing nodes are restarted. There may be a short
  interruption in availability during this time.

.. code-block:: console

   osism-kolla deploy mariadb

Grafana
~~~~~~~

.. code-block:: console

   osism-kolla deploy grafana -l testbed-node-2.osism.local

OpenStack
---------

.. code-block:: console

   osism-kolla deploy SERVICE -l control

Removing a control node
=======================
