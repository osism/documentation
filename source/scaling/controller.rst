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

HAProxy
-------

.. code-block:: console

   osism-kolla deploy haproxy -l NEW-CONTROLLER

Removing a controller node
==========================
