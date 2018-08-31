=====
Kolla
=====

.. note:: Run this command on the manager node.

.. code-block:: console

   $ osism-kolla deploy ROLE

Infrastructure
==============

* memcached
* mariadb
* rabbitmq
* redis (>= ``pike``, required by Mistral)

Networking
==========

* openvswitch (>= ``pike``)

Storage
=======

* iscsi (optional)
* multipath (optional)

OpenStack
=========

* keystone
* horizon
* glance
* cinder
* nova
* neutron
* heat

Clients
=======

.. code-block:: console

   $ osism-infrastructure helper --tags openstackclient
   $ osism-infrastructure helper --tags phpmyadmin
