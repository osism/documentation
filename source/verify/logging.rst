=======
Logging
=======

Elasticsearch
=============

* https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html

.. note:: Run this command on the manager node.

.. code-block:: console

   $ curl -s http://10.49.0.100:9200/_cluster/health | python -m json.tool
   {
       "active_primary_shards": 321,
       "active_shards": 642,
       "active_shards_percent_as_number": 100.0,
       "cluster_name": "kolla_logging",
       "delayed_unassigned_shards": 0,
       "initializing_shards": 0,
       "number_of_data_nodes": 3,
       "number_of_in_flight_fetch": 0,
       "number_of_nodes": 3,
       "number_of_pending_tasks": 0,
       "relocating_shards": 0,
       "status": "green",
       "task_max_waiting_in_queue_millis": 0,
       "timed_out": false,
       "unassigned_shards": 0
   }

* ``number_of_data_nodes`` should be the number of available Elasticsearch nodes
* ``status`` should be ``green``

Fluentd
=======

.. code-block:: console

   $ docker logs fluentd
   [...]
   2018-06-14 08:15:52 +0000 [info]: #0 listening syslog socket on 10.49.10.11:5140 with udp
   [...]
   2018-06-14 08:27:05 +0000 [info]: #0 Connection opened to Elasticsearch cluster => {:host=>"10.49.0.100", :port=>9200, :scheme=>"http"}
