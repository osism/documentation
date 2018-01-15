============================
dict object has no attribute
============================

If the error ``dict object' has no attribute u'ansible_ens18'`` occurs while running an Ansible playbook, it is most likely because the facts in the cache are outdated.

To update the facts, re-collect them on the manager node.

.. code-block:: shell

   $ osism-generic facts
