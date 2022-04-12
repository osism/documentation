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

.. _nova-console-spice:

NoVNC or Spicehtml
==================

There are two options:

* novnc (default)
* spice

The configuration switch is in ``environments/kolla/configuration.yml``

.. code-block:: console

   nova_console: novnc/spice

This change have to be done before running ``loadbalancer`` deployment. Otherwise ``reconfigure`` ``loadbalancer``.

.. code-block:: console

   osism-kolla reconfigure loadbalancer

Deploying Openstack Services
============================

The deployment of a single Openstack service is done using Kolla via the
``osism-kolla`` wrapper.

.. code-block:: console

   $ osism-kolla deploy SERVICE

Depending on the available bandwidth, it may be a good idea to pull the Docker
images in advance prior to deployment. This can be done with ``osism-kolla pull SERVICE``.
Please also note, that you might encounter session timeouts as the system hardening role
enforces these. To prevent logouts push SPACE sometimes or use a multiplexer like
``screen`` or ``tmux``.

.. _deploymentservicesopenstackinfrastructure:

Infrastructure components
=========================

* memcached
* mariadb
* rabbitmq
* redis

Networking
==========

* openvswitch
* ovn (optional)

Storage
=======

* iscsi (optional)
* multipathd (optional)

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

