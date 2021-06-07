.. _configuration-environment-manager:

=======
Manager
=======

Base directory: ``environments/manager``

Ansible configuration
=====================

.. note::

   Do not customize the ``ansible.cfg`` configuration file. The file will be updated
   from time to time.

Playbooks
=========

The manager environment ``environments/manager/`` hosts playbooks to perform the
initial bootstrap of the manager node. The initial bootstrap installs management
commands and configuration files.

.. note::

   These playbooks are updated from time to time. Therefore do not make any changes to them.
   Custom playbooks can be placed in the custom environment.

Inventory
=========

The manager environment has a dedicated inventory file
``environments/manager/hosts``. Only one host group ``manager`` is part of the
inventory. All other environments use the global inventory at
``inventory/hosts`` or ``inventory/20-roles``.

To use Netbox as inventory create the file e.g. ``inventory/netbox-inventory.yml``

.. code-block:: ini

   plugin: netbox.netbox.nb_inventory
   api_endpoint: <netbox_url>
   validate_certs: True
   group_by:
     - device_roles
   query_filters:
     - role: <netbox_role>
   token: "<netbox_token>"
   cache: yes
   cache_prefix: netbox_inventory_
   cache_timeout: 3600

Script
======

The manager environment includes a ``run.sh`` script. This script is used for
the execution of the included playbooks.

.. note::

   Do not customize the ``run.sh`` script. The file will be updated from time to time.

Caching
=======

Redis
-----

* ``environments/ansible.cfg``

.. code-block:: ini

   # Fact caching
   gathering = smart
   fact_caching = redis
   fact_caching_timeout = 86400
   fact_caching_connection = cache:6379:0

JSON file
---------

* ``environments/manager/configuration.yml``

.. code-block:: ini

   redis_enable: false

* ``environments/ansible.cfg``

.. code-block:: ini

   # Fact caching
   gathering = smart
   fact_caching = jsonfile
   fact_caching_timeout = 86400
   fact_caching_connection = /share/facts

.. warning::

   ``jsonfile`` fact caching can cause a huge performance impact for compute nodes, due to the
   large number of virtual network interfaces. Cases of 50MB and above for a single node have
   been seen. Depending on the number of compute nodes this slows down Ansible quite a lot. If
   you have issues with that, switch to Redis fact caching.
