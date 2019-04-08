=======
Horizon
=======

.. contents::
   :local:

Disable "Consistency Groups"  and "Consistency Group Snapshots" dashboards
==========================================================================

The two dashboards ``Consistency Groups`` and ``Consistency Group Snapshots`` are unfortunately
always activated in Horizon and there is no configuration parameter to deactivate them.
Therefore only the deactivation by manual removal of files within the Horizon containers works
at the moment.

.. code-block:: console

   $ docker exec -it horizon bash
   (horizon)[root@20-10 /]# find /var/lib/kolla \
     -name '_1340_project_consistency_groups_panel.py*' \
     -exec rm -f {} \;
   (horizon)[root@20-10 /]# find /var/lib/kolla \
     -name '_1350_project_cg_snapshots_panel.py*' \
     -exec rm -f {} \;

.. code-block:: console

   $ docker restart horizon


Horizon webinterface broken
===========================

Description
-----------

.. image:: /images/horizon-broken.png

Solution
--------

You have to cleanup and restart all horizon containers.

* Up to Queens release:

  .. code-block:: console

     $ docker exec -it horizon rm /var/lib/kolla/.local_settings.md5sum.txt && docker restart horizon

* As of Rocky release

  .. code-block:: console

     $ docker exec -it horizon rm /var/lib/kolla/.settings.md5sum.txt && docker restart horizon
