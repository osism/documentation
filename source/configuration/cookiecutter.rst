============
Cookiecutter
============

.. note::

   To gain access to the configuration repository for your customer specific
   infrastructure, please send a request to info@betacloud-solutions.de.

Preparations
============

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

Installation
============

Installation of *gcc*, *python-development* and *git* packages is a
prerequisite to install required Python packages.

.. code-block:: console

   apt-get install git build-essential python3-dev

It is recommended to use a virtual environment when installing packages from PyPI.

.. code-block:: console

   virtualenv -p python3 .venv
   source .venv/bin/activate
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

Initialisation
==============

When running cookiecutter, infrastructure specific information needs to be
provided.

A list with all parameters can be found in the ``cookiecutter.json``
configuration file inside the configuration repository. A description of the
individual parameters can be found in the README file of the repository.

.. code-block:: console

   cookiecutter https://git.betacloud-solutions.de/generic/cookiecutter.git

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
   name_servers [default]: { "values": ["8.8.8.8", "4.4.4.4"] }
   ntp_servers [default]: { "values": ["de.pool.ntp.org"] }

Create a Git repository inside the newly created ``cfg-customer`` directory.
Be careful not to forget dotfiles like ``.gitignore``.

.. code-block:: console

    cd cfg-customer
    git init
    git add .
    git commit -m "Initial commit"

Push the repository to a Git server, so it will be available to the manager node.

.. code-block:: console

    git remote add origin <your-git-server>/cfg-customer
    git push --set-upstream origin master

.. figure:: /images/gitlab-initial-commit.png

   Directory structure after the initial commit in the Git repository. The ``secrets`` directory
   is only stored in the repository for test environments.
