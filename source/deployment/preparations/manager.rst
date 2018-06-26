============
Manager node
============

.. note::

   Run the commands on the seed node. Execute the commands within the
   manager environment (``cd environments/manager``).

.. note::

   Various Ansible configurations can be adjusted via environment variables.

   For example, to query the password for using ``sudo``, add ``ANSIBLE_BECOME_ASK_PASS=True``.

   If ``secrets.yml`` files are encrypted with Ansible Vault, ``ANSIBLE_ASK_VAULT_PASS=True`` is added.

   http://docs.ansible.com/ansible/devel/reference_appendices/config.html#environment-variables

* Creation of the necessary operator user

.. note::

   If at the beginning the login with a password is required, ``ANSIBLE_ASK_PASS=True`` must be set.

.. code-block:: console

   $ ANSIBLE_USER=ubuntu ./run.sh operator

.. note::

   If the error ``/bin/sh: 1: /usr/bin/python: not found`` occurs, Python must first be installed on
   the manager node.

   .. code-block:: console

      $ ANSIBLE_USER=ubuntu ./run.sh python

* Configuration of the network

.. note::

   The network configuration already present on a system should be saved before this step.

.. note::

   Upon completion of this step, a system reboot should be performed to ensure that the configuration is functional and reboot secure.

.. code-block:: console

   $ ./run.sh network

* Bootstrap of the node

.. code-block:: console

   $ ./run.sh bootstrap

* Transfer configuration repository

.. code-block:: console

   $ ./run.sh configuration

* Deployment of necessary services

.. code-block:: console

   $ ./run.sh manager

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

   $ ./run.sh configuration

On the manager node use the following command to update the configuration repository.

.. code-block:: console

   $ osism-generic configuration
