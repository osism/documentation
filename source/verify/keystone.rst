========
Keystone
========

.. code-block:: shell

   $ openstack --os-cloud testbed token issue
   +------------+-------------------------------+
   | Field      | Value                         |
   +------------+-------------------------------+
   | expires    | 2018-01-16T10:05:59+0000      |
   | id         | gAAAAABaXH0HNIsZUXKGYBPl[...] |
   | project_id | de8299637be6486f9dd0d51c[...] |
   | user_id    | e2cf7b56b0e647e79f25c6b0[...] |
   +------------+-------------------------------+

Other tests are the following commands.

* ``openstack --os-cloud testbed catalog list``
* ``openstack --os-cloud testbed endpoint list``
* ``openstack --os-cloud testbed domain list``
* ``openstack --os-cloud testbed user list --domain default``
