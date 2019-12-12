========
Networks
========

.. image:: /images/network-schema.png

.. list-table:: Required networks
   :header-rows: 1
   :widths: 7 10 3 3 3

   * - Name
     - Nodes
     - MTU
     - Optional
     - Routed
   * - Management
     - all nodes
     - 1500
     - |times|
     - |check|
   * - Internal
     - all nodes
     - 1500
     - |times|
     - |times|
   * - Tunnel
     - compute & network nodes
     - 1500
     - |check|
     - |times|
   * - Migration
     - compute nodes
     - 1500
     - |check|
     - |times|
   * - External API
     - controller nodes
     - 1500
     - |check|
     - |question|
   * - External Networks
     - network nodes
     - 1500
     - |check|
     - |check|
   * - Provider Networks
     - compute & network nodes
     - 1500
     - |check|
     - |question|
   * - Ceph Frontend
     - all nodes that require access to the storage
     - 9000
     - |times|
     - |times|
   * - Ceph Backend
     - storage nodes
     - 9000
     - |times|
     - |times|
   * - Monitoring
     - all nodes
     - 1500
     - |check|
     - |times|
