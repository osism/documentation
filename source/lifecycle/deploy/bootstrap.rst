=========
Bootstrap
=========

.. note::

   Run the commands on the manager node.

* Creation of the necessary operator user

.. note::

   The operator key has to be added in advance on all nodes to ``authorized_keys`` of the user
   specified with ``-u``.

.. code-block:: console

   $ osism-generic operator -l 'all:!manager' -u ubuntu

.. note::

   If the error ``/bin/sh: 1: /usr/bin/python: not found`` occurs, Python must first be installed on
   the nodes.

   .. code-block:: console

      $ osism-generic python -l 'all:!manager' -u ubuntu

* Configuration of the network

.. note::

   The network configuration already present on a system should be saved before this step.

.. note::

   Upon completion of this step, a system reboot should be performed to ensure that the configuration is functional and reboot secure.

.. code-block:: console

   $ osism-generic network -l 'all:!manager'

* Bootstrap of the nodes

.. code-block:: console

   $ osism-generic bootstrap

* Refresh ``/etc/hosts`` on the manager node

.. code-block:: console

   $ osism-generic hosts -l manager
