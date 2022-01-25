======
Chrony
======

* https://chrony.tuxfamily.org/

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``collection.osism.services.chrony``
   * - **Repository**
     - https://github.com/osism/ansible-collection-services/tree/main/roles/chrony
   * - **Documentation**
     - ---

Configuration
=============

* Configuration for ``chrony`` only as Client

.. code-block:: yaml
   :caption: environments/configuration.yml

   ##########################
   # chrony

   enable_chrony: true
   chrony_servers:
     - 10.0.3.1
     - 10.0.3.2
   chrony_allowed_subnets:
     - 127.0.0.1/32

* Configure ``manager`` as NTP client and server and ``control`` as NTP client

.. code-block:: yaml
   :caption: inventory/group_vars/manager.yml

   ##########################
   # chrony

   enable_chrony: true
   chrony_servers:
     - 0.de.pool.ntp.org
     - 1.de.pool.ntp.org
     - 2.de.pool.ntp.org
     - 3.de.pool.ntp.org
   chrony_allowed_subnets:
     - 10.0.3.0/24

.. code-block:: yaml
   :caption: inventory/group_vars/control.yml

   ##########################
   # chrony

   enable_chrony: true
   chrony_servers:
     - 10.0.3.1 # manager1
     - 10.0.3.2 # manager2
   chrony_allowed_subnets:
     - 127.0.0.1/32