===
ARA
===

ARA records Ansible playbooks and makes them discoverable via web interface.

The ARA web interface can be reached via the ``console`` network, running on the
manager node on port ``8120``. The username is ``ara`` and the password can be
found in the file ``environments/secrets.yml`` at variable ``ara_password``.

Open the URL pointing to your manager node like: ``http://mananger01:8120/``

Delete old playbooks
====================

With the following call the 100 oldest playbooks that are at least 31
days old will be deleted.

With ``--days`` the minimum age can be specified.

.. code-block:: console

   docker exec -it manager_ara-server_1 sh
   ara-manage prune --confirm --username $ARA_API_USERNAME --password $ARA_API_PASSWORD
