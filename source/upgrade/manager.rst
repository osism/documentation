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

Notes
=====

2019.4.0
--------

The ARA 1.x introduced in 2019.4.0 is unfortunately not downward compatible to ARA 0.x.

Therefore, when upgrading the manager to 2019.4.0, the ARA database must be reset.

The following steps must be performed before upgrading the manager.

.. code-block:: console

   docker rm -f manager_database_1
   docker volume rm manager_mariadb

The ARA configuration parameters must be removed from all ``ansible.cfg`` files.
These are no longer necessary. Usually these parameters are only available in
``environments/ansible.cfg``.

.. code-block:: ini

   [ara]
   database = mysql+pymysql://ara:password@database/ara

The new secret ``ara_password`` is added to the ``environments/secrets.yml`` file.

.. code-block:: yaml

   # manager

   ara_password: password
