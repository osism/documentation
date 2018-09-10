====
Ceph
====

Cluster start and stop
======================

* https://www.openattic.org/posts/how-to-do-a-ceph-cluster-maintenanceshutdown/

**Stop**

.. warning::

   Ensure that any services/clients using Ceph are stopped and that the cluster is in a healthy state.

1. Set OSD flags

.. code-block:: console

   $ ceph osd set noout
   $ ceph osd set nobackfill
   $ ceph osd set norecover
   $ ceph osd set norebalance
   $ ceph osd set nodown
   $ ceph osd set pause

2. Stop the manager services (one by one)

.. code-block:: console

   $ systemctl stop ceph-mgr@HOSTNAME.service
   $ systemctl disable ceph-mgr@HOSTNAME.service

3. Stop the osd servies (one by one)

.. code-block:: console

   $ systemctl stop ceph-osd@DEVICE.service
   $ systemctl disable ceph-osd@DEVICE.service

4. Stop the monitor service (one by one)

.. code-block:: console

   $ systemctl stop ceph-mon@HOSTNAME.service
   $ systemctl disable ceph-mon@HOSTNAME.service

**Start**

1. Start the monitor services (one by one)

.. code-block:: console

   $ systemctl start ceph-mon@HOSTNAME.service
   $ systemctl enable ceph-mon@HOSTNAME.service

2. Start the osd services (one by one)

.. code-block:: console

   $ systemctl start ceph-osd@DEVICE.service
   $ systemctl enable ceph-osd@DEVICE.service

3. Start the manager service (one by one)

.. code-block:: console

   $ systemctl start ceph-mgr@HOSTNAME.service
   $ systemctl enable ceph-mgr@HOSTNAME.service

4. Unset OSD flags

.. code-block:: console

   $ ceph osd unset pause
   $ ceph osd unset nodown
   $ ceph osd unset norebalance
   $ ceph osd unset norecover
   $ ceph osd unset nobackfill
   $ ceph osd unset noout

**Check**

.. code-block:: console

   $ ceph -s

Deep scrub distribution
=======================

* https://ceph.com/geen-categorie/deep-scrub-distribution/

Distribution per weekday:

.. code-block:: console

   $ for date in $(ceph pg dump | grep active | awk '{ print $20 })'; do date +%A -d $date; done | sort | uniq -c

Distribution per hours:

.. code-block:: console

   $ for date in $(ceph pg dump | grep active | awk '{ print $21 }'); do date +%H -d $date; done | sort | uniq -c
