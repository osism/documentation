=======
Logging
=======

Elasticsearch
=============

* https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html

.. code-block:: console

   dragon@10-11:~$ curl -s http://10.49.0.100:9200/_cluster/health |  python -m json.tool
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
