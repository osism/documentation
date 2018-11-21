=======
Testbed
=======

* https://github.com/osism/testbed

.. image:: /images/testbed-heat-dashboard.png

Prepare
=======

* Create ``clouds.yml`` file

  .. code-block:: yaml

     ---
     clouds:
       testbed:
         auth:
           username: USERNAME
           password: PASSWORD
           project_name: PROJECT
           auth_url: https://api-1.betacloud.io:5000/v3
           project_domain_name: DOMAIN
           user_domain_name: DOMAIN
         interface: public
         identity_api_version: 3
         verify: false
     ansible:
       use_hostnames: True
       expand_hostvars: True
       fail_on_errors: True

* If necessary, adapt the environment files in the directory ``etc`` (e.g. to set the flavor type or the public network)
* Create stack

  .. code-block:: console

     $ tox -qe full create
     info: check if stack exist
     Stack not found: testbed-full
     info: create stack
     2018-11-08 18:56:56Z [testbed-full]: CREATE_IN_PROGRESS  Stack CREATE started
     2018-11-08 18:57:18Z [testbed-full.storage_2_volume_2]: CREATE_IN_PROGRESS  state changed
     [...]
     +---------------------+--------------------------------------+
     | Field               | Value                                |
     +---------------------+--------------------------------------+
     | id                  | c06e2193-b5a2-4bef-9817-66570b731211 |
     | stack_name          | testbed-full                         |
     | description         | No description                       |
     | creation_time       | 2018-11-08T18:56:55Z                 |
     | updated_time        | None                                 |
     | stack_status        | CREATE_COMPLETE                      |
     | stack_status_reason | Stack CREATE completed successfully  |
     +---------------------+--------------------------------------+

.. note::

   Depending on the environment used, the creation of the stack takes a few minutes.

Deploy
======

.. note::

   The versions to be used can be defined by environment variables when deploying the manager.
   The default values are in the ``tox.ini`` file.

   .. code-block:: shell

      export ANSIBLE_VERSION=2.6.0
      export CEPH_VERSION=luminous
      export DOCKER_VERSION=18.06.1
      export OPENSTACK_VERSION=queens
      export OSISM_VERSION=latest
      export UBUNTU_VERSION=16.04

* Bootstrap & deploy manager: ``$ tox -qe full manager``

.. note::

   If the cloud init check fails, restart the manager deployment a few minutes later.
   The initial bootstrap of the manager node is not completed yet.

   .. code-block:: none

      PLAY [Check cloud init] *******************************************************

      TASK [Check /var/lib/cloud/instance/boot-finished] ****************************
      fatal: [testbed-controller-manager.osism.xyz]: FAILED! => {"changed": true,
      [...]

.. note::

   Depending on the environment used, the boostrap of the manager takes some time.

* Bootstrap nodes: ``$ tox -qe full bootstrap-nodes``

.. note::

   Depending on the environment used, the boostrap of the nodes takes some time.

* Reboot nodes: ``$ tox -qe full reboot-nodes``
* Wait for nodes: ``$ tox -qe full wait-for-nodes``

All services
------------

.. code-block:: console

   $ tox -qe full deploy-nodes

Single service
--------------

.. code-block:: console

   $ tox -qe full fabric-rabbitmq

Usage
=====

Information
-----------

.. code-block:: console

   $ tox -qe full info

   environment name: testbed

   Ceph version: luminous
   Docker version: 18.06.1
   OSISM version: latest
   OpenStack version: queens

   path to private ssh key: environments/manager/files/id_rsa.testbed-full
   ssh username: dragon
   external manager address: 185.136.140.36

   ara dashboard: http://185.136.140.36:8120
   cockpit: https://185.136.140.36:8130
   grafana: http://185.136.140.36:3000
   horizon: http://185.136.140.36
   kibana: http://185.136.140.36:5601
   phpmyadmin: http://185.136.140.36:8110
   rabbitmq: http://185.136.140.36:15672
   rally: http://185.136.140.36:8090
   ________________summary _____________________
     full: commands succeeded
     congratulations :)

Login
-----

.. note::

   The login is only possible after the manager's bootstrap.

.. code-block:: console

   $ tox -qe full login
   Last login: Thu Sep 27 14:18:09 2018 from a.b.c.d
   dragon@testbed-full-manager:~$

Configuration repository update
-------------------------------

.. code-block:: console

   $ tox -qe full prepare-manager
   $ tox -qe full ceph-fetch-keys  # optional

Destroy
=======

.. code-block:: console

   $ tox -qe full destroy
   2018-11-08 18:50:09Z [testbed-full]: DELETE_IN_PROGRESS  Stack DELETE started
   2018-11-08 18:50:18Z [testbed-full.controller_2_volume_docker_attachment]: DELETE_IN_PROGRESS  state changed
   2018-11-08 18:50:18Z [testbed-full.storage_3_volume_docker_attachment]: DELETE_IN_PROGRESS  state changed
   [...]
   2018-11-08 18:54:30Z [testbed-full.net_external]: DELETE_COMPLETE  state changed
   2018-11-08 18:54:30Z [testbed-full.net_storage_backend]: DELETE_COMPLETE  state changed
   2018-11-08 18:54:31Z [testbed-full.net_provider]: DELETE_COMPLETE  state changed
   2018-11-08 18:54:31Z [testbed-full]: DELETE_COMPLETE  Stack DELETE completed successfully
