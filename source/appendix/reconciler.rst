====================
Inventory Reconciler
====================

What is the ``Inventory Reconciler`` and how does it work.

Overview Inventory Reconciler
=============================

* ``Inventory Reconciler`` builds an inventory for ``Ansible``
* out of all data in ``configuration/inventory`` and repositories ``defaults`` and ``generics``

.. image:: /images/overview-reconciler.png

Inventory in detail
===================

The ``configuration/inventory`` directory looks like in testbed

https://github.com/osism/testbed/tree/main/inventory

.. code-block:: console

   $ ls -l /opt/configuration/inventory/
   -rw-rw-r-- 1 dragon dragon   80 Dec 15  2020 10-custom
   -rw-rw-r-- 1 dragon dragon 1255 Sep 14 06:13 20-roles
   -rw-rw-r-- 1 dragon dragon   80 Dec 15  2020 99-overwrite
   drwxrwxr-x 2 dragon dragon 4096 Sep 14 06:13 host_vars

* ``host_vars`` contains the variables about the hosts
* ``10-custom`` contains custom hostgroups
* ``20-roles`` contains the typical hostgroups, like

   * generic
   * manager
   * monitoring
   * control
   * compute
   * network
   * ceph-control
   * ceph-resource

* ``99-overwrite`` all hostgroups here will ``overwrite`` the hostgroups out of ``defaults``, ``generics`` or ``20-roles``

Lifecycle management
====================

Adding a test inventory will result in new inventory for ``Ansible``. Also deleting a test or old inventory (e.g. migrating from NetBox to another tool) will be considered.

Links ``defaults`` and ``generics``
===================================

* defaults https://github.com/osism/ansible-defaults/tree/main/all
* generics https://github.com/osism/cfg-generics/tree/main/inventory
