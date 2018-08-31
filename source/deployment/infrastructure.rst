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

Helper
======

.. code-block:: console

   $ osism-infrastructure helper --tags openstackclient
   $ osism-infrastructure helper --tags cephclient
   $ osism-infrastructure helper --tags phpmyadmin
   $ osism-infrastructure helper --tags rally
   $ osism-infrastructure helper --tags phpmyadmin

Custom
======

.. code-block:: console

   $ osism-run custom cronjobs
