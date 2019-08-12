===============
Synchronisation
===============

The configuration repository, created using cookiecutter has to be synchronized
regularly with https://github.com/osism/cfg-master to obtain any updates.

``cfg-master`` contains in particular ``environments/manager``, which is needed
to initially build the manager node, and is updated on a regular basis.

If there are errors when rebuilding an environment, such as a missing Ansible role, you should first
try synchronizing before time-consuming debugging.

The value for ``MANAGER_VERSION`` is stored in ``environments/manager/configuration.yml`` in the
``osism_manager_version`` parameter.

Synchronization must also be performed when updating to a new version. In this case, ``MANAGER_VERSION``
is set to the new version accordingly.

The following commands are executed within the root directory of the respective configuration
repository.

.. code-block:: console

   virtualenv -p python3 .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   MANAGER_VERSION=2019.3.0 gilt overlay

After synchronization, check for changes in the configuration repository.

.. code-block:: console

   git status

If there are changes, review and commit them.

.. code-block:: console

   git diff
   git add .
   git commit
