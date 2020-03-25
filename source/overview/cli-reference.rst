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

.. code-block:: console

   osism-generic
       [configuration]
       [hosts]
       [facts]
       [ping]
       [operator]
       [--user USER | -u USER]
       [--key-file /path/to/id_rsa]
       [--ask-pass]
       [--ask-become-pass]
       [--become]
       [bootstrap]
       [repository]
       [docker]
       [network]
       [backup-mariadb]
       [cleanup-backup-mariadb]
       [upgrade-packages]
       [check-reboot]
       [reboot]
       [resolvconf]
       [hardening]
       [--limit ANSIBLE_INVENTORY_NAME | -l ANSIBLE_INVENTORY_NAME]

   configuration
       get the latest git data for osism
   hosts
       update /etc/hosts
   facts
       update the facts
   ping
       connection test via ansible
   operator
       login via key and configure dragon user
       in combination with --user, --key-file and --limit or
       --ask-pass, --ask-become-pass and --become
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
   bootstrap
       bootstrap
   repository
       add repositories
   docker
       install/update/configure docker daemon
   network
       configure network
   backup-mariadb, cleanup-backup-mariadb
       mariadb backup and cleanup backups
   upgrade-packages
       upgrade the repository packages, the playbook asks are you sure
   check-reboot
       check if reboot is necessary
   reboot
       reboot, the playbook asks are you sure
   resolvconf
       update DNS
   hardening
       hardening role

osism-infrastucture
===================

container manager_osism-ansible_1

.. code-block:: console

   osism-infrastructure
       [helper]
       [cobbler]
       [mirror]
       [mirror-images]
       [mirror-packages]
       [--tags HELPER_TAG]

   helper
       deploy helper like cephclient, openstackclient, phpmyadmin, rally, sshconfig, adminer
   cobbler
       deploy/configure/update cobbler
   mirror
       deploy aptly, nexus, registry
   mirror-images
       mirror images
   mirror-packages
       create aptly mirror

osism-kolla
===========

container manager_kolla-ansible_1

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

script using environment /opt/configuration/environments/manager/

.. code-block:: console

   osism-manager
       [manager]

   manager
       deploy/update manager, twice vault pw
   prefix
       please use environment variables for Ansible configuration like ANSIBLE_ASK_VAULT_PASS=True,
       e.g. ANSIBLE_ASK_VAULT_PASS=True osism-manager manager

osism-mirror
============

script using environment /opt/configuration/environments/infrastructure
.. code-block:: console

   osism-mirror images, packages
       # synchronize images and packages

osism-monitoring
================

.. code-block:: console

   osism-monitoring prometheus-exporter, prometheus, monitoring
       # deploy prometheus, grafana and configuration

osism-openstack
===============

.. code-block:: console

   osism-openstack nova-aggregates
   osism-openstack nova-flavors
   osism-openstack glance-images

osism-run
=========

osism-run is for all additional plays/playbooks

.. code-block:: console

   osism-run proxmox create
       # create proxmox VM
   osism-run custom force-timesync
       # force NTP sync via chrony http://docs.osism.io/operations/generic.html#run-commands
   osism-run-without-secrets ...
       # runs the following command without asking for password and without all secrets,
         e.g. for cronjobs
   osism-run custom personalized-accounts
       # runs playbook for configuring personalized accounts

osism-run-without-secrets
=========================

run playbooks without vault access

.. code-block:: console

   dragon@controller:~$ cat /etc/cron.d/osism
   INTERACTIVE="false"
   #Ansible: gather facts
   15 */6 * * * dragon /usr/local/bin/osism-run-without-secrets generic facts