============
Requirements
============

Deployment
==========

If the deployment is carried out or supervised by us, direct SSH access to the system
acting as manager is required.

Optimally, a VPN is provided via which all relevant nodes including the remote consoles
can be accessed.

Services & Access
=================

The nodes need access to some external services.

All nodes
---------

* DNS and NTP servers
* Docker Hub
* Official Ubuntu mirrors

.. note::

   * Mirrors for Docker and Ubuntu can be provided within the environment. Then access to
     Docker Hub and Ubuntu is only required from the manager.

   * If no direct access to external services is possible, the use of an HTTP proxy is
     possible.

Manager node
------------

* GitHub or an internal Git repository server (e.g. Gitlab)
* PyPI

Network
=======

VLAN based
----------

.. list-table:: Required VLANs
   :header-rows: 1
   :widths: 7 10 3 3 3

   * - Name
     - Nodes
     - MTU
     - Optional
     - Routed
   * - console
     - all nodes
     - 1500
     - |times|
     - |check|
   * - internal
     - all nodes
     - 1500
     - |times|
     - |times|
   * - tunnel
     - compute & network nodes
     - 1500
     - |check|
     - |times|
   * - migration
     - compute nodes
     - 1500
     - |check|
     - |times|
   * - external api
     - controller nodes
     - 1500
     - |check|
     - |question|
   * - external
     - network nodes
     - 1500
     - |check|
     - |check|
   * - provider
     - compute & network nodes
     - 1500
     - |check|
     - |question|
   * - storage frontend
     - all nodes that require access to the storage
     - 9000
     - |times|
     - |times|
   * - storage backend
     - storage nodes
     - 9000
     - |times|
     - |times|
   * - monitoring
     - all nodes
     - 1500
     - |check|
     - |times|

Hardware
========
