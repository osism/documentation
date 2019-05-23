=========
OpenStack
=========

.. contents::
   :local:

Execute the following commands on the manager node.

The deployment of a single Kolla service is done via the ``osism-kolla`` wrapper.

.. code-block:: console

   $ osism-kolla deploy SERVICE

Depending on the available bandwidth, it may be a good idea to pull the Docker
images in advance prior to deployment. This can be done with ``osism-kolla pull SERVICE``.

The facts should be updated once with ``osism-generic facts`` before starting the deployment
of the individual services.

Infrastructure
==============

* memcached
* mariadb
* rabbitmq
* redis (required by Mistral & Gnocchi)

Networking
==========

* openvswitch

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

Further services like Gnocchi or Ceilometer can be activated and deployed on demand.

Clients
=======

* OpenStackClient (aka OSC) is a command-line client for OpenStack that brings the command set for Compute,
  Identity, Image, Object Storage and Block Storage APIs together in a single shell with a uniform command
  structure.

  .. code-block:: console

     $ osism-infrastructure helper --tags openstackclient

* phpMyAdmin is a free software tool written in PHP, intended to handle the administration of MySQL over
  the Web.

  .. code-block:: console

     $ osism-infrastructure helper --tags phpmyadmin
