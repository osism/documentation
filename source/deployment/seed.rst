=========
Seed node
=========

.. contents::
   :local:

.. note:: Execute the following commands on the seed node.

The seed node is used once for the first bootstrap of the manager node. It is sufficient to use
the local workstation. It doesn't have to be a dedicated system. The seed node must be able to
reach the manager node via SSH.

The use of Linux on the seed node is recommended. Other operating systems should also work
without problems.

Required Packages
=================

.. code-block:: console

   $ sudo apt install git python3-pip python3-virtualenv sshpass

Configuration repository
========================

.. code-block:: console

   $ git clone ssh://git@git.betacloud-solutions.de:10022/customers/xxx/cfg-yyy.git

If necessary, the configuration SSH key can be used for the initial transfer of the
repository.

For this, the following content is added in ``~/.ssh/config`` and the SSH privte key is
stored in ``~/.ssh/id_rsa.configuration``.

.. code-block:: none

   Host git.betacloud-solutions.de
     HostName git.betacloud-solutions.de
     User git
     Port 10022
     IdentityFile ~/.ssh/id_rsa.configuration
