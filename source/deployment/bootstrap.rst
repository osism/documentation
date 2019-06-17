=========
Bootstrap
=========

Execute the following commands on the manager node.

* Creation of the necessary operator user

  .. code-block:: console

     $ osism-generic operator -l 'all:!manager' -u ubuntu

  * The operator key has to be added in advance on all nodes to ``authorized_keys`` of the user
    specified with ``-u``.
  * Alternatively, you can work with the parameters ``--ask-pass`` and ``--ask-become-pass``.
  * If the error ``/bin/sh: 1: /usr/bin/python: not found`` occurs, Python must first be installed on
    the manager node with ``osism-generic python -l 'all:!manager' -u ubuntu``.

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

* Configuration of the network

  .. code-block:: console

     $ osism-generic network -l 'all:!manager'

  * The network configuration already present on a system should be saved before this step.
  * We are currently still using ``/etc/network/interfaces``. Therefore rename all files below ``/etc/netplan`` to ``X.unused``.

* Reboot of the nodes

  .. code-block:: console

     $ osism-generic reboot -l 'all:!manager'

* Check if all systems are reachable

  .. code-block:: console

     $ osism-generic ping

* Refresh facts

  .. code-block:: console

     $ osism-generic facts

* Bootstrap of the nodes

  .. code-block:: console

     $ osism-generic bootstrap

  .. note::

     The re-execution of the bootstrap on the manager is intended.
