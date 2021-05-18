===========================
OSISM Ansible Vault Secrets
===========================

OSISM uses Ansible Vault for handling secret information like passwords, ssh-keys, etc. There are several ``secret.yml`` files in the repository. See the following points for details on ansible-vault

* https://docs.ansible.com/ansible/latest/user_guide/vault.html
* ansible-vault --help

Find ``secret.yml`` files
=========================

.. code-block:: console

   $ find environments/ -name "*secrets.yml"
   environments/custom/secrets.yml
   environments/secrets.yml
   environments/infrastructure/secrets.yml
   environments/openstack/secrets.yml
   environments/generic/secrets.yml
   environments/monitoring/secrets.yml
   environments/ceph/secrets.yml
   environments/manager/secrets.yml
   environments/kolla/secrets.yml

General Secrets
---------------

In the file ``environments/secrets.yml`` there are general secrets OSISM is using and accessing over all environments like ``operator_private_key`` for ssh access with key.

Manager Secrets
---------------

``environments/manager/secrets.yml`` contains manager specific secrets.

Generic Secrets
---------------

``environments/generic/secrets.yml`` contains generic specific secrets.

Infrastructure Secrets
----------------------

``environments/infrastructure/secrets.yml`` contains infrastructure specific secrets.

Kolla Secrets
-------------

``environments/kolla/secrets.yml`` contains e.g. database admin password, keystone admin password, etc.

Ceph Secrets
------------

``environments/ceph/secrets.yml`` contains ceph specific secrets.

Openstack Secrets
-----------------

``environments/openstack/secrets.yml`` contains e.g. openstack-client clouds configuration data.

Custom Secrets
--------------

``environments/custom/secrets.yml`` contains custom secrets, e.g. ipmi password, slack webhook

Monitoring Secrets
------------------

``environments/monitoring/secrets.yml`` contains monitoring specific secrets.

Search Secret Files for Password
================================

Use the `script`_ ``environments/.vault_pass`` for searching passwords.

.. note::

   This works only on local git clone, **not** on manager.

.. code-block:: console

   $ cd environments/
   $ ./.vault_pass kibana
   Please enter the ansible vault password:

   kibana_password: lesssecret

Since this script is added in year 2021, you have to download and deploy the script in older environments.

.. _script: https://github.com/osism/cfg-cookiecutter/blob/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/.vault_pass