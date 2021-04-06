===================
OSISM CLI Reference
===================

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
       [check-reboot]
       [cleanup-backup-mariadb]
       [configuration]
       [docker]
       [facts]
       [hardening]
       [hosts]
       [network]
       [operator]
       [ping]
       [reboot]
       [repository]
       [resolvconf]
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
   check-reboot
       check if reboot is necessary
   cleanup-backup-mariadb
       cleanup mariadb backups
   configuration
       get the latest git data for osism
   docker
       install/update/configure docker daemon
   facts
       update the facts
   hardening
       hardening role
   hosts
       update /etc/hosts
   network
       configure network
   operator
       login via key and configure dragon user
       in combination with --user, --key-file and --limit or
       --ask-pass, --ask-become-pass and --become
   ping
       connection test via ansible
   reboot
       reboot, the playbook asks are you sure
   repository
       add repositories
   resolvconf
       update DNS
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
       [cobbler]
       [helper]
       [mirror]
       [mirror-images]
       [mirror-packages]
       [--tags HELPER_TAG]

   cobbler
       deploy/configure/update cobbler
   helper
       deploy helper like cephclient, openstackclient, phpmyadmin, rally, sshconfig, adminer
   mirror
       deploy aptly, nexus, registry
   mirror-images
       mirror images
   mirror-packages
       create aptly mirror

osism-kolla
===========

container manager_kolla-ansible_1

configuration directory environments/kolla

.. code-block:: console

   osism-kolla
       [deploy SERVICE]
       [pull SERVICE]
       [reconfigure SERVICE]
       [upgrade SERVICE]

   deploy
       deploy SERVICE like common, keystone, nova, neutron
   pull
       pull container image for SERVICE
   reconfigure
       reconfigure SERVICE, e.g. configuration change
   upgrade
       upgrade SERVICE, e.g. Rocky -> Stein

osism-manager
=============

container manager_osism-ansible_1

configuration directory environments/manager/

.. code-block:: console

   osism-manager
       [manager]

   manager
       deploy/update manager, twice vault pw
   prefix
       please use environment variables for Ansible configuration like
       ANSIBLE_ASK_VAULT_PASS=True, e.g.
       ANSIBLE_ASK_VAULT_PASS=True osism-manager manager

osism-mirror
============

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
       [monitoring]
       [prometheus]
       [prometheus-exporter]

   monitoring
       deploy monitoring, e.g. netdata, zabbix
   prometheus
       deploy prometheus, only in older version of OSISM
   prometheus-exporter
       deploy prometheus-exporter, only in older version of OSISM

osism-openstack
===============

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
       force NTP sync via chrony http://docs.osism.io/operations/generic.html#run-commands
   custom personalized-accounts
       runs playbook for configuring personalized accounts

osism-run-without-secrets
=========================

run playbooks without vault access

.. code-block:: console

   dragon@controller:~$ cat /etc/cron.d/osism
   INTERACTIVE="false"
   #Ansible: gather facts
   15 */6 * * * dragon /usr/local/bin/osism-run-without-secrets generic facts
