=========
Seed node
=========

.. note::

   Execute the following commands on the seed node.

The seed node is used once for the initial bootstrap of the manager node. It is sufficient
to use the local workstation. It doesn't have to be a dedicated system. The seed node is no
longer needed in the further process. The seed node must be able to reach the manager node
via SSH.

The use of Linux on the seed node is recommended. Other operating systems should also work
without problems.


Install required packages
=========================

Ubuntu/Debian:

.. code-block:: console

   sudo apt install git python3-pip python3-virtualenv sshpass

MacOS:

``sshpass`` cannot be installed directly as a package via homebrew (``We won't add sshpass because
it makes it too easy for novice SSH users to ruin SSH's security.``).

.. code-block:: console

   brew tap esolitos/ipa
   brew install esolitos/ipa/sshpass


Get a copy of the configuration repository
==========================================

Each environment managed with OSISM is based on a configuration repository. This was previously
created with `Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_ and the
`cfg-cookiecutter <https://github.com/osism/cfg-cookiecutter>`_ repository. A configuration repository
is stored on a Git server (e.g. GitHub, Gitlab, ...). The configuration repository is individual
for each environment and is therefore not provided by us.

The configuration repository to be used must be available on the seed node. In the following
example, replace ``ORGANIZATION`` and ``cfg-ENVIRONMENT`` accordingly.

.. code-block:: console

   git clone ssh://git@github.com:ORGANIZATION/cfg-ENVIRONMENT.git

Examples:

* The repository is located in the ``betacloud`` organisation on GitHub, has the name
  ``configuration`` and can be accessed via SSH: ``ssh://git@github.com:betacloud/configuration.git``
* The repository is located in the ``betacloud`` organisation on Gitlab, has the name
  ``configuration`` and can be accessed via SSH: ``ssh://git@gitlab.com:betacloud/configuration.git``
* The repository is located in the ``betacloud`` organisation on an internal Gitlab, has the
  name ``configuration`` and can be accessed via SSH: ``ssh://git@git.services.osism.tech:betacloud/configuration.git``

If necessary, the configuration SSH key can be used for the initial transfer of the
repository.

For this, the following content is added in ``~/.ssh/config`` and the SSH privte key is
stored in ``~/.ssh/id_rsa.configuration``.

.. code-block:: none

   Host github.com
     HostName github.com
     User git
     Port 22
     IdentityFile ~/.ssh/id_rsa.configuration

**Ready. The seed is now ready to prepare the manager node.**
