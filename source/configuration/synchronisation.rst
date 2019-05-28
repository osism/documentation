===============
Synchronisation
===============

The configuration repository must be regularly synchronized with https://github.com/osism/cfg-master.

``cfg-master`` contains in particular ``environments/manager``, which is needed to build the manager
node for new environments.

If there are errors when rebuilding an environment, such as a missing Ansible role, you should first
try synchronizing before time-consuming debugging.

The value for ``MANAGER_VERSION`` is stored in ``environments/manager/configuration.yml`` in the
``osism_manager_version`` parameter.

Synchronization must also be performed when updating to a new version. In this case, ``MANAGER_VERSION``
is set to the new version accordingly.

The following commands are executed within the root directory of the respective configuration
repository.

.. code-block:: console

   $ virtualenv -p python3 .venv
   $ pip install -r requirements.txt
   $ MANAGER_VERSION=2019.3.0 gilt overlay

After synchronization, check changes with ``git status`` and commit them.
