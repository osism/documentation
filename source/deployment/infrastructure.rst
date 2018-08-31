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

Custom
======

.. code-block:: console

   $ osism-run custom cronjobs
