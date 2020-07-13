===============
Synchronisation
===============

The configuration repository, created using *cookiecutter* needs to be
synchronized regularly with https://github.com/osism/cfg-generics to obtain any
updates.

``cfg-generics`` contains in particular the directory ``environments/manager``,
which is needed to initially build the manager node, and is updated on a regular
basis.

If there are errors when rebuilding an environment, such as a missing Ansible
role, you should first try synchronizing before time-consuming debugging.

The value for ``MANAGER_VERSION`` is stored in
``environments/manager/configuration.yml`` in the ``osism_manager_version``
parameter.

Synchronization has to be performed when updating to a new version. In this
case, ``MANAGER_VERSION`` will be set to the new version.

The following commands are executed within the root directory of the
configuration repository.

.. code-block:: console

   virtualenv -p python3 .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   MANAGER_VERSION=2019.3.0 gilt overlay

After synchronization, check for changes in the configuration repository.

.. code-block:: console

   git status

If there are any changes, review and commit them.

.. code-block:: console

   git diff
   git add .
   git commit
