============
Preparations
============

Seed node
=========

.. note::

   Run the commands on the seed node.

* Install required packages

  .. code-block:: console

     $ sudo apt install git python-pip python-virtualenv

* Clone the configuration repository

  .. code-block:: console

     $ git clone ssh://git@config-1.osism.io:10022/customers/xxx/cfg-yyy.git

.. note::

   If necessary, the deployment key can be used for the initial transfer of the repository.

   For this, the following content is added in ``~/.ssh/config`` and the SSH privte key is stored in
    ``~/.ssh/id_rsa.configuration``.

   ``config-1.osism.io`` will be replaced by the corresponding server

   .. code-block:: none

      Host config-1.osism.io
        HostName config-1.osism.io
        User git
        Port 10022
        IdentityFile ~/.ssh/id_rsa.configuration

Manager node
============

.. note::

   Run the commands on the seed node. Execute the commands within the
   manager environment (``cd environments/manager``).

.. note::

   You can use a different folder location for the virtual environment that will be created by setting
   the environment variable ``VENV_PATH``. This is required for example if your current folder path
   contains blank characters.

.. note::

   Various Ansible configurations can be adjusted via environment variables.

   For example, to query the password for using ``sudo``, add ``ANSIBLE_BECOME_ASK_PASS=True``.

   If ``secrets.yml`` files are encrypted with Ansible Vault, ``ANSIBLE_ASK_VAULT_PASS=True`` is added.

   http://docs.ansible.com/ansible/devel/reference_appendices/config.html#environment-variables

* Creation of the necessary operator user

.. note::

   If at the beginning the login with a password is required, ``ANSIBLE_ASK_PASS=True`` must be set.

.. note::

   If at the beginning the login with an SSH key is required, the key has to be added on the manager
   node to ``authorized_keys`` of the user specified in ``ANSIBLE_USER``.

.. warning::

   If the operator user was already created when the operating system was provisioned, this
   role must still be executed. ``ANSIBLE_USER`` is then adjusted accordingly.

   The UID and GID must also be checked. If it is not ``45000``, it must be adapted accordingly.

   .. code-block:: console

      # usermod -u 45000 dragon
      # groupmod -g 45000 dragon

      # chgrp dragon /home/dragon/
      # chown dragon /home/dragon/

      # find /home/dragon -group 1000 -exec chgrp -h dragon {} \;
      # find /home/dragon -user 1000 -exec chown -h dragon {} \; 

.. code-block:: console

   $ ANSIBLE_USER=ubuntu ./run.sh operator

.. note::

   A typical call to create the operator user looks like this.

   .. code-block:: console

      $ ANSIBLE_BECOME_ASK_PASS=True ANSIBLE_ASK_VAULT_PASS=True ANSIBLE_ASK_PASS=True ANSIBLE_USER=ubuntu ./run.sh operator

.. note::

   If the error ``/bin/sh: 1: /usr/bin/python: not found`` occurs, Python must first be installed on
   the manager node.

   .. code-block:: console

      $ ANSIBLE_USER=ubuntu ./run.sh python

.. note::

   To verify the creation of the operator user, use the private key file ``id_rsa.operator``.

   .. code-block:: console

      $ ssh -i id_rsa.operator dragon@10.49.20.10

.. code-block:: console

   $ export ANSIBLE_ASK_VAULT_PASS=True

* Configuration of the network

.. note::

   The network configuration already present on a system should be saved before this step.

.. note::

   Upon completion of this step, a system reboot should be performed to ensure that the configuration is functional and reboot secure. Since network services are not restarted automatically, later changes to the network configuration are not effective without a manual restart of the network service or reboot of the nodes.

.. code-block:: console

   $ ./run.sh network
   $ ./run.sh reboot

* Bootstrap of the node

.. code-block:: console

   $ ./run.sh bootstrap

.. note::

   After the bootstrap check if a reboot is required by checking if the file
   ``/var/run/reboot-required`` exists.

* Transfer configuration repository

.. code-block:: console

   $ ./run.sh configuration

* Deployment of necessary services

.. code-block:: console

   $ ./run.sh manager

.. note::

   To cleanup created directories/files after a run set the environment variable
   ``CLEANUP=true`` or manually delete the ``roles`` and ``.venv`` directories
   as well as the ``id_rsa.operator`` file when you finished the preparations of
   the manager system.

Infrastructure services
=======================

.. note:: Run the commands on the manager node.

Cobbler
-------

.. code-block:: shell

   $ osism-infrastructure cobbler

Mirror
------

.. code-block:: shell

   $ osism-infrastructure mirror

After the bootstrap of the mirror services they have to be synchronized. Depending on the bandwidth, this process will take several hours.

.. code-block:: shell

   $ osism-mirror files
   $ osism-mirror images
   $ osism-mirror packages
