============
Manager node
============

.. contents::
   :local:

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

Initialization
==============

.. note::

  It is possible to manage more than one manager. In this case it may be useful
  to work with --limit.

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

.. code-block:: console

  ./run.sh network

* The network configuration, already present on a system should be saved before
  this step.

* Currently we are still using ``/etc/network/interfaces``. Hence rename all
  files below ``/etc/netplan`` to ``X.unused``.

  The default file ``01-netcfg.yaml`` with the following content can remain as
  is.

  .. code-block:: yaml

    # This file describes the network interfaces available on your system
    # For more information, see netplan(5).
    network:
      version: 2
      renderer: networkd

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


Deploy the manager services:

  .. code-block:: console

    ./run.sh manager

Optional infrastructure services
================================

The deployment of these infrastructure services is optional. They are only
deployed if they are to be used.

Mirror
------

With the mirror services it is possible to store packages for Ubuntu and images
for Docker in one central location.

.. code-block:: console

  osism-infrastructure mirror

After the bootstrap of the mirror services they have to be synchronized.
Depending on the bandwidth, this process will take several hours.

.. code-block:: console

  osism-mirror images
  osism-mirror packages

import nodes from MAAS to netbox
------

If you are using netbox as your inventory and if you use canonical's MAAS for deploying your hosts,
there is a possibility to import your nodes from MAAS as source to netbox

.. code-block:: console

  osism-manager maas2netbox

At the moment the hosts are imported together with the network interfaces and the primary IPv4 will be assigned.


You have to add the credentials for accessing MAAS to ``environments/manager/secrets.yml``

.. code-block:: yaml

  maas_login_profile: '<user>'
  maas_login_url: 'http://<maas_host>:5240/MAAS/'
  maas_api_key: '<maas_api_key>'
