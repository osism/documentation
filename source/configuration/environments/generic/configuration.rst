========================
Configuration repository
========================

* role: ``osism.configuration`` (https://github.com/osism/ansible-configuration)

Git
===

* ``environments/configuration.yml``

.. code-block:: yaml

   ##########################
   # configuration

   configuration_directory: /opt/configuration
   configuration_type: git
   configuration_git_version: master

   configuration_git_username: git
   configuration_git_host: git-1.osism.io
   configuration_git_port: 22
   configuration_git_protocol: ssh
   configuration_git_repository: customers/foobar.git

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
