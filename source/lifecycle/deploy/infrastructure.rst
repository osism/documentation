==============
Infrastructure
==============

.. note:: Run this command on the manager node.

Common
======

.. code-block:: console

   $ osism-kolla deploy common

Logging
=======

.. code-block:: console

   $ osism-kolla deploy haproxy
   $ osism-kolla deploy elasticsearch
   $ osism-kolla deploy kibana

Monitoring
==========

.. code-block:: console

   $ osism-kolla deploy grafana
   $ osism-monitoring prometheus-exporter
   $ osism-monitoring prometheus
   $ osism-monitoring monitoring

Custom
======

.. code-block:: console

   $ osism-run custom cronjobs
