======
Cinder
======

LVM support
===========

* ``environments/kolla/configuration.yml``

.. code-block:: yaml

   enable_cinder_backend_lvm: "yes"

* create PV and VG

.. code-block:: console

   pvcreate /dev/sdX /dev/sdY
   vgcreate cinder-volume /dev/sdX /dev/sdY

iSCSI support
=============

* ``environments/kolla/configuration.yml``

.. code-block:: yaml

   enable_cinder_backend_iscsi: "yes"
   enable_cinder_backend_lvm: "no"

* ``inventory/hosts``

.. code-block:: ini

   [iscsid:children]
   compute
   storage
   ironic-conductor

   [multipathd:children]
   compute
   storage

   [tgtd:children]
   storage
