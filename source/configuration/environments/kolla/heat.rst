====
Heat
====

* https://docs.openstack.org/heat/latest/

Configuration parameters
========================

.. code-block:: yaml

   enable_heat: "yes"
   enable_horizon_heat: "{{ enable_heat | bool }}"

Inventory groups
================

.. code-block:: ini

   [heat:children]
   control

   # heat

   [heat-api:children]
   heat

   [heat-api-cfn:children]
   heat

   [heat-engine:children]
   heat

Use of self-signed certificates
===============================

.. code-block:: ini
   :caption: environments/kolla/files/overlays/heat.conf

   [clients_keystone]
   insecure = True
