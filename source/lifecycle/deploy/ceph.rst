====
Ceph
====

.. note:: Run this command on the manager node.

.. code-block:: console

   $ osism-ceph ROLE

* mons
* mgrs
* mdss
* osds

Dashboard
=========

* http://docs.ceph.com/docs/luminous/mgr/dashboard/

* manual activation

.. code-block:: console

   $ ceph mgr module enable dashboard

* ``environments/ceph/configuration.yml``

.. code-block:: yaml

   ##########################
   # custom

   ceph_conf_overrides:
     mon:
       mgr initial modules: dashboard
