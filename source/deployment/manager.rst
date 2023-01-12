============
Manager node
============

.. note::

   Execute the following commands on the seed node. Execute the commands within
   the manager environment (``cd environments/manager``) of the configuration
   repository.

The manager node is used to manage all other nodes of the environment. The use
of a dedicated system is recommended. In many environments, one of the
controller nodes is used as the manager node.

You can use a different folder location for the virtual environment that will be
created by setting the environment variable ``VENV_PATH``. This is required for
example if your current folder path contains blank characters.

Various Ansible configurations can be adjusted via environment variables.

* To query the password for using ``sudo``:

  .. code-block:: shell

     ANSIBLE_BECOME_ASK_PASS=True

* If ``secrets.yml`` files are encrypted with Ansible Vault, let Ansible prompt
  for the password by using:

  .. code-block:: shell

     ANSIBLE_ASK_VAULT_PASS=True

An overview with all parameters can be found at
http://docs.ansible.com/ansible/devel/reference_appendices/config.html#environment-variables.

It is possible to manage more than one manager. In this case it may be useful
to work with --limit.

If you get the error message ``ERROR! the playbook: osism.manager.keypair could not be found``
(or similar) with one of the following commands, the installed Ansible version is too old.
In this case the local ``.venv`` directory is deleted and then the script is executed again.

If another Ansible installation is used on the seed system instead of the local
``.venv`` directory, this installation must be updated accordingly.

Creation of the operator user
=============================

The *operator user* is created on each system. It is used as a service account
for OSISM. All Docker containers run with this user. Ansible also uses this
user to access the systems. Commands on the manager node need to be run as
this user.

.. code-block:: console

   ANSIBLE_USER=ubuntu ./run.sh operator

* If a password is required to login to the manager node,
  ``ANSIBLE_ASK_PASS=True`` must be set.

* If an SSH key is required to login to the manager node, the key has to be
  added on the manager node to ``~/.ssh/authorized_keys`` in the home directory
  of the user specified as ``ANSIBLE_USER``.

* If the error ``ERROR! Attempting to decrypt but no vault secrets found`` occurs,
  ``ANSIBLE_ASK_VAULT_PASS=True`` has to be set.

* If the error ``/bin/sh: 1: /usr/bin/python: not found`` occurs, Python has to
  be installed on the manager node by executing:

  .. code-block:: console

     ANSIBLE_USER=ubuntu ./run.sh python3

* To verify the creation of the operator user, use the private key file
  ``id_rsa.operator``. Make sure you purge all keys from ssh-agent identity
  cache using ``ssh-add -D``. You can print the list using ``ssh-add -l``. The
  list should be empty.

  .. code-block:: console

     ssh-add -D
     ssh -o IdentitiesOnly=yes -i environments/manager/id_rsa.operator dragon@testbed-manager

* If you receive the following error message ``ssh: Too many authentication failures``
  set ``ANSIBLE_SSH_ARGS`` environment variable to use only the operator ssh key
  for authentication.

  .. code-block:: console

     export ANSIBLE_SSH_ARGS="-o IdentitiesOnly=yes"

* The warning message ``[WARNING]: running playbook inside collection osism.manager``
  can be ignored

* If Ansible Vault is used, let Ansible ask for the Vault password:

  .. code-block:: shell

     export ANSIBLE_ASK_VAULT_PASS=True

* A typical call to create the *operator user* looks like this:

  .. code-block:: console

     ANSIBLE_BECOME_ASK_PASS=True \
     ANSIBLE_ASK_VAULT_PASS=True \
     ANSIBLE_ASK_PASS=True \
     ANSIBLE_USER=ubuntu \
     ./run.sh operator

Configuration of the network
============================

.. note::

   Most of the parameters required for Ansible (``ANSIBLE_BECOME_ASK_PASS``, ``ANSIBLE_ASK_PASS``,
   ``ANSIBLE_USER``, ..) in the previous step are no longer necessary. If Ansible Vault is used,
   however, ``ANSIBLE_ASK_VAULT_PASS`` must still be set.

   To prevent recurring installation of Ansible Collections, ``export INSTALL_ANSIBLE_ROLES=False``
   can be used.

* The network configuration, already present on a system should be backuped before
  this step.

  .. code-block:: console

    ./run.sh network

* Upon completion of the network configurtion, a system reboot should be
  performed to ensure the configuration is functional and reboot safe. Since
  network services are not restarted automatically, later changes to the network
  configuration are not effective without a manual apply of the network
  configuration or reboot of the nodes.

  .. code-block:: console

     ./run.sh reboot

Bootstrap
=========

.. note::

   Most of the parameters required for Ansible (``ANSIBLE_BECOME_ASK_PASS``, ``ANSIBLE_ASK_PASS``,
   ``ANSIBLE_USER``, ..) in the previous step are no longer necessary. If Ansible Vault is used,
   however, ``ANSIBLE_ASK_VAULT_PASS`` must still be set.

   To prevent recurring installation of Ansible Collections, ``export INSTALL_ANSIBLE_ROLES=False``
   can be used.

* Bootstrap the manager node:

  .. code-block:: console

     ./run.sh bootstrap

* Reboot the manager node afterwards to ensure changes are boot safe:

  .. code-block:: console

     ./run.sh reboot

* Deploy the configuration repository on the manager node:

  .. code-block:: console

     ./run.sh configuration

* Deploy the traefik service:

  .. code-block:: console

     ./run.sh traefik

* Deploy the netbox service:

  .. code-block:: console

     ./run.sh netbox

* Deploy the manager service:

  .. code-block:: console

     ./run.sh manager

**Ready. The manager is now prepared and you can continue with the bootstrap of the other nodes.**
