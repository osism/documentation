=========
OpenStack
=========

Execute the following commands on the manager node.

The deployment of a single Kolla service is done via the ``osism-kolla`` wrapper.

.. code-block:: console

   $ osism-kolla deploy ROLE

Depending on the available bandwidth, it may be a good idea to pull the Docker
images in advance prior to deployment. This can be done with ``osism-kolla pull ROLE``.

Infrastructure
==============

* memcached
* mariadb
* rabbitmq
* redis (>= ``pike``, required by Mistral & Gnocchi)

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
