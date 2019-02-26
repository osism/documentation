=====
Kolla
=====

Execute the following commands on the manager node.

.. code-block:: console

   $ osism-kolla deploy ROLE

Infrastructure
==============

* memcached
* mariadb
* rabbitmq
* redis (>= ``pike``, required by Mistral)

.. code-block:: console

   $ osism-infrastructure helper --tags phpmyadmin

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

Client
======

.. code-block:: console

   $ osism-infrastructure helper --tags openstackclient
