====
Ceph
====

Cluster start and stop
======================

* https://www.openattic.org/posts/how-to-do-a-ceph-cluster-maintenanceshutdown/

**Stop**

.. warning::

   Ensure that any services/clients using Ceph are stopped.

.. warning::

   Make sure the cluster is in a healthy state.

1. Set OSD flags

.. code-block:: console

   $ ceph osd set noout
   $ ceph osd set nobackfill
   $ ceph osd set norecover
   $ ceph osd set norebalance
   $ ceph osd set nodown
   $ ceph osd set pause

2. Stop the manager services (one by one)

.. code-block::

   $ systemctl stop ceph-mgr@HOSTNAME.service

3. Stop the osd servies (one by one)

.. code-block::

   $ systemctl stop ceph-osd@DEVICE.service

4. Stop the monitor service (one by one)

.. code-block::

   $ systemctl stop ceph-mon@HOSTNAME.service

**Start**

1. Start the monitor services (one by one)

.. code-block::

   $ systemctl start ceph-mon@HOSTNAME.service

2. Start the osd services (one by one)

.. code-block::

   $ systemctl start ceph-osd@DEVICE.service

3. Start the manager service (one by one)

.. code-block::

   $ systemctl start ceph-mgr@HOSTNAME.service

4. Unset OSD flags

.. code-block:: console

   $ ceph osd unset pause
   $ ceph osd unset nodown
   $ ceph osd unset norebalance
   $ ceph osd unset norecover
   $ ceph osd unset nobackfill
   $ ceph osd unset noout

**Check**

.. code-block::

   $ ceph -s
