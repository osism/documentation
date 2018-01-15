======
Cinder
======

.. code-block: shell

   $ openstack --os-cloud testbed volume create --size 10 testing
   +---------------------+--------------------------------------+
   | Field               | Value                                |
   +---------------------+--------------------------------------+
   | attachments         | []                                   |
   | availability_zone   | internal                             |
   | bootable            | false                                |
   | consistencygroup_id | None                                 |
   | created_at          | 2018-01-15T12:54:14.713970           |
   | description         | None                                 |
   | encrypted           | False                                |
   | id                  | cc49acac-300c-4861-856e-417ea67787f2 |
   | migration_status    | None                                 |
   | multiattach         | False                                |
   | name                | testing                              |
   | properties          |                                      |
   | replication_status  | None                                 |
   | size                | 10                                   |
   | snapshot_id         | None                                 |
   | source_volid        | None                                 |
   | status              | creating                             |
   | type                | None                                 |
   | updated_at          | None                                 |
   | user_id             | ddac12227a2540ea97fa4e1db5a651da     |
   +---------------------+--------------------------------------+

   $ openstack --os-cloud testbed volume list
   +--------------------------------------+--------------+-----------+------+-------------+
   | ID                                   | Display Name | Status    | Size | Attached to |
   +--------------------------------------+--------------+-----------+------+-------------+
   | cc49acac-300c-4861-856e-417ea67787f2 | testing      | available |   10 |             |
   +--------------------------------------+--------------+-----------+------+-------------+

   $ openstack --os-cloud testbed volume delete testing

.. code-block:: shell

   $ openstack --os-cloud admin image list
   +--------------------------------------+--------+--------+
   | ID                                   | Name   | Status |
   +--------------------------------------+--------+--------+
   | c65f20fb-e693-444f-926c-6c5b7861639c | random | active |
   +--------------------------------------+--------+--------+

   $ openstack --os-cloud testbed volume create --image random --size 10 testing-glance
   [...]

   $ openstack --os-cloud testbed volume show testing-glance
   [...]
   | volume_image_metadata          | {u'container_format': u'bare', u'min_ram': u'0', u'disk_format': u'raw', u'image_name': u'random', u'image_id': u'c65f20fb-e693-444f-926c-6c5b7861639c', u'checksum': u'f936234a5e7662792086365e1483a0b1', u'min_disk': u'0', u'size': u'104857600'} |
   [...]

   $ openstack --os-cloud testbed volume delete testing-glance
