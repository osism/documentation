=============
Elasticsearch
=============

Delete old indices
==================

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
       description: Delete indices with %Y.%m.%d in the name where that date is older than 14 days
       options:
         ignore_empty_list: True
       filters:
         - filtertype: age
           source: name
           timestring: '%Y.%m.%d'
           unit: days
           unit_count: 14
           direction: older

.. code-block:: shell

   (elasticsearch)[elasticsearch@20-10 /]$ curator delete-indices-older-than-14-days.yml
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
