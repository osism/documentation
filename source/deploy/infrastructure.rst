==============
Infrastructure
==============

.. note::

   Run the commands on the manager node.

* Creation of the necessary operator user

.. code-block:: console

   $ osism-generic operator

* Configuration of the network

.. note::

   The network configuration already present on a system should be saved before this step.

.. note::

   Upon completion of this step, a system reboot should be performed to ensure that the configuration is functional and reboot secure.

.. code-block:: console

   $ osism-generic network
   $ osism-generic reboot

* Bootstrap of the nodes

.. code-block:: console

   $ osism-generic bootstrap
   $ osism-generic common
