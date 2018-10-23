=======
Testbed
=======

* https://github.com/osism/testbed

.. image:: /images/testbed-heat-dashboard.png

Prepare
=======

* Create ``clouds.yml`` file
* If necessary, adapt the environment files in the directory ``etc`` (e.g. to set the flavor type or the public network)
* Create stack: ``$ tox -qe full-xenial-ansible25 create``

.. note::

   Depending on the environment used, the creation of the stack takes a few minutes.

Deploy
======

* Bootstrap & deploy manager: ``$ tox -qe full-xenial-ansible25 manager``

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

* Bootstrap nodes: ``$ tox -qe full-xenial-ansible25 bootstrap-nodes``

.. note::

   Depending on the environment used, the boostrap of the nodes takes some time.

* Reboot nodes: ``$ tox -qe full-xenial-ansible25 reboot-nodes``

All services
------------

.. code-block:: console

   $ tox -qe full-xenial-ansible25 deploy-nodes

Single service
--------------

.. code-block:: console

   $ tox -qe full-xenial-ansible25 deploy-rabbitmq

Usage
=====

Information
-----------

.. code-block:: console

   $ tox -qe full-xenial-ansible25 info
   external manager address: 185.136.140.19

   path to private ssh key: environments/manager/files/id_rsa.testbed-full

   ssh username: dragon

   ara dashboard: http://185.136.140.17:8120
   cockpit: https://185.136.140.17:8130
   grafana: http://185.136.140.17:3000
   horizon: http://185.136.140.17
   kibana: http://185.136.140.17:5601
   phpmyadmin: http://185.136.140.17:8110
   rabbitmq: http://185.136.140.17:15672
   rally: http://185.136.140.17:8090
   ________________mmary _____________________
     full-xenial-ansible25: commands succeeded
     congratulations :)

Login
-----

.. note::

   The login is only possible after the manager's bootstrap.

.. code-block:: console

   $ tox -qe full-xenial-ansible25 login
   Last login: Thu Sep 27 14:18:09 2018 from a.b.c.d
   dragon@testbed-full-manager:~$

Configuration repository update
-------------------------------

.. code-block:: console

   $ tox -qe full-xenial-ansible25 prepare-manager
   $ tox -qe full-xenial-ansible25 ceph-fetch-keys  # optional

Destroy
=======

.. code-block:: console

   $ tox -qe full-xenial-ansible25 destroy
