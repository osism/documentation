=======
Cockpit
=======

* https://cockpit-project.org

Client
======

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.cockpit``
   * - **Repository**
     - https://github.com/osism/ansible-cockpit
   * - **Documentation**
     - ---

* ``environments/configuration.yml``

  .. code-block:: yaml

     ##########################
     # cockpit

     configure_cockpit: yes
     cockpit_ssh_interface: "{{ console_interface }}"

     ##########################
     # hardening

     security_sshd_allowed_macs: hmac-sha2-256,hmac-sha2-512,hmac-sha1

Server
======

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.cockpit``
   * - **Repository**
     - https://github.com/osism/ansible-cockpit
   * - **Documentation**
     - ---

* ``inventory/host_vars/MANAGER.yml``

  .. code-block:: yaml

     ##########################
     # cockpit

     configure_cockpit_server: yes
     cockpit_host: "{{ hostvars[inventory_hostname]['ansible_' + console_interface]['ipv4']['address'] }}"
