=======================
Configuration reference
=======================

.. toctree::
   :maxdepth: 2

   configuration/cookiecutter
   configuration/synchronisation
   configuration/update
   configuration/networks
   configuration/environments

The basis of an OSISM installation is a configuration repository, which is
specific to the customers infrastructure, and is divided into individual
environments. Environments are the components used to configure the whole
infrastructure, like manager node, frontend and backend services, and so forth.

The structure, creation and content of the configuration repository is explained
in this chapter.

**Directories**

* ``inventory``: Ansible inventory directory. All host-specific details are managed here.
* ``docs``: Optional directory to manage documents about an environment.
* ``environments``: Directory for managing the individual environments. Each environment has its own subdirectory.

**Environments**

* :ref:`configuration-environment-manager`
* :ref:`configuration-environment-generic`
* :ref:`configuration-environment-infrastructure`
* :ref:`configuration-environment-openstack`
* :ref:`configuration-environment-ceph`
* :ref:`configuration-environment-custom`

With the exception of a special environment for the manager, all
environments have the same structure and share the same inventory.

**Files**

* ``configuration.yml``: Default configuration parameters can be overwritten by this file.
* ``images.yml``: This file can be used to overwrite default images.
* ``secrets.yml``: Environment specific secrets can be deposited in this file.
* ``ansible.cfg``: Ansible configuration file.
* ``playbook-*.yml``: Playbook files for Ansible.
* ``environments/ansible.cfg``: Ansible configuration file.
* ``environments/*/ansible.cfg``: Ansible configuration file.
* ``inventory/hosts``: Ansible inventory file.
* ``inventory/host_vars/*.yml``: Ansible host variables.
* ``inventory/group_vars/*.yml``: Ansible group variables.
