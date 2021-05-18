============
Cookiecutter
============

Cookiecutter Preparations
=========================

A Git repository is required to store the configuration for your specific
infrastructure. The manager node needs to have access to this repository.
An SSH deploy/access key for read-only access is sufficient.

Before creating the configuration repository, infrastructure specific
information needs to be provided:

* NTP servers
* DNS servers
* FQDNs and IP addresses for the API endpoints
* desired versions of OSISM, OpenStack, Ceph and Docker
* CIDRs of networks for Ceph
* SSL certificate, if one is used

.. note::

   After the deployment of the manager node, it is possible to generate a
   self-signed SSL certificate using an included Ansible playbook.
   See :ref:`generation-of-self-signed-certificate` for more information.

Usually the configuration repository is prepared on your workstation. After
the repository creation, it needs to be pushed to a central Git server, to make
it available to the manager node.

Dependency Installation
=======================

Installation of *gcc*, *python-development* and *git* packages is a
prerequisite to install required Python packages.

.. code-block:: console

   apt-get install git build-essential python3-dev

It is recommended to use a virtual environment when installing packages from PyPI.

.. code-block:: console

   virtualenv -p python3 .venv
   source .venv/bin/activate

.. code-block:: console

   pip3 install \
     ansible \
     cookiecutter \
     cryptography \
     oslo.utils \
     paramiko \
     passlib \
     pwgen \
     pycrypto \
     pykeepass \
     python-gilt \
     pyyaml \
     ruamel.yaml \
     yamllint

Cookiecutter Initialisation
===========================

When running *cookiecutter*, infrastructure specific information needs to be
provided.

A list with all parameters can be found in the ``cookiecutter.json``
configuration file inside the configuration repository. A description of the
individual parameters can be found in the README file of the repository.

.. code-block:: console

   cookiecutter https://github.com/osism/cfg-cookiecutter

   with_ceph [1]:
   with_vault [1]:
   ceph_fsid [Use a great UUID here]: 1a6b162c-cc15-4569-aa09-db536c93569f
   ceph_manager_version [latest]:
   ceph_network_backend [193.168.80.0/24]:
   ceph_network_frontend [192.168.70.0/24]:
   ceph_version [nautilus]:
   docker_registry [index.docker.io]:
   docker_version [5:19.03.5]:
   domain [osism.local]:
   fqdn_external [api.osism.local]:
   fqdn_internal [api-int.osism.local]:
   git_host [github]:
   git_port [22]:
   git_repository [osism/cfg-cookiecutter]:
   git_username [git]:
   git_version [master]:
   ip_external [192.168.90.200]:
   ip_internal [192.168.50.100]:
   kolla_manager_version [latest]:
   openstack_version [train]:
   osism_manager_version [latest]:
   project_name [customer]: osism
   repository_version [latest]:
   name_servers [default]: { "values": ["9.9.9.9", "149.112.112.112"] }
   ntp_servers [default]:

Create a Git repository inside the newly created ``cfg-osism`` directory.
Be careful not to forget dotfiles like ``.gitignore``.

.. code-block:: console

    cd cfg-osism
    git init
    git add .
    git commit -m "Initial commit"

Push the repository to a Git server, so it will be available to the manager node.

.. code-block:: console

    git remote add origin <your-git-server>/cfg-osism
    git push --set-upstream origin master

.. figure:: /images/gitlab-initial-commit.png

   Directory structure after the initial commit in the Git repository. The
   ``secrets`` directory is only stored in the repository for test environments.
