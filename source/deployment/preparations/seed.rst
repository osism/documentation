=========
Seed node
=========

.. note::

   Run the commands on the seed node.

* install required packages

  .. code-block:: console

     $ sudo apt install git python-pip python-virtualenv

* clone the configuration repository

  .. code-block:: console

     $ git clone git@github.com:organisation/cfg-xyz.git

.. note::

   If necessary, the deployment key can be used for the initial transfer of the repository.

   For this, the following content is added in ``~/.ssh/config`` and the SSH privte key is stored in
    ``~/.ssh/id_rsa.configuration``.

   ``github.com`` will be replaced by the corresponding server

   .. code-block:: none

      Host github.com
        HostName github.com
        User git
        Port 22
        IdentityFile ~/.ssh/id_rsa.configuration
