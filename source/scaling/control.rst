============
Control node
============

.. contents::
   :local:

Adding a control node
=====================

If a control node is also used as network node, storage node or compute node the
corresponding instructions can be found in the corresponding chapters.

Before deploying the OpenStack services, all necessary infrastructure services
should be added.

If the default inventory is used it is sufficient to add the new node to the
``control`` group.

.. warning::

   Always add the new control node as the last host in the group. This is really
   important. If the new control node is added in the first place, strange
   things can happen.

Infrastructure
--------------

By adding Memcached and RabbitMQ on the control node, all OpenStack services on
the compute nodes and network nodes need to be reconfigured. It is recommended
to combine this with an already pending maintenance of the nodes and not to do
this at the same time as adding the control node.

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

   OSISM manager version 2020.1 is necessary for the scaling of RabbitMQ.
   Support only from Rocky on.

By default, ``rabbitmq_cluster_version`` is set to ``1``. This value must be incremented
with each change. This configuration change is only necessary for Rocky.

.. code-block:: yaml
   :caption: environments/kolla/configuration.yml

   # rabbitmq

   rabbitmq_cluster_version: 2

.. code-block:: console

   osism-kolla deploy rabbitmq

After deployment, the following commands are executed on the new node. The following steps
are only necessary if Rocky is used.

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

Open vSwitch
~~~~~~~~~~~~

This step is only needed if the control node is also used as network node
or compute node.

.. code-block:: console

   osism-kolla deploy openvswitch -l testbed-node-2.osism.local

OpenStack
---------

This step is performed for each OpenStack service available in the environment.

Due to a restart of the API and scheduler/conductor services this step may cause
a short interruption of availability.

Depending on the OpenStack service ``-e kolla_serial=1`` can be used. This is not
possible for every OpenStack service. Especially not for Keystone.

.. code-block:: console

   osism-kolla deploy SERVICE -l control

Removing a control node
=======================
