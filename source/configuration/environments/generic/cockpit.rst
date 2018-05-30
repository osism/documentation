=======
Cockpit
=======

Client
======

* role: ``osism.common`` (https://github.com/osism/ansible-common)

Necessary packages are installed by default.

To not install these packages set ``required_packages_cockpit: []`` in ``environments/configuration.yml``.

* ``environments/configuration.yml``

  .. code-block:: yaml

     ##########################
     # hardening

     security_sshd_allowed_macs: hmac-sha2-256,hmac-sha2-512,hmac-sha1

Server
======

* role: ``osism.manager`` (https://github.com/osism/ansible-manager)

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
