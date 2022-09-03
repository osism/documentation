=======
Manager
=======

Before starting the upgrade, the configuration repository must to be prepared.

The *OSISM* version must to be set to the new version.

Set the new manager version in ``environments/manager/configuration.yml``.

.. code-block:: yaml

   manager_version: 3.2.0

Create a temporary Python virtual environment for executing ``gilt`` (only
required if ``gilt`` is not already usable).

.. code-block:: console

   python3 -m venv --prompt osism-upgrade .venv
   source .venv/bin/activate
   pip3 install python-gilt

Next the configuration repository has to be synchronized with the generics
repository. Run the following command from the root directory of a local
copy of the configuration repository.

.. code-block:: console

   MANAGER_VERSION=3.2.0 gilt overlay  # you have to do this 2x
   MANAGER_VERSION=3.2.0 gilt overlay

Review the changes made to the configuration repository and commit the changes.

.. code-block:: console

   git diff
   git add .
   git commit -m "Upgrade MANAGER_VERSION=3.2.0"
   git push

Finally, the manager services can be updated. This is done directly on the manager
itself.

.. code-block:: console

   osism apply configuration
   osism-update-manager

.. note::

   If encountering the following error message, while running ``osism-manager``

   ``ERROR! Attempting to decrypt but no vault secrets found``

   Place the vault password of the configuration repository into file in
   the users home folder and export the following environment variable:

.. code-block:: console

   export ANSIBLE_VAULT_PASSWORD_FILE=$HOME/vaultpass

.. note::

   It is not possible to update the manager with the old ``osism-manager manager`` command.

   The new ``osism-update-manager`` command must be used for this.

   .. code-block:: console

      $ osism-manager manager
      [WARNING]: Invalid characters were found in group names but not replaced, use -vvvv to see details
      ERROR! the role 'osism.manager' was not found in /ansible/roles:/ansible/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/ansible

      The error appears to be in '/ansible/manager-manager.yml': line 6, column 5, but may
      be elsewhere in the file depending on the exact syntax problem.

      The offending line appears to be:

        roles:
        - role: osism.manager
          ^ here
