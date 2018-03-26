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

* Prepare nodes
  ``./scripts/020-prepare-nodes.sh``
* Bootstrap nodes
  ``./scripts/025-bootstrap-nodes.sh``

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
   Last login: Mon Mar 26 08:43:34 2018 from 185.136.140.18
   dragon@testbed-manager:~$
