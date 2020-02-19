===
ARA
===

Delete old playbooks
====================

With the following call the 100 oldest playbooks that are at least 31
days old will be deleted.

With ``--days`` the minimum age can be specified.

.. code-block:: console

   docker exec -it manager_ara-server_1 sh
   ara-manage prune --confirm --username $ARA_API_USERNAME --password $ARA_API_PASSWORD
