============
Requirements
============

Services & Access
=================

All nodes:

* access to DNS and NTP servers
* access to Dockerhub
* access to official Ubuntu mirrors

.. note::

   Mirrors can be provided within the environment.

Manager node:

* access to Github
* access to Git repository server

Network
=======

.. list-table:: Required VLANs
   :header-rows: 1
   :widths: 7 10 3

   * - Name
     - Nodes
     - Optional
   * - management
     - all nodes
     - |times|
   * - internal
     - all nodes
     - |times|
   * - monitoring
     - all nodes
     - |check|
   * - tunnel
     - compute & controller nodes
     - |check|
   * - external api
     - controller nodes
     - |check|
   * - external
     - controller nodes
     - |check|
   * - provider
     - compute & controller nodes
     - |check|
   * - storage frontend
     - all nodes that require access to the storage
     - |times|
   * - storage backend
     - storage nodes
     - |times|

Hardware
========
