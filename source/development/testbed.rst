=======
Testbed
=======

* https://github.com/osism/testbed

Preparations
============

Generic
-------

* Create ``clouds.yml`` file
* Set type: ``export TYPE=ceph`` (possible types: ceph, controller, full, kolla, manager)

Stack
-----

* Create stack
  ``./scripts/000-manage-stack.sh``

Manager
-------

* Bootstrap manager
  ``./scripts/005-bootstrap-manager.sh``
* Prepare manager
  ``./scripts/007-prepare-manager.sh``
* Deploy manager
  ``./scripts/010-deploy-manager.sh``

Nodes
-----
* Bootstrap nodes
  ``./scripts/020-bootstrap-nodes.sh``

Deployment
==========

.. code-block:: console

   $ ./scripts/030-deploy.sh

Specific service
----------------

.. code-block:: console

   $ ./scripts/030-deploy.sh monitoring

Login
=====

.. code-block:: console

   $ ./scripts/800-ssh.sh 
   info: prepare virtual environment
   info: install required ansible roles
   info: check if stack exist
   info: get external manager address
   info: get internal manager address
   Last login: Mon Mar 26 08:43:34 2018 from 1.2.3.4
   dragon@testbed-manager:~$

.. code-block:: console

   $ ./scripts/801-info.sh
   info: prepare virtual environment
   info: install required ansible roles
   info: check if stack exist
   info: get external manager address
   info: get internal manager address

   external manager address: 1.2.3.4

   path to private ssh key: environments/manager/files/id_rsa.testbed-full

   ssh username: dragon

   rally: http://1.2.3.4:8090
   phpmyadmin: http://1.2.3.4:8110
   ara dashboard: http://1.2.3.4:8120
   prometheus: http://1.2.3.4:9090
