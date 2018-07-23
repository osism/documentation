=======
Cockpit
=======

Client
======

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.common``
   * - **Repository**
     - https://github.com/osism/ansible-common
   * - **Documentation**
     - ---

* ``environments/configuration.yml``

  .. code-block:: yaml

     ##########################
     # common

     configure_cockpit: yes

     ##########################
     # hardening

     security_sshd_allowed_macs: hmac-sha2-256,hmac-sha2-512,hmac-sha1

Server
======

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.manager``
   * - **Repository**
     - https://github.com/osism/ansible-manager
   * - **Documentation**
     - ---

* ``environments/manager/configuration.yml``

  .. code-block:: yaml

     ##########################
     # cockpit

     configure_cockpit: yes
     cockpit_groupname: all
     cockpit_host: "{{ hostvars[inventory_hostname]['ansible_' + management_interface]['ipv4']['address'] }}"
     cockpit_port: 8130
     cockpit_ssh_port: 22


     ##########################
     # cockpit

* ``environments/configuration.yml``

  .. code-block:: yaml

     ##########################
     # cockpit

     cockpit_ssh_interface: "{{ console_interface }}"
