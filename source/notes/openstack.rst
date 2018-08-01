=========
OpenStack
=========

Nested virtualisation
=====================

.. note:: The activation of nested virtualization will be enabled automatically in the future.
          Until then carry out subsequent manual steps.

AMD
---

.. code-block:: console

   $ echo "options kvm-amd nested=y" | sudo tee /etc/modprobe.d/kvm-nested-virtualization.conf

.. code-block:: console

   $ cat /sys/module/kvm_amd/parameters/nested
   Y

Intel
-----


.. code-block:: console

   $ echo "options kvm-intel nested=y" | sudo tee /etc/modprobe.d/kvm-nested-virtualization.conf

.. code-block:: console

   $ cat /sys/module/kvm_intel/parameters/nested
   Y

References
----------

* https://docs.openstack.org/devstack/latest/guides/devstack-with-nested-kvm.html

Support of QCOW2 images
=======================

Do not use QCOW2 images. Only use RAW images.

* https://support.metacloud.com/hc/en-us/articles/234955888-Converting-QCOW2-Images-to-RAW-with-Ceph-Root-Disk
* http://docs.metacloud.com/latest/user-guide/converting-images/

Performance tweaks via image extra properties
=============================================

* https://redhatstackblog.redhat.com/2017/01/18/9-tips-to-properly-configure-your-openstack-instance/
* http://ceph.com/planet/more-recommendations-for-ceph-and-openstack/

Virtio SCSI
===========

Set ``hw_scsi_model=virtio-scsi`` and ``hw_disk_bus=scsi``.

.. code-block:: console

   $ openstack image set
     --property hw_scsi_model=virtio-scsi
     --property hw_disk_bus=scsi
     <name or ID of your image>

Virtio Multiqueuing
===================

OS/distribution type
====================

Set ``os_type`` (``linux`` or ``windows``) and ``os_distro``.

Possible values for ``os_distro`` can be found under https://docs.openstack.org/python-glanceclient/latest/cli/property-keys.html.

Alternatively, the program ``osinfo-query`` contained in the package ``libosinfo-bin`` can be used.

.. code-block:: console

   $ osinfo-query os
    Short ID    | Name                    | Version | ID
   -------------+-------------------------+---------+---------------------------------
    altlinux1.0 | Mandrake RE Spring 2001 | 1.0     | http://altlinux.org/altlinux/1.0
    altlinux2.0 | ALT Linux 2.0           | 2.0     | http://altlinux.org/altlinux/2.0
   [...]

Remove services
===============

Cinder
------

* https://docs.openstack.org/cinder/latest/man/cinder-manage.html

.. code-block:: console

   $ docker exec -it cinder_api cinder-manage service list
   Binary         Host   Zone  Status    State Updated At           RPC Version  Object Version  Cluster
   [...]
   cinder-backup  50-10  nova  disabled  XXX   2017-10-03 18:14:59  2.0          1.11
   [...]
   $ docker exec -it cinder_api cinder-manage service remove cinder-backup 50-10
   Service cinder-backup on host 50-10 removed.

Horizon webinterface broken
===========================

Description
-----------

.. image:: /images/horizon-broken.png

Solution
--------

You have to cleanup and restart all horizon containers.

.. code-block:: console

   $ docker exec -it horizon rm /var/lib/kolla/.local_settings.md5sum.txt && docker restart horizon

Empty action list in Mistral
============================

Solution
--------

You have to populate the database.

.. code-block:: console

   $ docker exec -it mistral_api mistral-db-manage --config-file /etc/mistral/mistral.conf populate
