=========
OpenStack
=========

Prepare OpenStack environment
=============================

For the verification of the OpenStack services it is necessary to prepare the OpenStack enviornment in the configuration repository.
The ``clouds.yml`` file should be adapted accordingly.

.. code-block:: yaml

   ---
   clouds:
     testbed:
       auth:
         username: testbed
         project_name: testbed
        auth_url: https://api-1.betacloud.io:5000/v3
        project_domain_name: default
        user_domain_name: default
      identity_api_version: 3
      verify: false

It is not recommended to store passwords in plain text in the confiugration repository. The password should be stored in a ``secure.yml`` file and encrypted.

* https://docs.openstack.org/os-client-config/latest/user/configuration.html#splitting-secrets

.. code-block:: yaml

   ---
   clouds:
     testbed:
       auth:
         password: password

A project ``testbed`` and a user ``testbed`` are to be created accordingly.

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

Glance
======

.. code-block:: shell

   $ dd if=/dev/urandom of=/opt/configuration/environments/openstack/random.img bs=1M count=100
   $ openstack --os-cloud testbed image create --file /configuration/random.img random
   +------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | Field            | Value                                                                                                                                   |
   +------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | checksum         | f936234a5e7662792086365e1483a0b1                                                                                                        |
   | container_format | bare                                                                                                                                    |
   | created_at       | 2018-01-15T12:14:52Z                                                                                                                    |
   | disk_format      | raw                                                                                                                                     |
   | file             | /v2/images/c65f20fb-e693-444f-926c-6c5b7861639c/file                                                                                    |
   | id               | c65f20fb-e693-444f-926c-6c5b7861639c                                                                                                    |
   | min_disk         | 0                                                                                                                                       |
   | min_ram          | 0                                                                                                                                       |
   | name             | random                                                                                                                                  |
   | owner            | a3a35b63df1941ba9133897f0e89eb5b                                                                                                        |
   | properties       | locations='[{u'url': u'rbd://815d7241-e7e1-4eee-855d-a9c54750c1bc/images/c65f20fb-e693-444f-926c-6c5b7861639c/snap', u'metadata': {}}]' |
   | protected        | False                                                                                                                                   |
   | schema           | /v2/schemas/image                                                                                                                       |
   | size             | 104857600                                                                                                                               |
   | status           | active                                                                                                                                  |
   | tags             |                                                                                                                                         |
   | updated_at       | 2018-01-15T12:14:56Z                                                                                                                    |
   | virtual_size     | None                                                                                                                                    |
   | visibility       | shared                                                                                                                                  |
   +------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. code-block:: shell

   $ openstack --os-cloud admin image list
   +--------------------------------------+--------+--------+
   | ID                                   | Name   | Status |
   +--------------------------------------+--------+--------+
   | c65f20fb-e693-444f-926c-6c5b7861639c | random | active |
   +--------------------------------------+--------+--------+

.. code-block:: shell

   $ rbd list images
   c65f20fb-e693-444f-926c-6c5b7861639c

.. code-block:: shell

   $ rbd info c65f20fb-e693-444f-926c-6c5b7861639c -p images
   rbd info c65f20fb-e693-444f-926c-6c5b7861639c -p images
   rbd image 'c65f20fb-e693-444f-926c-6c5b7861639c':
           size 102400 kB in 13 objects
           order 23 (8192 kB objects)
           block_name_prefix: rbd_data.3ba4238e1f29
           format: 2
           features: layering, exclusive-lock, object-map, fast-diff, deep-flatten
           flags:

.. code-block:: shell

   $ rm /opt/configuration/environments/openstack/random.img

.. code-block:: shell

   $ openstack --os-cloud testbed image delete random

.. note::

   This image is also used in the test by Cinder. Therefore, remove this image only after successful test of Cinder.

Cinder
======

.. code-block:: shell

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
