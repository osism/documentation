======
Travis
======

This chapter uses the Travis CLI. It is assumed that this is installed and a login has taken place.

* https://github.com/travis-ci/travis.rb#readme
* https://docs.travis-ci.com/user/apps/

Custom builds
=============

* https://blog.travis-ci.com/2017-08-24-trigger-custom-build

.. code-block:: yaml

   env:
     global:
       - OSISM_VERSION=latest
     matrix:
       - OPENSTACK_VERSION=pike KOLLA_IMAGES=rabbitmq PUSH=false BASEPUSH=false

.. image:: /images/travis-custom-build.png

Encrypted files
===============

* The project must be activated on Travis first.
* Add the file to be encrypted to the global ``.gitignore`` file.
* Run ``travis encrypt-file path/to/clouds.yml``.

  .. code-block:: shell

    $ travis encrypt-file clouds.yml
    encrypting clouds.yml for betacloud/mistral-workflows
    storing result as clouds.yml.enc
    storing secure env variables for decryption

    Please add the following to your build script (before_install stage in your .travis.yml, for instance):

        openssl aes-256-cbc -K $encrypted_bdf29e24ac6e_key -iv $encrypted_bdf29e24ac6e_iv -in clouds.yml.enc -out clouds.yml -d

    Pro Tip: You can add it automatically by running with --add.

    Make sure to add clouds.yml.enc to the git repository.
    Make sure not to add clouds.yml to the git repository.
    Commit all changes to your .travis.yml.
* Extend the ``travis.yml`` file as specified.

  .. code-block:: yaml

     before_install:
       - openssl aes-256-cbc -K $encrypted_bdf29e24ac6e_key -iv $encrypted_bdf29e24ac6e_iv -in clouds.yml.enc -out clouds.yml -d
