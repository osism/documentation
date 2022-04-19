=============
CLI Reference
=============

The following section lists osism commands and describe these.

osism-ansible
=============

container manager_osism-ansible_1

.. code-block:: console

   osism-ansible generic all
       [--module-name ANSIBLE_MODULE | -m ANSIBLE_MODULE]
       [--args 'COMMAND' | -a 'COMMAND']
       [--limit ANSIBLE_INVENTORY_NAME | -l ANSIBLE_INVENTORY_NAME]

   --module-name setup
       run ANSIBLE_MODULE (ansible-doc -l) for host ANSIBLE_INVENTORY_NAME to STDOUT,
       can be forwarded e.g. via > to FILE
   --args 'COMMAND'
       arguments for command 'COMMAND', e.g. 'chronyc tracking'|'uname -a'
   --limit ANSIBLE_INVENTORY_NAME
       limits the action to ANSIBLE_INVENTORY_NAME

osism-ceph
==========

container manager_ceph-ansible_1

configuration directory environments/kolla/ceph

.. code-block:: console

   osism-ceph
       [mons]
       [mgrs]
       [osds]
       [--limit ANSIBLE_INVENTORY_NAME | -l ANSIBLE_INVENTORY_NAME]

   mons
      deploys ceph monitoring
   mgrs
      deploys ceph manager
   osds
      deployes ceph osd
   --limit ANSIBLE_INVENTORY_NAME
      limits the actions to ANSIBLE_INVENTORY_NAME

osism-generic
=============

container manager_osism-ansible_1

configuration directory environments/

.. code-block:: console

   osism-generic
       [backup-mariadb]
       [bootstrap]
       [certificates]
       [check-reboot]
       [chrony-force-sync]
       [chrony]
       [cleanup-backup-mariadb]
       [cockpit]
       [docker]
       [facts]
       [frr]
       [grub]
       [hardening]
       [hostname]
       [hosts]
       [kernel-modules]
       [lldpd]
       [network]
       [operator]
       [packages]
       [ping]
       [proxy]
       [reboot]
       [repository]
       [resolvconf]
       [sysctl]
       [timezone]
       [upgrade-packages]
       [--user USER | -u USER]
       [--key-file /path/to/id_rsa]
       [--ask-pass]
       [--ask-become-pass]
       [--become]
       [--limit ANSIBLE_INVENTORY_NAME | -l ANSIBLE_INVENTORY_NAME]

   backup-mariadb, cleanup-backup-mariadb
       mariadb backup and cleanup backups
   bootstrap
       bootstrap
   certificates
       update certificate store
   check-reboot
       check if reboot is necessary
   chrony-force-sync
       force sync chrony
   chrony
       setup chrony
   cleanup-backup-mariadb
       cleanup mariadb backups
   cockpit
       setup cockpit
   docker
       install/update/configure docker daemon
   facts
       update the facts
   frr
       setup frrouting
   grub
       modify grub configuration
   hardening
       hardening role
   hostname
       setup hostname of nodes
   hosts
       update /etc/hosts
   kernel-modules
       configure kernel modules
   lldpd
       install lldpd
   network
       configure network
   operator
       login via key and configure dragon user
       in combination with --user, --key-file and --limit or
       --ask-pass, --ask-become-pass and --become
   packages
       upgrade packages and install ``required_packages``
   ping
       connection test via ansible
   proxy
       configure proxy configuration
   reboot
       reboot, the playbook asks are you sure
   repository
       add repositories
   resolvconf
       update DNS
   sysctl
       setup sysctl settings
   timezone
       configure timezone
   upgrade-packages
       upgrade the repository packages, the playbook asks are you sure
   --user USER
       argument for remote user
   --key-file /path/to/id_rsa
       argument for keyfile to login via remote user
   --ask-pass
       argument for asking the login password
   --ask-become-pass
       argument for asking the become pass
   --become
       argument for using the become method, e.g. sudo
   --limit ANSIBLE_INVENTORY_NAME
      limits the actions to ANSIBLE_INVENTORY_NAME

osism-infrastucture
===================

container manager_osism-ansible_1

configuration directory environments/infrastructure

