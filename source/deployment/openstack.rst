=========
OpenStack
=========

.. note:: Run this command on the manager node.

.. code-block:: console

   $ osism-kolla deploy ROLE

Shared services
===============

* memcached
* mariadb
* rabbitmq
* redis (>= ``pike``, required by Mistral)

Networking
==========

* openvswitch (>= ``pike``)

Storage
=======

* iscsid (optional)
* multipathd (optional)

OpenStack
=========

* keystone
* horizon
* glance
* cinder
* nova
* neutron
* heat
