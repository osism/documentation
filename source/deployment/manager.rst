========================
Prepare the manager node
========================

.. note:: Run the commands on the seed node.

.. code-block:: shell

   $ cd environments/manager
   $ ANSIBLE_USER=ubuntu ./run.sh operator
   $ ./run.sh network
   $ ./run.sh bootstrap
   $ ./run.sh configuration
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
