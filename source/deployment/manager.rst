=======================
Manager Node Deployment
=======================

.. contents::
   :depth: 2

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

* to query the password for using ``sudo``:

  .. code-block:: shell

    ANSIBLE_BECOME_ASK_PASS=True

* if ``secrets.yml`` files are encrypted with Ansible Vault, let Ansible prompt
  for the password by using:

  .. code-block:: shell

    ANSIBLE_ASK_VAULT_PASS=True

* set the password file location (password will be in cleartext!)

  .. code-block:: shell

    ANSIBLE_VAULT_PASSWORD_FILE=../../secrets/vaultpass

An overview with all parameters can be found at
http://docs.ansible.com/ansible/devel/reference_appendices/config.html#environment-variables.

Manager Node Initialization
===========================

.. note::

  It is possible to manage more than one manager. In this case it may be useful
  to work with --limit.

.. note::

   If you get the following error message (or similar) with the following commands,
   the installed Ansible version is too old. In this case the local ``.venv`` directory
   is deleted and then the script is executed again.

   If another Ansible installation is used on the seed system instead of the local
   ``.venv`` directory, this installation must be updated accordingly.

   .. code-block:: none

      ERROR! the playbook: osism.manager.keypair could not be found
      ERROR! the playbook: osism.manager.manager could not be found

Creation of the operator user
-----------------------------

.. code-block:: console

  ANSIBLE_USER=ubuntu ./run.sh operator

.. note::

  The *operator user* is created on each system. It is used as a service account
  for OSISM. All Docker containers run with this user. Ansible also uses this
  user to access the systems. Commands on the manager node need to be run as
  this user!

* If a password is required to login to the manager node,
  ``ANSIBLE_ASK_PASS=True`` must be set.

* If an SSH key is required to login to the manager node, the key has to be
  added on the manager node to ``~/.ssh/authorized_keys`` in the home directory
  of the user specified as ``ANSIBLE_USER``.

* If the error ``/bin/sh: 1: /usr/bin/python: not found`` occurs, Python has to
  be installed on the manager node by executing:

  .. code-block::

    ANSIBLE_USER=ubuntu ./run.sh python3

* To verify the creation of the operator user, use the private key file
  ``id_rsa.operator``. Make sure you purge all keys from ssh-agent identity
  cache using ``ssh-add -D``. You can print the list using ``ssh-add -l``. The
  list should be empty.

  .. code-block::

    ssh-add -D
    ssh -o IdentitiesOnly=yes -i environments/manager/id_rsa.operator dragon@testbed-manager

* If you receive the following error message:

  .. code-block:: console

    ssh: Too many authentication failures

  set ``ANSIBLE_SSH_ARGS`` environment variable to use only the operator ssh key
  for authentication.

  .. code-block:: console

    export ANSIBLE_SSH_ARGS="-o IdentitiesOnly=yes"

* A typical call to create the *operator user* looks like this:

  .. code-block:: console

    ANSIBLE_BECOME_ASK_PASS=True \
    ANSIBLE_ASK_VAULT_PASS=True \
    ANSIBLE_ASK_PASS=True \
    ANSIBLE_USER=ubuntu \
    ./run.sh operator

.. warning::

  If the *operator user* was already created when the operating system was
  provisioned, ``./run.sh operator`` must still be executed. ``ANSIBLE_USER``
  should be set to a user with sudo rights and different from the
  *operator user*.

  The UID and GID of the *operator user* need to be ``45000``. Execute the
  following commands as *root* user on the manger node:

  .. code-block:: console

    usermod -u 45000 dragon
    groupmod -g 45000 dragon

    chgrp dragon /home/dragon/
    chown dragon /home/dragon/

    find /home/dragon -group 1000 -exec chgrp -h dragon {} \;
    find /home/dragon -user 1000 -exec chown -h dragon {} \;

* If Ansible Vault is used, direct Ansible to prompt for the Vault password:

  .. code-block:: shell

    export ANSIBLE_ASK_VAULT_PASS=True

  or the password file location can be exported
  (password will be in cleartext!):

  .. code-block:: shell

    export ANSIBLE_VAULT_PASSWORD_FILE=../../secrets/vaultpass

Configuration of the network
----------------------------

* The network configuration, already present on a system should be saved before
  this step.

* Currently we are still using ``/etc/network/interfaces``. Files below
  ``/etc/netplan`` will be moved to ``X.unused``.

* Some configuration examples for ``inventory/host_vars/<nodeX>`` can be found in
  :ref:`host-vars-network-config-examples`

.. code-block:: console

  ./run.sh network

* Upon completion of the network configurtion, a system reboot should be
  performed to ensure the configuration is functional and reboot safe. Since
  network services are not restarted automatically, later changes to the network
  configuration are not effective without a manual restart of the network
  service or reboot of the nodes.

* A reboot is performed to activate and test the network configuration. The
  reboot must be performed before the bootstrap is performed.

  .. code-block:: console

     ./run.sh reboot

Bootstrap of the manager node
-----------------------------

  .. code-block:: console

    ./run.sh bootstrap

Reboot the manager node afterwards to ensure changes are boot safe:

  .. code-block:: console

    ./run.sh reboot

Deploy the configuration repository on the manager node:

  .. code-block:: console

     ./run.sh configuration

If the manager node does not have access to the server hosting the configuration
repository, it can be copied manually with rsync from the seed node to the
manager node. First clone the configuration repository, to ensure the repository
contains no secrets in plain text.

  .. code-block:: console

     git clone cfg-customer cfg-customer.rsync
     rsync -Paz -e "ssh -o IdentitiesOnly=yes -i cfg-customer/secrets/id_rsa.operator" cfg-customer.rsync/ dragon@testbed-manager:/opt/configuration/


If you want to import the inventory into Netbox, first deploy Netbox.

Netbox need to be enabled first in the file
``environments/manager/configuration.yml``:

  .. code-block:: yaml

    netbox_enable: true

Then deploy Netbox:

  .. code-block:: console

    ./run.sh netbox

Deploy the manager services:

  .. code-block:: console

    ./run.sh manager
