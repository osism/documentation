=========
OpenStack
=========

.. contents::
   :local:

OpenStack Client Preparations
=============================

For the verification of the OpenStack services it is necessary to change to the
directory ``/opt/configuration/environments/openstack`` on the manager node.

The ``openstack-client`` will use ``clouds.yml`` and ``secure.yml`` to read the
project information and credentials.

.. code-block:: yaml

   ---
   clouds:
     admin:
       auth:
         username: admin
         project_name: admin
        auth_url: https://api-1.betacloud.io:5000/v3
        project_domain_name: default
        user_domain_name: default
      identity_api_version: 3
      verify: false

Create the file ``secure.yml`` and set the ``keystone_admin_password`` from
``environments/kolla/secrets.yml`` as ``password``.

.. code-block:: yaml

   ---
   clouds:
     admin:
       auth:
         password: password

It is not recommended to store passwords in plain text in the confiugration
repository.

* https://docs.openstack.org/os-client-config/latest/user/configuration.html#splitting-secrets

Keystone Test
=============

.. code-block:: console

   $ openstack --os-cloud admin token issue
   +------------+-------------------------------+
   | Field      | Value                         |
   +------------+-------------------------------+
   | expires    | 2018-01-16T10:05:59+0000      |
   | id         | gAAAAABaXH0HNIsZUXKGYBPl[...] |
   | project_id | de8299637be6486f9dd0d51c[...] |
   | user_id    | e2cf7b56b0e647e79f25c6b0[...] |
   +------------+-------------------------------+

Other tests are the following commands.

* ``openstack --os-cloud admin catalog list``
* ``openstack --os-cloud admin endpoint list``
* ``openstack --os-cloud admin domain list``
* ``openstack --os-cloud admin user list --domain default``

Glance Test
===========

.. code-block:: console

   $ dd if=/dev/urandom of=/opt/configuration/environments/openstack/random.img bs=1M count=100
   100+0 records in
   100+0 records out
   104857600 bytes (105 MB, 100 MiB) copied, 9.0766 s, 11.6 MB/s

.. code-block:: console

   $ openstack --os-cloud admin image create --file /configuration/random.img random
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

.. code-block:: console

   $ openstack --os-cloud admin image list
   +--------------------------------------+--------+--------+
   | ID                                   | Name   | Status |
   +--------------------------------------+--------+--------+
   | c65f20fb-e693-444f-926c-6c5b7861639c | random | active |
   +--------------------------------------+--------+--------+

.. code-block:: console

   $ rbd list images
   c65f20fb-e693-444f-926c-6c5b7861639c

.. code-block:: console

   $ rbd info c65f20fb-e693-444f-926c-6c5b7861639c -p images
   rbd info c65f20fb-e693-444f-926c-6c5b7861639c -p images
   rbd image 'c65f20fb-e693-444f-926c-6c5b7861639c':
           size 102400 kB in 13 objects
           order 23 (8192 kB objects)
           block_name_prefix: rbd_data.3ba4238e1f29
           format: 2
           features: layering, exclusive-lock, object-map, fast-diff, deep-flatten
           flags

.. code-block:: console

   $ rm /opt/configuration/environments/openstack/random.img

.. note::

   This image is also used in the test by Cinder. Therefore, remove this image only after successful test of Cinder.

.. code-block:: console

   $ openstack --os-cloud admin image delete random

Cinder Test
===========

Check Ceph connection
---------------------

.. code-block:: console

   $ docker exec -ti cinder_volume ceph -k /etc/ceph/ceph.client.cinder.keyring -n client.cinder -s

Check services
--------------

.. code-block:: console

   $ openstack --os-cloud admin volume service list
   $ openstack --os-cloud admin availability zone list --volume (--long)

Empty volume
------------

.. code-block:: console

   $ openstack --os-cloud admin volume create --size 10 testing
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

.. code-block:: console

   $ openstack --os-cloud admin volume list
   +--------------------------------------+--------------+-----------+------+-------------+
   | ID                                   | Display Name | Status    | Size | Attached to |
   +--------------------------------------+--------------+-----------+------+-------------+
   | cc49acac-300c-4861-856e-417ea67787f2 | testing      | available |   10 |             |
   +--------------------------------------+--------------+-----------+------+-------------+

.. code-block:: console

   $ rbd list volumes
   volume-cc49acac-300c-4861-856e-417ea67787f2

.. code-block:: console

   $ rbd info volume-cc49acac-300c-4861-856e-417ea67787f2 -p volumes
   rbd image 'volume-cc49acac-300c-4861-856e-417ea67787f2':
         size 10240 MB in 2560 objects
         order 22 (4096 kB objects)
         block_name_prefix: rbd_data.11237a6d8d3c
         format: 2
         features: layering, exclusive-lock, object-map, fast-diff, deep-flatten
         flags:
         create_timestamp: Thu Jun 14 11:59:33 2018

.. code-block:: console

   $ openstack --os-cloud admin volume delete testing

Volume from image
-----------------

