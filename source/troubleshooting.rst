===============
Troubleshooting
===============

Horizon dashboard looks broken
------------------------------

.. image:: /images/horizon-broken.png

You have to cleanup and restart all horizon containers.

.. code-block:: shell

   $ docker exec -it horizon rm /tmp/.local_settings.md5sum.txt && docker restart horizon

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

If this does not work check the grastate.dat file on all controller nodes.

.. code-block:: shell

   $ docker cp mariadb:/var/lib/mysql/grastate.dat /tmp/kolla_mariadb_grastate.dat
   $ cat /tmp/kolla_mariadb_grastate.dat
   # GALERA saved state
   version: 2.1
   uuid:    5ae8bce5-5ccd-4f8b-b56f-cfa601e7060e
   seqno:   -1
   safe_to_bootstrap: 0

If seqno is -1 and safe_to_bootstrap is 0 on all nodes you have to overwrite this file on one of the nodes. Set safe_to_bootstrap to 1 and copy the file into the data volume.

.. code-block:: shell

   $ docker cp /tmp/kolla_mariadb_grastate.dat mariadb:/var/lib/mysql/grastate.dat

Cleanup and run the playbook again.

.. code-block:: shell

   $ rm /tmp/kolla_mariadb_grastate.dat

* http://galeracluster.com/2016/11/introducing-the-safe-to-bootstrap-feature-in-galera-cluster/
