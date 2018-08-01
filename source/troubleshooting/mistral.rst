=======
Mistral
=======

Empty action list
=================

Solution
--------

You have to populate the database.

.. code-block:: console

   $ docker exec -it mistral_api mistral-db-manage --config-file /etc/mistral/mistral.conf populate
