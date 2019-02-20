================
Initial creation
================

You need a Git repository to store the configuration of the environment. It has to be accessible from
the manager node. A SSH deploy key for read-only access is sufficient.

Before you create the configuration, you need some basic information:

* NTP Server
* DNS Server
* FQDNs and IP addresses for the API endpoints
* SSL certificate, if one is used
* desired versions of OSISM, OpenStack, Ceph and Docker

To prepare the configuration repository, you need cookiecutter. Usually you prepare and edit the
repository on your workstation. It is pushed to a central server and pulled from the manager node
later.

.. note::

   It is recommended to always use a virtual environment when you install packages from PyPI.

   .. code-block:: console

      $ virtualenv -p python3 .venv
      $ source .venv/bin/activate

.. code-block:: console

   $ pip install cookiecutter oslo.utils pycrypto pyyaml ruamel.yaml python-gilt paramiko

When you run cookiecutter, you are asked for the information you collected before.
A list with all queries can be found in the ``cookiecotter.json`` configuration file.

.. note::

   To gain access to the cookiecutter repository, please send a request to info@betacloud-solutions.de.

.. code-block:: console

   $ cookiecutter ssh://git@git.betacloud-solutions.de:10022/generic/cookiecutter.git

Copy the content of the newly created ``cfg-customer`` directory into your Git repository. Be careful
not to forget the ``.gitignore`` file.

.. warning::

   In a productive environment use Ansible Vault to encrypt the newly created ``secrets.yml`` files,
   before committing it to the Git repository. Never commit any plaintext passwords or secrets to the
   configuration repository.
