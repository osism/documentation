======
Custom
======

The custom environment is used to store any additional playbooks and services.

Where possible, playbooks are integrated into ``osism-ansible``. Additional services are implemented in a separate role as needed.

Playbooks
=========

* Playbooks are provided with the prefix ``playbook-`` and the file extension ``.yml``, completely so then ``playbook-NAME.yml``
* Playbooks can be executed via ``osism-run custom NAME``

Here is an example of playbook ``playbook-cronjobs.yml`` that creates a cronjob for collecting facts on a manager node on a regular basis.

It is executed with ``osism-run custom cronjobs``.

.. code-block:: yaml

   ---
   - name: Manage cronjobs on the manager node
     hosts: manager
     gather_facts: false

     tasks:
     - name: Run helper scripts non-interactive
       cron:
         name: INTERACTIVE
         env: yes
         value: "false"
         cron_file: osism
         user: "{{ operator_user }}"
       become: true

     - name: Gather facts
       cron:
         name: "gather facts"
         minute: "15"
         hour: "*/6"
         job: /usr/local/bin/osism-run-without-secrets generic facts
         cron_file: osism
         user: "{{ operator_user }}"
       become: true

Services
========
