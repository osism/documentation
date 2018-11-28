=============
Configuration
=============

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.configuration``
   * - **Repository**
     - https://github.com/osism/ansible-configuration
   * - **Documentation**
     - ---

Git
===

* ``environments/configuration.yml``

.. code-block:: yaml

   ##########################
   # configuration

   configuration_directory: /opt/configuration
   configuration_type: git

   configuration_git_host: config-1.osism.io
   configuration_git_port: 10022

   configuration_git_private_key_file: ~/.ssh/id_rsa.configuration
   configuration_git_protocol: ssh
   configuration_git_repository: customers/CUSTOMER/cfg-NAME.git
   configuration_git_username: git
   configuration_git_version: master

Deploy key
----------

* https://developer.github.com/v3/guides/managing-deploy-keys/#deploy-keys
* https://docs.gitlab.com/ee/ssh/#per-repository-deploy-keys

* ``environments/secrets.yml``

  .. code-block:: yaml

     ##########################
     # private ssh keys

     configuration_git_private_key: |
       -----BEGIN RSA PRIVATE KEY-----
       [...]
       -----END RSA PRIVATE KEY-----
