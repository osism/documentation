============
Cookiecutter
============

.. note::

   To gain access to the cookiecutter repository, please send a request to info@betacloud-solutions.de.

To prepare the configuration repository, you need the tool `Cookiecutter <https://github.com/audreyr/cookiecutter>`_.

Preparations
============

You need a Git repository to store the configuration of the environment. It has to be accessible
from the manager node. A SSH deploy/access key for read-only access is sufficient.

Before you create the configuration, you need some basic information:

* NTP servers
* DNS servers
* FQDNs and IP addresses for the API endpoints
* desired versions of OSISM, OpenStack, Ceph and Docker
* CIDRs of networks for Ceph
* SSL certificate, if one is used

.. note::

   After the deployment of the manager, it is possible to generate a self-signed SSL certificate
   using an included Ansible playbook. See :ref:`generation-of-self-signed-certificate` for more
   information.

Usually you prepare and edit the configuration on your workstation. It is pushed to a central Git
server and pulled from the manager node later.

Installation
============

Installation of gcc and python-development packages is a prerequisite to install
required Python packages.

.. code-block:: console

   $ apt-get install build-essential python3-dev

It is recommended to always use a virtual environment when you install packages from PyPI.

.. code-block:: console

   $ virtualenv -p python3 .venv
   $ source .venv/bin/activate
   $ pip3 install \
       ansible \
       cookiecutter \
       cryptography \
       oslo.utils \
       paramiko \
       passlib \
       pycrypto \
       pykeepass \
       python-gilt \
       pyyaml \
       ruamel.yaml \
       yamllint

Initialisation
==============

When you run cookiecutter, you are asked for the information you collected before.

A list with all parameters can be found in the ``cookiecutter.json`` configuration file.
A description of the individual parameters can be found in the README file of the repository.

.. code-block:: console

   $ cookiecutter https://git.betacloud-solutions.de/generic/cookiecutter.git

   with_ceph [1]: yes
   with_monitoring [1]: no
   with_vault [1]: yes
   ceph_fsid [Use a great UUID here]: 1a6b162c-cc15-4569-aa09-db536c93569f
   ceph_manager_version [2019.3.0]:
   ceph_network_backend [192.168.101.0/24]: 10.0.6.0/24
   ceph_network_frontend [192.168.100.0/24]: 10.0.5.0/24
   ceph_version [luminous]:
   docker_registry [index.docker.io]:
   docker_version [5:18.09.5]:
   domain [osism.io]: betacloud.io
   fqdn_external [api-1.osism.io]: external-api.betacloud.io
   fqdn_internal [api-1.osism.xyz]: internal-api.betacloud.xyz
   git_host [git.betacloud-solutions.de]:
   git_port [22]:
   git_repository [generic/cookiecutter]:
   git_username [git]:
   git_version [master]:
   ip_external [192.168.0.200]: 10.0.3.10
   ip_internal [192.168.0.100]: 10.0.1.10
   kolla_manager_version [2019.3.0]:
   openstack_version [rocky]:
   osism_manager_version [2019.3.0]:
   project_name [customer]: betacloud
   repository_version [2019.3.0]:
   name_servers [default]: { "values": ["10.0.0.1"] }
   ntp_servers [default]: { "values": ["10.0.0.1"] }

Push the contents of the newly created ``cfg-customer`` directory to your Git repository. Be careful
not to forget dotfiles like ``.gitignore``. The directory itself is not stored in the repository.

.. figure:: /images/gitlab-initial-commit.png

   Directory structure after the initial commit in the Git repository. The ``secrets`` directory
   is only stored in the repository for test environments.
