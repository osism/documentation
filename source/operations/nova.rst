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

Purge rows from the shadow tables
=================================

.. code-block:: console

   docker exec nova_api nova-manage db purge --verbose --before "2018-01-01"
   DB: Deleted 105 rows from shadow_block_device_mapping based on timestamp column deleted_at
   DB: Deleted 197 rows from shadow_instance_actions based on timestamp column created_at
   DB: Deleted 195 rows from shadow_instance_actions_events based on timestamp column created_at
   DB: Deleted 104 rows from shadow_instance_extra based on timestamp column deleted_at
   DB: Deleted 104 rows from shadow_instance_info_caches based on timestamp column deleted_at
   DB: Deleted 1366 rows from shadow_instance_system_metadata based on timestamp column deleted_at
   DB: Deleted 104 rows from shadow_instances based on timestamp column deleted_at
   DB: Deleted 475 rows from shadow_reservations based on timestamp column deleted_at
   DB: Deleted 103 rows from shadow_virtual_interfaces based on timestamp column deleted_at

Compute service delete
======================

* check disabled compute service

.. code-block:: console

  $ openstack --os-cloud admin compute service list
  +-----+------------------+-------------------+----------+----------+-------+----------------------------+
  |  ID | Binary           | Host              | Zone     | Status   | State | Updated At                 |
  +-----+------------------+-------------------+----------+----------+-------+----------------------------+
  [...]
  | 100 | nova-compute     | nova-compute01    | nova     | disabled | down  | 2018-05-17T12:17:24.000000 |
  +-----+------------------+-------------------+----------+----------+-------+----------------------------+
  $ openstack --os-cloud admin hypervisor list
  [...]
  |  4 | nova-compute01.openstack.org    | QEMU            | 192.168.1.50  | down  |

* delete compute service

.. code-block:: console

  $ openstack --os-cloud admin compute service delete 100
  $ openstack --os-cloud admin compute service list
  +-----+------------------+-------------------+----------+----------+-------+----------------------------+
  |  ID | Binary           | Host              | Zone     | Status   | State | Updated At                 |
  +-----+------------------+-------------------+----------+----------+-------+----------------------------+
  [...]
  | 100 | nova-compute     | nova-compute01    | nova     | disabled | up    | 2018-05-17T12:17:24.000000 |
  +-----+------------------+-------------------+----------+----------+-------+----------------------------+
  $ openstack --os-cloud admin hypervisor list
  [...]
  |  4 | nova-compute01.openstack.org    | QEMU            | 192.168.1.50  | up    |

* look in the following databases and tables for old entries

.. code-block:: console

  nova compute_nodes
  $ docker exec -it mariadb mysql -u root -p nova -e "select created_at,id,hypervisor_hostname,deleted,host,deleted_at from compute_nodes;"
  +---------------------+----+---------------------------+---------+------------------+---------------------+
  | created_at          | id | hypervisor_hostname       | deleted | host             | deleted_at          |
  +---------------------+----+---------------------------+---------+------------------+---------------------+
  | 2017-09-27 11:32:23 |  4 | nova-compute01.fqdn.de    |       0 | nova-compute01   | NULL                |
  | 2017-11-08 14:10:58 | 40 | nova-compute02.fqdn.de    |      40 | nova-compute02   | 2018-11-22 13:21:54 |
  | 2019-03-25 11:44:47 | 95 | nova-compute03.fqdn.de    |       0 | nova-compute03   | NULL                |
  +---------------------+----+---------------------------+---------+------------------+---------------------+

  nova services
  $ docker exec -it mariadb mysql -u root -p nova -e "select created_at,id,host,deleted,deleted_at,version from services;"
  +---------------------+-----+------------------+---------+---------------------+---------+
  | created_at          | id  | host             | deleted | deleted_at          | version |
  +---------------------+-----+------------------+---------+---------------------+---------+
  | 2017-09-27 11:32:04 |   4 | nova-compute01   |       0 | NULL                |      16 |
  | 2017-11-08 14:10:57 |  85 | nova-compute02   |      85 | 2018-11-22 13:21:54 |      16 |
  | 2019-03-25 11:44:47 | 143 | nova-compute03   |       0 | NULL                |      16 |
  +---------------------+-----+------------------+---------+---------------------+---------+

  nova_api host_mappings
  $ docker exec -it mariadb mysql -u root -p nova_api -e "select * from host_mappings"
  +---------------------+------------+----+---------+------------------+
  | created_at          | updated_at | id | cell_id | host             |
  +---------------------+------------+----+---------+------------------+
  | 2017-09-27 11:32:36 | NULL       |  4 |       7 | nova-compute01   |
  | 2017-09-27 11:32:36 | NULL       |  7 |       7 | nova-compute02   |
  | 2017-09-27 13:39:18 | NULL       | 10 |       7 | nova-compute03   |
  +---------------------+------------+----+---------+------------------+

  nova_api resource_providers
  $ docker exec -it mariadb mysql -u root -p nova_api -e "select created_at,id,name from resource_providers"
  +---------------------+-------+--------------------------+
  | created_at          | id    | name                     |
  +---------------------+-------+--------------------------+
  | 2017-09-27 11:32:29 |     4 | nova-compute01.fqdn.de   |
  | 2018-11-22 19:48:37 |    73 | nova-compute01.fqdn.de   |
  | 2019-03-25 11:44:47 | 20864 | nova-compute01.fqdn.de   |
  +---------------------+-------+--------------------------+

Copy/Move Instance images manual to another hypervisor
======================================================

* login to hypervisorA

.. code-block:: console

  manager$ ssh hypervisorA
  hypervisorA$

* jump in ``nova_ssh`` container as user ``nova``

.. code-block:: console

  hypervisorA$ docker exec -it -u nova nova_ssh
  ()[nova@hypervisorA ~]$

* you can jump to ``my_ip`` of ``nova.conf`` of hypervisorB

.. code-block:: console

  ()[nova@hypervisorA ~]$ ssh <hypervisorB-my_ip>

* or copy/move instance images

.. code-block:: console

  ()[nova@hypervisorA ~]$ scp /var/lib/nova/instances/<UUID>/disk <hypervisorB-my_ip>:/var/lib/nova/instances/<UUID>/disk
