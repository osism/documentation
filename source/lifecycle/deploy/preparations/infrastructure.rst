=======================
Infrastructure services
=======================

.. note:: Run the commands on the manager node.

Cobbler
=======

.. code-block:: shell

   $ osism-infrastructure cobbler

Mirror
======

.. code-block:: shell

   $ osism-infrastructure mirror

After the bootstrap of the mirror services they have to be synchronized. Depending on the bandwidth, this process will take several hours.

.. code-block:: shell

   $ osism-mirror files
   $ osism-mirror images
   $ osism-mirror packages
