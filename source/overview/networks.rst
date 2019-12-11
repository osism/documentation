========
Networks
========

.. image:: /images/networks-and-nodes.png

.. list-table:: Required networks
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
