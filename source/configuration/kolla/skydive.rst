=======
Skydive
=======

.. note::

  Service Skydive is a technical preview.

* http://skydive.network/documentation/

Configuration parameters
========================

.. code-block:: yaml

   enable_skydive: "yes"

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
