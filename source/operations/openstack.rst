=========
OpenStack
=========

Show all instances on a specific compute node
=============================================

.. code-block:: console

   openstack --os-cloud admin server list --all-projects --host 54-02

Show all running instances
==========================

.. code-block:: console

   openstack --os-cloud admin server list --all-projects --power-state running
