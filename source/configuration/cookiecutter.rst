============
Cookiecutter
============

.. note::

   To gain access to the cookiecutter repository, please send a request to info@betacloud-solutions.de.

To prepare the configuration repository, you need the tool `Cookiecutter <https://github.com/audreyr/cookiecutter>`_.

Preparations
============

You need a Git repository to store the configuration of the environment. It has to be accessible
from the manager node. A SSH deploy key for read-only access is sufficient.

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

   $ cookiecutter ssh://git@git.betacloud-solutions.de:10022/generic/cookiecutter.git
   with_ceph [1]:
   with_monitoring [1]:
   with_vault [1]:
   ceph_fsid [Use a great UUID here]:
   [...]

Push the contents of the newly created ``cfg-customer`` directory to your Git repository. Be careful
not to forget dotfiles like ``.gitignore``. The directory itself is not stored in the repository.

.. figure:: /images/gitlab-initial-commit.png

   Directory structure after the initial commit in the Git repository. The ``secrets`` directory
   is only stored in the repository for test environments.
