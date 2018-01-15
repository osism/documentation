=============================================
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

FIXME

OS/distribution type
====================

Set ``os_type`` (``linux`` or ``windows``) and ``os_distro``.

Possible values for ``os_distro`` can be found under https://docs.openstack.org/python-glanceclient/latest/cli/property-keys.html.

Alternatively, the program ``osinfo-query`` contained in the package ``libosinfo-bin`` can be used.

.. code-block:: shell

   $ osinfo-query os
    Short ID             | Name                                               | Version  | ID
   ----------------------+----------------------------------------------------+----------+-----------------------------------------
    altlinux1.0          | Mandrake RE Spring 2001                            | 1.0      | http://altlinux.org/altlinux/1.0
    altlinux2.0          | ALT Linux 2.0                                      | 2.0      | http://altlinux.org/altlinux/2.0
   [...]
