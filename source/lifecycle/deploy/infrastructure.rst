==============
Infrastructure
==============

.. note:: Run this command on the manager node.

Logging
=======

.. code-block:: console

   $ osism-kolla deploy haproxy
   $ osism-kolla deploy elasticsearch
   $ osism-kolla deploy kibana

Common
======

.. code-block:: console

   $ osism-kolla deploy common
   $ osism-run custom cronjobs

Monitoring
==========

.. code-block:: console

   $ osism-kolla deploy grafana
   $ osism-monitoring prometheus-exporter
   $ osism-monitoring prometheus
   $ osism-monitoring monitoring
