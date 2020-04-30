========
RabbitMQ
========

.. contents::
   :local:

Cluster start and stop
======================

Stop
----

Ensure that any services using RabbitMQ are stopped.

Stop the ``rabbitmq`` container on all controller nodes (one by one) and note the order of the nodes.

.. code-block:: console

   docker stop rabbitmq

Start
-----

Successively start the ``rabbitmq`` container on all controller nodes (one by one) in the reverse order.

.. code-block:: console

   docker start rabbitmq

Check
-----

.. code-block:: console

   docker exec -it rabbitmq rabbitmqctl cluster_status
   Cluster status of node 'rabbit@testbed-node-1'
   [{nodes,[{disc,['rabbit@testbed-node-0','rabbit@testbed-node-1']}]},
    {running_nodes,['rabbit@testbed-node-0','rabbit@testbed-node-1']},
    {cluster_name,<<"rabbit@testbed-node-0.osism.local">>},
    {partitions,[]},
    {alarms,[{'rabbit@testbed-node-0',[]},{'rabbit@testbed-node-1',[]}]}]

Emptying the notification queues
================================

If notifications of individual services are activated and these notifications are not consumed,
for example by Panko, over the course of time many unprocessed messages accumulate on the
individual notification queues.

.. code-block:: console

   docker exec -it rabbitmq rabbitmqctl list_queues | grep -v $'\t0'
   Listing queues
   versioned_notifications.info    2983
   versioned_notifications.error   29

.. code-block:: console

   docker exec -it rabbitmq rabbitmqctl purge_queue versioned_notifications.info
   Purging queue 'versioned_notifications.info' in vhost '/'

rabbitmqadmin
=============

https://www.rabbitmq.com/management-cli.html

The management plugin ships with a command line tool rabbitmqadmin which can perform
some of the same actions as the Web-based UI, and which may be more convenient for
automation tasks. Note that rabbitmqadmin is just a specialised HTTP client; if you
are contemplating invoking rabbitmqadmin from your own program you may want to consider
using an HTTP API client library instead.

.. code-block:: console

   curl -o rabbitmqadmin http://api-int.osism.local:15672/cli/rabbitmqadmin

Cluster status
==============

.. code-block:: console

   docker exec -it rabbitmq rabbitmqctl eval 'rabbit_clusterer:status().'
   Rabbit is running in cluster configuration:
   [{node_ids,[{'rabbit@testbed-node-0',<<33,223,136,84,52,55,149,250,118,202,
                                          103,22,88,214,60,236>>},
               {'rabbit@testbed-node-1',<<186,47,70,175,150,251,92,174,244,196,
                                          192,37,25,113,247,124>>}]},
    {gospel,{node,'rabbit@testbed-node-0'}},
    {nodes,[{'rabbit@testbed-node-0',disc},{'rabbit@testbed-node-1',disc}]},
    {version,1}]
   Running nodes: ['rabbit@testbed-node-0','rabbit@testbed-node-1']
   ok

Broken queue
============

.. code-block:: console

   2020-03-20 17:24:44.846 6 ERROR oslo_service.service MessageDeliveryFailure: Unable to connect to AMQP server on 10.49.20.11:5672 after None tries: Queue.declare: (404) NOT_FOUND - failed to perform operation on queue 'dhcp_agent.30-02' in vhost '/' due to timeout

Stop the service, delete the queue and start the service.

Set number of Erlang schedulers
===============================

Schedulers in the runtime assign work to kernel threads that perform it. By
default the runtime will start one scheduler for one CPU core it detects. This
can lead to permanent high CPU utilisation. Setting the number of schedulers to
a lower value, will decrease CPU utilisation considerably.

.. code-block:: yaml
   :caption: environments/kolla/configuration.yml

   rabbitmq_server_additional_erl_args: "+S 1:1"

See `RabbitMQ documentation <https://www.rabbitmq.com/runtime.html>`_ for more
details.