.. code-block:: console

   $ openstack --os-cloud admin image list
   +--------------------------------------+--------+--------+
   | ID                                   | Name   | Status |
   +--------------------------------------+--------+--------+
   | c65f20fb-e693-444f-926c-6c5b7861639c | random | active |
   +--------------------------------------+--------+--------+

.. code-block:: console

   $ openstack --os-cloud admin volume create --image random --size 10 testing-glance
   [...]

.. code-block:: console

   $ openstack --os-cloud admin volume show testing-glance
   [...]
   | volume_image_metadata          | {u'container_format': u'bare', u'min_ram': u'0', u'disk_format': u'raw', u'image_name': u'random', u'image_id': u'c65f20fb-e693-444f-926c-6c5b7861639c', u'checksum': u'f936234a5e7662792086365e1483a0b1', u'min_disk': u'0', u'size': u'104857600'} |
   [...]

.. code-block:: console

   $ rbd list volumes
   volume-e3b844cc-87c2-4975-b4c4-a904a7369b58

.. code-block:: console

   $ rbd info volume-e3b844cc-87c2-4975-b4c4-a904a7369b58 -p volumes
   rbd image 'volume-e3b844cc-87c2-4975-b4c4-a904a7369b58':
         size 10240 MB in 2560 objects
         order 22 (4096 kB objects)
         block_name_prefix: rbd_data.116a9daf632
         format: 2
         features: layering, exclusive-lock, object-map, fast-diff, deep-flatten
         flags:
         create_timestamp: Thu Jun 14 12:02:20 2018
         parent: images/c65f20fb-e693-444f-926c-6c5b7861639c@snap
         overlap: 102400 kB

.. code-block:: console

   $ openstack --os-cloud admin volume delete testing-glance

Neutron Test
============

Check Neutron Services
----------------------

.. code-block:: console

   $ openstack --os-cloud admin network agent list
   $ openstack --os-cloud admin router list
   $ openstack --os-cloud admin availability zone list --network --long

Open vSwitch agent
------------------

On network nodes and compute nodes with provider networks, after the initial start of
the ``neutron-openvswitch-agent`` service.

.. code-block:: console

   $ docker exec -it openvswitch_vswitchd ovs-vsctl show
   a2f9dbad-519e-4873-aea4-0719abcd9e2a
       Manager "ptcp:6640:127.0.0.1"
           is_connected: true
       Bridge br-int
           Controller "tcp:127.0.0.1:6633"
               is_connected: true
           fail_mode: secure
           Port br-int
               Interface br-int
                   type: internal
           Port patch-tun
               Interface patch-tun
                   type: patch
                   options: {peer=patch-int}
           Port int-br-ex
               Interface int-br-ex
                   type: patch
                   options: {peer=phy-br-ex}
       Bridge br-tun
           Controller "tcp:127.0.0.1:6633"
               is_connected: true
           fail_mode: secure
           Port br-tun
               Interface br-tun
                   type: internal
           Port patch-int
               Interface patch-int
                   type: patch
                   options: {peer=patch-tun}
       Bridge br-ex
           Controller "tcp:127.0.0.1:6633"
               is_connected: true
           fail_mode: secure
           Port phy-br-ex
               Interface phy-br-ex
                   type: patch
                   options: {peer=int-br-ex}
           Port br-ex
               Interface br-ex
                   type: internal
           Port "enp24s0f1"
               Interface "enp24s0f1"

Nova Test
=========

Check Nova Services
-------------------

.. code-block:: console

   $ openstack --os-cloud admin compute service list
   $ openstack --os-cloud admin hypervisor list
   $ openstack --os-cloud admin availability zone list --compute --long

Check Ceph connectivity
-----------------------

.. code-block:: console

   $ docker exec -ti nova_compute ceph -k /etc/ceph/ceph.client.nova.keyring -n client.nova -s

Create instances
----------------

.. code-block:: console

   $ openstack --os-cloud admin server create --image c65f20fb-e693-444f-926c-6c5b7861639c --flavor 4C-R8G-D10G --min 50 --max 100 test
   $ openstack --os-cloud admin server list (--long) (--all-projects)

Check libvirt
-------------

.. code-block:: console

   com1$ docker exec -it nova_libvirt virsh list (--all)

Flavor
======

Create flavor
-------------

.. code-block:: console

   $ openstack --os-cloud admin flavor create --ram 8096 --disk 10 --vcpus 4 --public 4C-R8G-D10G

.. code-block:: console

   $ openstack --os-cloud admin flavor list (--long)
   +-----------+-------------+------+------+-----------+-------+-----------+------+-------------+------------+
   | ID        | Name        |  RAM | Disk | Ephemeral | VCPUs | Is Public | Swap | RXTX Factor | Properties |
   +-----------+-------------+------+------+-----------+-------+-----------+------+-------------+------------+
   | 46b1[...] | 4C-R8G-D10G | 8096 |   10 |         0 |     4 | False     |      |      1.0    |            |
   +-----------+-------------+------+------+-----------+-------+-----------+------+-------------+------------+

Heat
====

Check Heat Services
-------------------

.. code-block:: console

   $ openstack --os-cloud admin orchestration service list
