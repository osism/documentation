=======
Freezer
=======

* https://docs.openstack.org/freezer/latest/

Configuration parameters
========================

.. code-block:: yaml

   enable_freezer: "no"
   enable_horizon_freezer: "{{ enable_freezer | bool }}"

Inventory groups
================

.. code-block:: ini

   [freezer:children]
   control

   # freezer

   [freezer-api:children]
   freezer

   [freezer-scheduler:children]
   freezer
