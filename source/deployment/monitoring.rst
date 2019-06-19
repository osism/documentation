==========
Monitoring
==========

.. note:: Execute the following commands on the manager node.

The deployment of the monitoring services is optional. They are only deployed if they are
to be used.

Prometheus
==========

Prometheus, a Cloud Native Computing Foundation project, is a systems and service monitoring system.
It collects metrics from configured targets at given intervals, evaluates rule expressions, displays
the results, and can trigger alerts if some condition is observed to be true. [#]_

.. code-block:: console

   $ osism-monitoring prometheus-exporter
   $ osism-monitoring prometheus

Grafana
=======

Grafana is an open source, feature rich metrics dashboard and graph editor for Graphite, Elasticsearch,
OpenTSDB, Prometheus and InfluxDB. [#]_

.. code-block:: console

   $ osism-kolla deploy grafana
   $ osism-monitoring monitoring

.. [#] source: https://github.com/prometheus/prometheus/blob/master/README.md
.. [#] source:  https://github.com/grafana/grafana/blob/master/README.md
