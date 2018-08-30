============
Manager node
============

.. note::

   Run the commands on the seed node. Execute the commands within the
   manager environment (``cd environments/manager``).

.. note::

   You can use a different folder location for the virtual environment that will be created by setting
   the environment variable ``VENV_PATH``. This is required for example if your current folder path
   contains blank characters.

.. note::

   Various Ansible configurations can be adjusted via environment variables.

   For example, to query the password for using ``sudo``, add ``ANSIBLE_BECOME_ASK_PASS=True``.

   If ``secrets.yml`` files are encrypted with Ansible Vault, ``ANSIBLE_ASK_VAULT_PASS=True`` is added.

   http://docs.ansible.com/ansible/devel/reference_appendices/config.html#environment-variables

* Creation of the necessary operator user

.. note::

   If at the beginning the login with a password is required, ``ANSIBLE_ASK_PASS=True`` must be set.

.. note::

   If at the beginning the login with an SSH key is required, the key has to be added on the manager node to ``authorized_keys`` of
   the user specified in ``ANSIBLE_USER``.

.. code-block:: console

   $ ANSIBLE_USER=ubuntu ./run.sh operator

.. note::

   A typical call to create the operator user looks like this.

   .. code-block:: console

      $ ANSIBLE_BECOME_ASK_PASS=True ANSIBLE_ASK_VAULT_PASS=True ANSIBLE_ASK_PASS=True ANSIBLE_USER=ubuntu ./run.sh operator

.. note::

   If the error ``/bin/sh: 1: /usr/bin/python: not found`` occurs, Python must first be installed on
   the manager node.

   .. code-block:: console

      $ ANSIBLE_USER=ubuntu ./run.sh python

.. note::

   To verify the creation of the operator user, use the private key file ``id_rsa.operator``.

   .. code-block:: console

      $ ssh -i id_rsa.operator dragon@10.49.20.10


* Configuration of the network

.. note::

   The network configuration already present on a system should be saved before this step.

.. note::

   Upon completion of this step, a system reboot should be performed to ensure that the configuration is functional and reboot secure. Since network services are not restarted automatically, later changes to the network configuration are not effective without a manual restart of the network service or reboot of the nodes.

.. code-block:: console

   $ ./run.sh network
   $ ./run.sh reboot

* Bootstrap of the node

.. code-block:: console

   $ ANSIBLE_ASK_VAULT_PASS=true ./run.sh bootstrap

.. note::

   If the manager node cannot access a hardware clock, you can deactivate hardware clock synchronisation.

   * ``environments/manager/host_vars/<hostname>.yml``

   .. code-block:: yaml

      ##########################
      # other
      systohc_common: false

.. note::

   After the bootstrap check if a reboot is required by checking if the file
   ``/var/run/reboot-required`` exists.

* Transfer configuration repository

.. code-block:: console

   $ ANSIBLE_ASK_VAULT_PASS=true ./run.sh configuration

* Deployment of necessary services

.. code-block:: console

   $ ANSIBLE_ASK_VAULT_PASS=true ./run.sh manager

.. note::

   To cleanup created directories/files after a run set the environment variable
   ``CLEANUP=true`` or manually delete the ``roles`` and ``.venv`` directories
   as well as the ``id_rsa.operator`` file when you finished the preparations of
   the manager system.

.. note::

   Always carry out an update of the manager in this way.


Update configuration
====================

There are two possibilities to update the configuration repository on the manager node.

On the seed node change into the manager environment and use the following command. This will update the configuration repository on the manager node.

.. code-block:: console

   $ ANSIBLE_ASK_VAULT_PASS=true ./run.sh configuration

On the manager node use the following command to update the configuration repository.

.. code-block:: console

   $ osism-generic configuration
