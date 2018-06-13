=====
Kolla
=====

Ocata -> Pike
=============

Inventory
---------

* Add new host groups to ``inventory/hosts`` to the ``environment: kolla`` section

.. code-block:: ini

   # neutron

   [...]

   [neutron-bgp-dragent:children]
   network

.. code-block:: ini

   # neutron

   [...]

   [openvswitch:children]
   network
   compute

.. code-block:: ini

   ##########################################################
   # environment: kolla

   [...]

   [redis:children]
   control
