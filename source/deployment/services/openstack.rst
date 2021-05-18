=========
OpenStack
=========

Clients
=======

* OpenStackClient (aka OSC) is a command-line client for OpenStack that brings the command set for Compute,
  Identity, Image, Object Storage and Block Storage APIs together in a single shell with a uniform command
  structure.

  .. code-block:: console

     $ osism-infrastructure openstackclient

* phpMyAdmin is a free software tool written in PHP, intended to handle the administration of MySQL over
  the Web.

  .. code-block:: console

     $ osism-infrastructure phpmyadmin

.. contents::
   :depth: 2

Deploying Openstack Services
============================

The deployment of a single Openstack service is done using Kolla via the
``osism-kolla`` wrapper.

.. code-block:: console

   $ osism-kolla deploy SERVICE

Depending on the available bandwidth, it may be a good idea to pull the Docker
images in advance prior to deployment. This can be done with ``osism-kolla pull SERVICE``.

.. _deploymentservicesopenstackinfrastructure:

Infrastructure
==============

* memcached
* mariadb
* rabbitmq
* redis

Networking
==========

* openvswitch

Storage
=======

* iscsi (optional)
* multipath (optional)

Deploy OpenStack Services
=========================

* keystone
* horizon
* glance
* cinder
* placement (``>= Stein``)
* nova
* neutron
* heat

Further services like Gnocchi or Ceilometer can be activated and deployed on demand.

