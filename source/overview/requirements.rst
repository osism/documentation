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

All nodes:

* access to DNS and NTP servers
* access to Dockerhub
* access to official Ubuntu mirrors
* access to PyPI

.. note::

   Mirrors can be provided within the environment.

Manager node:

* access to GitHub or an internal Git repository server (e.g. Gitlab)

Network
=======

.. list-table:: Required VLANs
   :header-rows: 1
   :widths: 7 10 3 3

   * - Name
     - Nodes
     - Optional
     - Routed
   * - management
     - all nodes
     - |times|
     - |check|
   * - internal
     - all nodes
     - |times|
     - |times|
   * - monitoring
     - all nodes
     - |check|
     - |times|
   * - tunnel
     - compute & controller nodes
     - |check|
     - |times|
   * - external api
     - controller nodes
     - |check|
     - |question|
   * - external
     - controller nodes
     - |check|
     - |check|
   * - provider
     - compute & controller nodes
     - |check|
     - |question|
   * - storage frontend
     - all nodes that require access to the storage
     - |times|
     - |times|
   * - storage backend
     - storage nodes
     - |times|
     - |times|

Hardware
========
