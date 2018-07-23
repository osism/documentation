============
Preparations
============

Required information
====================

Before you create the configuration repository, you need some basic information:

* NTP Server
* DNS Server
* FQDNs and IP addresses for the API endpoints
* SSL certificate, if one is used
* desired versions of OSISM, OpenStack, Ceph and Docker 

Configuration repository
========================

You need a Git repository to store the configuration of the environment. It has to be accessible from
the manager node. A SSH deploy key for read-only access is suffient.

Cookiecutter
============

To prepare the configuration repository, you need cookiecutter. Usually you prepare and edit the
repository on your workstation. It is pushed to a central server and pulled from the manager node
later.

.. code-block:: console

   $ sudo apt install cookiecutter

When you run cookiecutter, you are asked for the information you collected before.

.. code-block:: console

   $ cookiecutter https://github.com/osism/cfg-cookiecutter.git

Copy the content of the newly created ``cfg-customer`` directory into your Git repository. Be careful
not to forget ``.gitignore``.

.. warning::

   In a productive environment use Ansible Vault to encrypt the newly created ``secrets.yml`` files,
before committing it to the Git repository. Never commit any plaintext passwords or secrets to the
configuration repository.

.. fixme::

   Explain Ansible Vault usage in more detail.

Gilt
====

Use the Git layering tool Gilt to pull some basic configuration files.

You can install Gilt from the Python Package Index. It is recommended to always use a virtual
environment when you install packages from PyPI.

.. code-block:: console

   $ sudo apt install pip virtualenv
   $ virtualenv venv
   $ source venv/bin/activate
   $ pip install python-gilt

Now, inside your Git repository, run ``gilt overlay`` twice. The first time to pull the complete
``gilt.yml`` and the second time to pull the actual configuration files.

.. code-block:: console

   $ gilt overlay
   $ gilt overlay

.. fixme::

   Set default passwords. Hash operator password.
