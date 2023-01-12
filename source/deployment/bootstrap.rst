.. _bootstrap:

=========
Bootstrap
=========

The following steps are performed to initialize all nodes. :ref:`scaling` describes how to
add a new node to an existing environment.

* Creation of the operator user

  .. code-block:: console

     osism apply operator -u ubuntu

  * The operator key has to be added in advance on all nodes to ``authorized_keys`` of the user
    specified with ``-u``.
  * Alternatively (not recommended), the password can be stored in plain text in a file
    ``/opt/configuration/secrets/ubuntu_password``. The parameter
    ``--conn-pass-file /opt/configuration/secrets/ubuntu_password`` must then
    also be specified:

    .. code-block:: console

       osism apply operator -u ubuntu --conn-pass-file /opt/configuration/secrets/ubuntu_password

  * If the error ``/bin/sh: 1: /usr/bin/python: not found`` occurs, Python must first be installed
    with ``osism apply python3 -u ubuntu``.

* Configuration of the network

  .. code-block:: console

     osism apply network

  * The network configuration already present on a system should be backuped before this step.

* Reboot of the nodes

  .. code-block:: console

     osism apply reboot -l 'all:!manager' -e ireallymeanit=yes

* Check if all systems are reachable (you probably have to do this several times until
  all systems are accessible)

  .. code-block:: console

     osism apply ping

  * System is currently rebooting and is not yet accessible via network

    .. code-block:: none

       fatal: [net003]: UNREACHABLE! => {"changed": false, "msg": "Connection timed
       out.", "unreachable": true}``

  * System has already been rebooted and is not accessible via the network

    .. code-block:: none

       fatal: [net003]: UNREACHABLE! => {"changed": false, "msg": "EOF on stream;
       last 100 lines received:\nssh: connect to host 10.15.0.33 port 22: No route
       to host\r", "unreachable": true}

* Refresh facts

  .. code-block:: console

     osism apply facts

* Bootstrap of the nodes

  .. code-block:: console

     osism apply bootstrap

* Reboot of the nodes

  .. code-block:: console

     osism apply reboot -l 'all:!manager' -e ireallymeanit=yes

* Prepare the SSH configuration of the manager node

  .. code-block:: console

     osism apply sshconfig

* Check again if all systems are reachable (you probably have to do this several times
  until all systems are accessible)

  .. code-block:: console

     osism apply ping

**Ready. All nodes are now bootstrapped and available to launch services.**
