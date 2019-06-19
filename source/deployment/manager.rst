============
Manager node
============

.. contents::
   :local:

.. note::

   Execute the following commands on the seed node. Execute the commands within the
   manager environment (``cd environments/manager``).

The manager node is used to manage all other nodes of the environment. The use of a dedicated system
is recommended. In many environments, one of the controller nodes is used as the manager node.

You can use a different folder location for the virtual environment that will be created by setting
the environment variable ``VENV_PATH``. This is required for example if your current folder path
contains blank characters.

Various Ansible configurations can be adjusted via environment variables. For example, to query the
password for using ``sudo``, add ``ANSIBLE_BECOME_ASK_PASS=True``. If ``secrets.yml`` files are
encrypted with Ansible Vault, ``ANSIBLE_ASK_VAULT_PASS=True`` is added.

An overview with all parameters can be found at http://docs.ansible.com/ansible/devel/reference_appendices/config.html#environment-variables.

Initialization
==============

* Creation of the necessary operator user

  .. code-block:: console

     $ ANSIBLE_USER=ubuntu ./run.sh operator

  .. note::

     The so-called operator user is created on each system. It is used as a service account for OSISM.
     All Docker Containers run under this user. Ansible also uses this account to access the systems.

  * If at the beginning the login with a password is required, ``ANSIBLE_ASK_PASS=True`` must be set.
  * If at the beginning the login with an SSH key is required, the key has to be added on the manager
    node to ``authorized_keys`` of the user specified in ``ANSIBLE_USER``.
  * If the error ``/bin/sh: 1: /usr/bin/python: not found`` occurs, Python must first be installed on
    the manager node with ``ANSIBLE_USER=ubuntu ./run.sh python``.
  * To verify the creation of the operator user, use the private key file ``id_rsa.operator``:
    ``ssh -i id_rsa.operator dragon@10.49.20.10``.
  * A typical call to create the operator user looks like this.

    .. code-block:: console

       $ ANSIBLE_BECOME_ASK_PASS=True \
         ANSIBLE_ASK_VAULT_PASS=True \
         ANSIBLE_ASK_PASS=True \
         ANSIBLE_USER=ubuntu \
         ./run.sh operator

  .. warning::

     If the operator user was already created when the operating system was provisioned, this
     role must still be executed. ``ANSIBLE_USER`` is then adjusted accordingly.

     The UID and GID must also be checked. If it is not ``45000``, it must be adapted accordingly.

     .. code-block:: console

        # usermod -u 45000 dragon
        # groupmod -g 45000 dragon

        # chgrp dragon /home/dragon/
        # chown dragon /home/dragon/

        # find /home/dragon -group 1000 -exec chgrp -h dragon {} \;
        # find /home/dragon -user 1000 -exec chown -h dragon {} \;

* If Ansible Vault is used, the ``ANSIBLE_ASK_VAULT_PASS`` variable will be used accordingly

  .. code-block:: console

     $ export ANSIBLE_ASK_VAULT_PASS=True

* Configuration of the network

  .. code-block:: console

     $ ./run.sh network

  * The network configuration already present on a system should be saved before this step.
  * We are currently still using ``/etc/network/interfaces``. Therefore rename all files below ``/etc/netplan`` to ``X.unused``.
  * Upon completion of this step, a system reboot should be performed to ensure that the
    configuration is functional and reboot secure. Since network services are not
    restarted automatically, later changes to the network configuration are not effective
    without a manual restart of the network service or reboot of the nodes.
  * A reboot is performed to activate and test the network configuration.
    The reboot must be performed before the bootstrap is performed.

    .. code-block:: console

       $ ./run.sh reboot

* Bootstrap of the manager node

  .. code-block:: console

     $ ./run.sh bootstrap

* Further reboot of the manager node

  .. code-block:: console

     $ ./run.sh reboot

* Transfer configuration repository

  .. code-block:: console

     $ ./run.sh configuration

* Deployment of necessary manager services

  .. code-block:: console

     $ ./run.sh manager

Optional infrastructure services
================================

The deployment of these infrastructure services is optional. They are only deployed if they are
to be used.

Cobbler
-------

Cobbler is a Linux installation server that allows for rapid setup of network installation environments.
It glues together and automates many associated Linux tasks so you do not have to hop between lots of
various commands and applications when rolling out new systems, and, in some cases, changing existing
ones. It can help with installation, DNS, DHCP, package updates, power management, configuration
management orchestration, and much more. [#]_

.. code-block:: console

   $ osism-infrastructure cobbler

Mirror
------

With the mirror services it is possible to store packages for Ubuntu and images for Docker in one central
location.

.. code-block:: console

   $ osism-infrastructure mirror

After the bootstrap of the mirror services they have to be synchronized. Depending on
the bandwidth, this process will take several hours.

.. code-block:: console

   $ osism-mirror images
   $ osism-mirror packages

.. [#] source: https://github.com/cobbler/cobbler/blob/master/README.md
