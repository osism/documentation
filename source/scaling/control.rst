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

Kibana
------

.. code-block:: console

   osism-kolla deploy kibana -l testbed-node-2.osism.local

HAProxy
-------

.. code-block:: console

   osism-kolla deploy haproxy -l testbed-node-2.osism.local

Removing a control node
=======================
