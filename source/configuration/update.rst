======
Update
======

There are three possible ways to update the configuration repository.

On the seed node containing the configuration repository, created by
*cookiecutter*, change into ``environments/manager`` directory and execute the
following command.  This will update the configuration repository on the manager
node.

.. code-block:: console

   ./run.sh configuration

On the manager node use the following command to update the configuration
repository.

.. code-block:: console

   osism-generic configuration

Alternatively, Git itself can be used on the manager node to update the
repository. Therefore the deploy key have to have write permissions.

.. code-block:: console

   cd /opt/configuration
   ssh-agent bash -c 'ssh-add ~/.ssh/id_rsa.configuration; git pull'
