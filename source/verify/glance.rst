======
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
