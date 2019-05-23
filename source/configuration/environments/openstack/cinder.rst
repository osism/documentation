======
Cinder
======

iSCSI support
=============

* ``environments/kolla/configuration.yml``

.. code-block:: yaml

   enable_cinder_backend_iscsi: yes
   enable_cinder_backend_lvm: no

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
