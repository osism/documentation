======
Update
======

There are three possibilities to update the configuration repository on the manager node.

On the seed node change into the manager environment and use the following command. This will update the configuration repository on the manager node.

.. code-block:: console

   $ ./run.sh configuration

On the manager node use the following command to update the configuration repository.

.. code-block:: console

   $ osism-generic configuration

Alternatively, Git itself can be used on the manager node to update the repository.

.. code-block:: console

   $ cd /opt/configuration
   $ ssh-agent bash -c 'ssh-add ~/.ssh/id_rsa.configuration; git pull'
