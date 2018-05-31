========
Overview
========

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

Configuration
-------------

* ``environments/ansible.cfg``
* ``environments/*/ansible.cfg``

Inventory
---------

* ``inventory``
* ``inventory/hosts``
* ``inventoyr/host_vars/*.yml``

Cookiecutter
============
