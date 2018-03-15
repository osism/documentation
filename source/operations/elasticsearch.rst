=============
Elasticsearch
=============

Delete old indices
==================

* https://www.elastic.co/guide/en/elasticsearch/reference/current/_list_all_indices.html

.. code-block:: none

   $ curl -s http://10.49.0.100:9200/_cat/indices?v | sort
   green  open   flog-2018.02.14 tqkXs5DSQQa7SUGALPCqYA   5   1      15694            0     22.4mb         11.3mb
   green  open   flog-2018.02.15 mFR46PEJQjW3bebsDJuHSg   5   1    8283538            0      7.3gb          3.6gb
   [...]
   green  open   flog-2018.03.12 e0Nb5Y46QeqKSz80vThVkg   5   1    4420167            0      4.4gb          2.2gb
   green  open   flog-2018.03.13 3MggZdM3QgWYhwzdI4q5AA   5   1    4401687            0      4.4gb          2.2gb
   green  open   .kibana         OVJoP2jSQ6W8KuHiHcyYQQ   1   1          4            0     45.4kb         22.7kb
   health status index           uuid                   pri rep docs.count docs.deleted store.size pri.store.size

* https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-delete-index.html

.. code-block:: none

   $ curl -s -X DELETE http://10.49.0.100:9200/flog-2018.02.14
   {"acknowledged":true}

With curator
------------

* https://github.com/elastic/curator

Place this file in ``/usr/share/elasticsearch/.curator/curator.yml``.

.. code-block:: yaml

   ---
   # Remember, leave a key empty if there is no value.  None will be a string,
   # not a Python "NoneType"
   client:
     hosts:
       - 10.49.20.10
       - 10.49.20.11
       - 10.49.20.12
     port: 9200
     url_prefix:
     use_ssl: False
     certificate:
     client_cert:
     client_key:
     ssl_no_validate: False
     http_auth:
     timeout: 30
     master_only: False

   logging:
     loglevel: INFO
     logfile:
     logformat: default
     blacklist: ['elasticsearch', 'urllib3']

.. code-block:: shell

   $ docker exec -it elasticsearch bash
   (elasticsearch)[elasticsearch@20-10 /]$ export LC_ALL=C.UTF-8
   (elasticsearch)[elasticsearch@20-10 /]$ export LANG=C.UTF-8
   (elasticsearch)[elasticsearch@20-10 /]$ curator_cli --host 10.49.20.10 show_indices
   flog-2018.02.09
   flog-2018.02.10
   flog-2018.02.11
   [...]
   flog-2018.02.27
   flog-2018.02.28

* https://discuss.elastic.co/t/delete-indices-older-than-30-days/96630/9

Place this file in ``/usr/share/elasticsearch/delete-indices-older-than-30-days.yml``.

.. code-block:: yaml

   ---
   actions:
     1:
       action: delete_indices
       description: Delete indices with %Y.%m.%d in the name where that date is older than 30 days
       options:
         ignore_empty_list: True
       filters:
         - filtertype: age
           source: name
           timestring: '%Y.%m.%d'
           unit: days
           unit_count: 30
           direction: older

.. code-block:: shell

   (elasticsearch)[elasticsearch@20-10 /]$ curator delete-indices-older-than-30-days.yml
   2018-02-28 14:13:42,992 INFO      Preparing Action ID: 1, "delete_indices"
   2018-02-28 14:13:43,004 INFO      Trying Action ID: 1, "delete_indices": Delete indices with %Y.%m.%d in the name where that date is older than 30 days
   2018-02-28 14:13:43,036 INFO      Deleting selected indices: ['flog-2018.02.09', 'flog-2018.02.11', 'flog-2018.02.10', 'flog-2018.02.14', 'flog-2018.02.12', 'flog-2018.02.13']
   2018-02-28 14:13:43,036 INFO      ---deleting index flog-2018.02.09
   2018-02-28 14:13:43,036 INFO      ---deleting index flog-2018.02.11
   2018-02-28 14:13:43,036 INFO      ---deleting index flog-2018.02.10
   2018-02-28 14:13:43,036 INFO      ---deleting index flog-2018.02.14
   2018-02-28 14:13:43,036 INFO      ---deleting index flog-2018.02.12
   2018-02-28 14:13:43,037 INFO      ---deleting index flog-2018.02.13
   2018-02-28 14:13:51,145 INFO      Action ID: 1, "delete_indices" completed.
   2018-02-28 14:13:51,145 INFO      Job completed.
