========
Keystone
========

Notes
=====

* The project ``service`` is an integral part of OpenStack. It must not be
  deleted under any circumstances. Do not delete! All services no longer
  work when deleted.
* The service users, like ``nova`` or ``neutron``, are necessary for the
  functionality of the OpenStack components. Do not delete them! The services
  will no longer work if deleted.
* It is not recommended to delete the project ``admin`` or the user ``admin``.
  We do not support it.
