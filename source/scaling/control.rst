=============
Control nodes
=============

.. contents::
   :local:

Adding a control node
=====================

Inventory
---------

If the default inventory is used it is sufficient to add the new node to the ``control`` group.

.. warning::

   Always add the new control node as the last host in the group.

HAProxy
-------

.. code-block:: console

   osism-kolla deploy haproxy -e kolla_serial=1

Kibana
------

.. code-block:: console

   osism-kolla deploy kibana -l testbed-node-2.osism.local

Elasticsearch
-------------

.. code-block:: console

   osism-kolla deploy elasticsearch -e kolla_serial=1

Redis
-----

.. code-block:: console

   osism-kolla deploy redis -l testbed-node-2.osism.local

Memcached
---------

.. code-block:: console

   osism-kolla deploy memcached -l testbed-node-2.osism.local

RabbitMQ
--------

MariaDB
-------

.. code-block:: console

   osism-kolla deploy mariadb

Grafana
-------

.. code-block:: console

   osism-kolla upgrade grafana -l testbed-node-2.osism.local

Removing a control node
=======================
