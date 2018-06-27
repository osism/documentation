=======
Ansible
=======

Read facts from cache
=====================

.. code-block:: console

   $ docker exec -it manager_cache_1 redis-cli --scan
   ansible_facts10-11.betacloud.xyz
   [...]

   $ docker exec -it manager_cache_1 redis-cli get ansible_facts10-11.betacloud.xyz
   "{ "ansible_processor_count ": 2,  "module_setup ": true, [...]

Found variable using reserved name
==================================

This error occurs until the release of Pike and is not critical.

.. code-block:: console

   $ osism-kolla deploy X

    [WARNING]: Found variable using reserved name: action

    [WARNING]: Found variable using reserved name: serial

dict object has no attribute
============================

If the error ``dict object' has no attribute u'ansible_ens18'`` occurs while running an Ansible playbook, it is most likely because the facts in the cache are outdated.

To update the facts, re-collect them on the manager node.

.. code-block:: console

   $ osism-generic facts

Update facts manually
---------------------

.. note:: Run this command on the manager node.

.. code-block:: console

   $ osism-generic facts

   PLAY [Gather facts for all hosts] **********************************************

   TASK [setup] *******************************************************************
   ok: [20-11.betacloud.xyz]
   ok: [20-10.betacloud.xyz]
   [...]

   PLAY [Gather facts for all hosts (if using --limit)] ***************************

   TASK [setup] *******************************************************************
   skipping: [30-11.betacloud.xyz] => (item=20-11.betacloud.xyz)
   skipping: [30-11.betacloud.xyz] => (item=20-10.betacloud.xyz)
   [...]

   PLAY RECAP *********************************************************************
   10-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   20-10.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   [...]

Update facts regularly with cron
--------------------------------

Add this task to the ``playbook-cronjobs.yml`` playbook in the ``custom`` environment.

.. code-block:: yaml

   - name: Gather facts
     cron:
       name: "gather facts"
       minute: "15"
       hour: "*/6"
       job: /usr/local/bin/osism-run-without-secrets generic facts
       cron_file: osism
       user: "{{ operator_user }}"
     become: true
