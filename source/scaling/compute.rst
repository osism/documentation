=============
Compute nodes
=============

.. contents::
   :local:

Adding a compute node
=====================

.. code-block:: console

   osism-kolla deploy openvswitch -l testbed-node-2.osism.local
   osism-kolla deploy neutron -l testbed-node-2.osism.local
   osism-kolla deploy nova -l testbed-node-2.osism.local
