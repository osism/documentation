=======
Manager
=======

The following parameters are adjusted accordingly in the configuration repository.

.. code-block:: yaml
   :caption: environments/manager/configuration.yml

   ##########################
   # versions

   ceph_manager_version: 2019.4.0
   kolla_manager_version: 2019.4.0
   osism_manager_version: 2919.4.0

Afterwards ``environments/manager`` is synchronized with the master configuration
repository.

.. code-block:: console

   MANAGER_VERSION=2019.4.0 gilt overlay

The directories ``environments/manager/roles`` and ``environments/manager/.venv`` are
deleted on the manager.

.. code-block:: console

   rm -rf /opt/configuration/environments/manager/roles
   rm -rf /opt/configuration/environments/manager/.venv

After updating the configuration repository, the manager is now updated.

.. code-block:: console

   osism-generic configuration
   osism-manager manager
