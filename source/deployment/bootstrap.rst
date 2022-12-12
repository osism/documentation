.. _bootstrap:

=========
Bootstrap
=========

The following steps are performed to initialize all nodes. :ref:`scaling` describes how to add a new node to an existing environment.

* Creation of the necessary operator user

  .. code-block:: console

     osism apply operator -l 'all:!manager' -u ubuntu

  * The operator key has to be added in advance on all nodes to ``authorized_keys`` of the user
    specified with ``-u``.
  * If the error ``/bin/sh: 1: /usr/bin/python: not found`` occurs, Python must first be installed on
    the manager node with ``osism apply python3 -l 'all:!manager' -u ubuntu``.

* Configuration of the network

  .. code-block:: console

     osism apply network -l 'all:!manager'

  * The network configuration already present on a system should be backuped before this step.

* Reboot of the nodes

  .. code-block:: console

     osism apply reboot -l 'all:!manager' -e ireallymeanit=yes

* Check if all systems are reachable

  .. code-block:: console

     osism apply ping

* Refresh facts

  .. code-block:: console

     osism apply facts

* Bootstrap of the nodes

  .. code-block:: console

     osism apply bootstrap

* Reboot of the nodes

  .. code-block:: console

     osism apply reboot -l 'all:!manager' -e ireallymeanit=yes
