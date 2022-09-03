=======
Fluentd
=======

.. contents::
   :depth: 2

The client noticed that the server is not a supported distribution of Elasticsearch.
====================================================================================

.. code-block:: console

   $ docker logs fluentd -n 20 -f
   ...
   + exec /usr/sbin/td-agent -o /var/log/kolla/fluentd/fluentd.log
   Running command: '/usr/sbin/td-agent -o /var/log/kolla/fluentd/fluentd.log'
   2022-01-12 15:35:50 +0000 [error]: fluent/log.rb:372:error: unexpected error error_class=Elasticsearch::UnsupportedProductError error="The client noticed that the server is not a supported distribution of Elasticsearch."

   $ osism-kolla refresh-containers common
