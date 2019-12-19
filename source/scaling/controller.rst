================
Controller nodes
================

.. contents::
   :local:

Adding a controller node
========================

Inventory
---------

If the default inventory is used it is sufficient to add the new node to the ``control`` group.

.. warning::

   Always add the new controller as the last host in the group.

Kibana
------

.. code-block:: console

   osism-kolla deploy kibana -l NEW-CONTROLLER

HAProxy
-------

.. code-block:: console

   osism-kolla deploy haproxy -l NEW-CONTROLLER

Removing a controller node
==========================
