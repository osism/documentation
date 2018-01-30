=========
OpenStack
=========

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

.. code-block:: shell

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

.. code-block:: shell

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

.. code-block:: shell

   $ docker exec -it cinder_api cinder-manage service list
   Binary         Host   Zone  Status    State Updated At           RPC Version  Object Version  Cluster
   [...]
   cinder-backup  50-10  nova  disabled  XXX   2017-10-03 18:14:59  2.0          1.11
   [...]
   $ docker exec -it cinder_api cinder-manage service remove cinder-backup 50-10
   Service cinder-backup on host 50-10 removed.
