============
Storage node
============

.. contents::
   :depth: 2

.. note::

   If a new node is added in a HCI environment which is used as resource node and
   as control node, first execute the steps for the resource node and then the steps
   for the control node.

Adding a storage resource node
==============================

.. code-block:: console

   osism-ceph osds -l testbed-node-2.osism.local

Removing a storage resource node
================================

Adding a storage control node
=============================

.. code-block:: console

   osism-ceph mons

.. code-block:: console

   osism-ceph mgrs

Removing a storage control node
===============================
