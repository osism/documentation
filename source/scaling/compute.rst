============
Compute node
============

.. contents::
   :local:

Adding a compute node
=====================

.. code-block:: console

   osism-kolla deploy openvswitch -l testbed-node-2.osism.local
   osism-kolla deploy neutron -l testbed-node-2.osism.local
   osism-kolla deploy nova -l testbed-node-2.osism.local

Storage (optional)
------------------

If multipath is configured in file ``environements/kolla/configuration.yml`` at
``enable_multipathd: yes``, the ``multipath`` role needs to be deployed as
well:

.. code-block:: console

   osism-kolla deploy multipath -l testbed-node-2.osism.local

If Cinder is configured to deliver volumes via LVM2/iSCSI in the configuration
repository in file ``environements/kolla/configuration.yml`` at
``enable_cinder_backend_lvm: yes``, the ``iscsi`` role needs to be deployed as
well:

.. code-block:: console

   osism-kolla deploy iscsi -l testbed-node-2.osism.local
