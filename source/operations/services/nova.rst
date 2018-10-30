====
Nova
====

* https://docs.openstack.org/nova/latest/cli/nova-manage.html

Archive deleted rows
====================

.. note::

   This command is executed on a controller node.

.. code-block:: console

   $ docker exec -it nova_api nova-manage db archive_deleted_rows --verbose --until-complete
   Archiving...........complete
   +--------------------------+-------------------------+
   | Table                    | Number of Rows Archived |
   +--------------------------+-------------------------+
   | block_device_mapping     | 8357                    |
   | instance_actions         | 15796                   |
   | instance_actions_events  | 14889                   |
   | instance_extra           | 7855                    |
   | instance_faults          | 37                      |
   | instance_info_caches     | 7852                    |
   | instance_metadata        | 203                     |
   | instance_system_metadata | 118642                  |
   | instances                | 7852                    |
   | migrations               | 21                      |
   | quotas                   | 707                     |
   | reservations             | 41815                   |
   | virtual_interfaces       | 8389                    |
   +--------------------------+-------------------------+

Compute service delete
======================

* check disabled compute service

.. code-block:: console

  $ openstack --os-cloud admin compute service list | grep disabled
  +-----+------------------+-------------------+----------+----------+-------+----------------------------+
  |  ID | Binary           | Host              | Zone     | Status   | State | Updated At                 |
  +-----+------------------+-------------------+----------+----------+-------+----------------------------+
  | 100 | nova-compute     | nova-compute01    | nova     | disabled | down  | 2018-05-17T12:17:24.000000 |
  +-----+------------------+-------------------+----------+----------+-------+----------------------------+
  $ openstack --os-cloud admin hypervisor list | grep down
  |  4 | nova-compute01.openstack.org    | QEMU            | 192.168.1.50  | down  |

* delete compute service

.. code-block:: console

  $ openstack --os-cloud admin compute service delete 100
  $ openstack --os-cloud admin compute service list | grep disabled
  $ openstack --os-cloud admin hypervisor list | grep down