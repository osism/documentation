=======
Testbed
=======

* https://github.com/osism/testbed

Preparations
============

Generic
-------

* Create ``clouds.yml`` file
* Set type: ``export TYPE=manager`` (possible types: ``ceph``, ``controller``, ``full``, ``kolla``, ``manager``, default is ``manager``)
* If necessary, adapt the environment files in the directory ``etc`` (e.g. to set the flavor type or the public network)

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

.. note::

   When deploying the AIO environment (``TYPE=manager``), this step can be omitted.

Deployment
==========

.. code-block:: console

   $ ./scripts/030-deploy.sh

Specific service
----------------

.. code-block:: console

   $ ./scripts/030-deploy.sh monitoring

All-in-one
----------

If the type ``manager`` is used, an all-in-one deployment can be performed after the deployment of the manager.

.. code-block:: console

   $ ./scripts/030-deploy.sh single

.. note::

   Currently the all-in-one environment does not include Ceph.

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

   path to private ssh key: environments/manager/files/id_rsa.testbed-manager

   ssh username: dragon

   horizon: http://1.2.3.4:8080
   rally: http://1.2.3.4:8090
   phpmyadmin: http://1.2.3.4:8110
   ara dashboard: http://1.2.3.4:8120
   cockpit: https://1.2.3.4:8130
   prometheus: http://1.2.3.4:9090

Destroy
=======

.. code-block:: console

   $ ./scripts/999-destroy.sh
