=======
Mistral
=======

* https://docs.openstack.org/mistral/latest/

Configuration parameters
========================

.. code-block:: yaml

   enable_mistral: "no"
   enable_horizon_mistral: "{{ enable_mistral | bool }}"

Inventory groups
================

.. code-block:: ini

   [mistral:children]
   control

   # mistral

   [mistral-api:children]
   mistral

   [mistral-executor:children]
   mistral

   [mistral-engine:children]
   mistral
