========
Skydive
========

* http://skydive.network/documentation/

Configuration parameters
========================

.. code-block:: yaml

   enable_skydive: "no"

Inventory groups
================

.. code-block:: ini

   [skydive:children]
   monitoring

   # skydive

   [skydive-analyzer:children]
   skydive

   [skydive-agent:children]
   compute
   network
