========
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