.. code-block:: console

   osism-infrastructure
       [cephclient]
       [dnsdist]
       [homer]
       [nexus]
       [openstackclient]
       [phpmyadmin]
       [virtualbmc]

   cephclient
       deploy cephclient
   dnsdist
       deploy dnsdist as dns forwarder
   homer
       deploy homer, overview of webinterfaces
   nexus
       deploy nexus, packages and container images repository
   openstackclient
       deploy openstackclient
   phpmyadmin
       deploy phpmyadmin
   virtualbmc
       deploy virtualbmc, bmc to libvirt

osism-kolla
===========

container manager_kolla-ansible_1

configuration directory environments/kolla

.. code-block:: console

   osism-kolla
       [deploy SERVICE]
       [pull SERVICE]
       [reconfigure SERVICE]
       [refresh-containers SERVICE]
       [stop SERVICE]
       [upgrade SERVICE]

   deploy
       deploy SERVICE like common, keystone, nova, neutron
   pull
       pull container image for SERVICE
   reconfigure
       reconfigure SERVICE, e.g. configuration change
   refresh-containers
       update container images of SERVICE
   stop
       stop SERVICE
   upgrade
       upgrade SERVICE, e.g. Wallaby -> Xena

osism-manager
=============

container manager_osism-ansible_1

configuration directory environments/manager/

.. code-block:: console

   osism-manager
       [bifrost-command]
       [bifrost-deploy]
       [configuration]
       [netbox]
       [manager]

   bifrost-command
       wrap the commands in openstackclient commands
   bifrost-deploy
       deploy bifrost
   configuration
       get the latest git data for osism
   netbox
       deploy netbox
   manager
       deploy/update manager, twice vault pw
   prefix
       please use environment variables for Ansible configuration like
       ANSIBLE_ASK_VAULT_PASS=True, e.g.
       ANSIBLE_ASK_VAULT_PASS=True osism-manager manager
   ansible options
       or use the ansible options, like -k, -K or -b

osism-mirror
============

.. note::

    Only in old versions of OSISM

container manager_osism-ansible_1

configuration directory environments/infrastructure

.. code-block:: console

   osism-mirror
       [images]
       [packages]

   images
       synchronize images
   packages
       synchronize packages

osism-monitoring
================

container manager_osism-ansible_1

configuration directory environments/monitoring

.. code-block:: console

   osism-monitoring
       [monitoring] - old OSISM version
       [netdata]
       [openstack-health-monitor]
       [prometheus] - old OSISM version
       [prometheus-exporter] - old OSISM version
       [remove-netdata]
       [remove-zabbix-agent]

   monitoring
       deploy monitoring, e.g. netdata, zabbix
   netdata
       deploy netdata
   openstack-health-monitor
       deploy openstack-health-monitor
   prometheus
       deploy prometheus, only in older version of OSISM
   prometheus-exporter
       deploy prometheus-exporter, only in older version of OSISM
   remove-netdata
       removes netdata
   remove-zabbix-agent
       removes zabbix agent

osism-openstack
===============

.. note::

    Only in old versions of OSISM

container manager_osism-ansible_1

configuration directory environments/openstack

.. code-block:: console

   osism-openstack
       [nova-aggregates]
       [nova-flavors]
       [glance-images]

   nova-aggregates
       configure nova aggregates, for older version of OSISM
   nova-flavors
       configure nova flavors, for older version of OSISM
   glance-images
       configure glance images, for older version of OSISM

osism-run
=========

osism-run is for all additional roles, not included in OSISM

container manager_osism-ansible_1

configuration directory environments/custom , environments/proxmox

.. code-block:: console

   osism-run
       [custom]
       [proxmox]

   proxmox
       manage proxmox role
   custom force-timesync
       force NTP sync via chrony
   custom personalized-accounts
       runs playbook for configuring personalized accounts

https://docs.osism.tech/operations/generic.html#run-commands

osism-run-without-secrets
=========================

run playbooks without vault access

.. code-block:: console

   dragon@controller:~$ cat /etc/cron.d/osism
   INTERACTIVE="false"
   #Ansible: gather facts
   15 */6 * * * dragon /usr/local/bin/osism-run-without-secrets generic facts
