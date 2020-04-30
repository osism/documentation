==========
Node types
==========

.. contents::
   :local:

.. image:: /images/network-schema.png

Seed node
=========

The seed node is required to build the manager node at the beginning. It is then no longer needed.

The local workstation can be used as a seed node. Often the manually installed manager node is
also used as seed node.

Manager node
============

The manager node is the central entry point into the environment for deployment and administration.

All services necessary for deployment and administration are placed on this node. This includes the
individual Ansible containers and clients for OpenStack and Ceph.

Infrastructure node
===================

In small environments, services such as mirror and monitoring are usually placed on the manager node.

In larger environments it may be makes sense to introduce dedicated infrastructure nodes for the
mirror and monitoring services.

The bare-metal provisioning service (Cobbler) can also be placed on a dedicated node.

Controller node
===============

Services such as MariaDB, Elasticsearch, HAProxy, APIs etc. are placed on the controller node.
Three controller nodes are used in most environments.

In small environments, one of the controller nodes can also be used as a manager node.

Network node
============

The use of dedicated network nodes is not necessary, but recommended. Neutron's L3 and DHCP agents
will be placed on this node.

Compute node
============

The compute nodes are used for the virtual systems.

Compute nodes and storage nodes are combined in a hyperconvergedinfrastructure. They are then
referred to as resource node.

Storage node
============

The storage nodes are used for Ceph.

Compute nodes and storage nodes are combined in a hyperconvergedinfrastructure. They are then
referred to as resource node.
