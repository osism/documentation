=========
Hardening
=========

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``hardening``
   * - **Repository**
     - https://github.com/openstack/ansible-hardening
   * - **Documentation**
     - https://docs.openstack.org/ansible-hardening/latest/

Use of local NTP server
=======================

* Remove ``security_ntp_servers`` and ``security_allowed_ntp_subnets`` from ``environments/configuration.yml``

.. code-block:: yaml
   :caption: host_vars file of a system providing a local NTP server

   ##########################################################
   # hardening

   security_ntp_servers:
     - 1.de.pool.ntp.org
     - 2.de.pool.ntp.org
     - 3.de.pool.ntp.org
     - 4.de.pool.ntp.org
   security_allowed_ntp_subnets:
     - 127.0.0.1/32
     - 192.168.102.0/24
   security_ntp_bind_local_interfaces_only: no

.. code-block:: yaml
   :caption: host_vars file of a system using a local NTP server

   ##########################################################
   # hardening

   security_ntp_servers:
     - 192.168.102.19
   security_allowed_ntp_subnets:
     - 127.0.0.1/32
