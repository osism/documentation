===============
Troubleshooting
===============

unable to find user dragon: no matching entries in passwd file
--------------------------------------------------------------

On the manager node restart the ``helper_helper_1`` container.

.. code-block:: shell

   $ docker restart helper_helper_1

MariaDB recovery
----------------

On the controller nodes stop the ``mariadb`` containers.

.. code-block:: shell

   $ docker stop mariadb

On the manager node run the recovery process.

.. code-block:: shell

   $ osism-kolla deploy mariadb_recovery
