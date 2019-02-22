========
Overview
========

The configuration repository is divided into so-called environments.

With the exception of a special environment for the manager, all environments
have the same structure.

All environments, except the manager's, share a common inventory.

There are the following environments:

* ceph
* custom
* generic
* infrastructure
* kolla
* manager
* monitoring

In the further subchapters, the configuration options within the individual
environments are described.

Files
=====

* ``configuration.yml``

  Default configuration parameters can be overwritten by this file.

* ``images.yml``

  This file can be used to overwrite default images.

* ``secrets.yml``

  Environment specific secrets can be deposited in this file.

* ``ansible.cfg``

  Ansible configuration file.

* ``playbook-*.yml``

  Playbook files for Ansible.

Directories
===========

* ``inventory``

  Ansible inventory directory. All host-specific details are managed here.

* ``environments``

  Directory for managing the individual environments. Each environment has its own subdirectory.

* ``docs``

  Optional directory to manage documents about an environment.

Ansible
=======

* ``environments/ansible.cfg``
* ``environments/*/ansible.cfg``

Inventory
=========

* ``inventory``
* ``inventory/hosts``
* ``inventory/host_vars/*.yml``
* ``inventory/group_vars/*.yml``
