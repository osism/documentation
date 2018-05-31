=======
Manager
=======

* base directory: ``environments/manager``

Ansible configuration
=====================

The Ansible configuration file stored in this environment must not be changed.

.. warning::

   Do not customize this file. The file will be updated from time to time.

Playbooks
=========

In this environment some playbooks are included. These are needed to perform the initial
bootstrap of the manager independently of Docker.

.. warning::

   These playbooks are updated from time to time. Therefore do not make any changes to them.
   Custom playbooks can be placed in the custom environment.

Inventory
=========

This environment has its own inventory file as the only environment. Only one host group
``manager`` is stored in this inventory. All other environments use the global inventory.

Script
======

This environment includes a ``run.sh`` script. This script is used for the execution of the
included playbooks.

.. warning::

   Do not customize this script. The file will be updated from time to time.
