=======
Testbed
=======

* https://github.com/osism/testbed

Prepare
=======

* Create ``clouds.yml`` file
* If necessary, adapt the environment files in the directory ``etc`` (e.g. to set the flavor type or the public network)
* Create stack: ``$ tox -qe full-xenial-ansible25 create``

Deploy
======

* Bootstrap & deploy manager: ``$ tox -qe full-xenial-ansible25 manager``
* Deploy mirror: ``$ tox -qe full-xenial-ansible25 mirror`` (optional)
* Bootstrap nodes: ``$ tox -qe full-xenial-ansible25 bootstrap-nodes``
* Deploy nodes: ``$ tox -qe full-xenial-ansible25 deploy-nodes``

Usage
=====

Information
-----------

.. code-block:: console

   $ tox -qe full-xenial-ansible25 info
   external manager address: 185.136.140.19

   path to private ssh key: environments/manager/files/id_rsa.testbed-full

   ssh username: dragon

   horizon: http://185.136.140.19:8080
   rally: http://185.136.140.19:8090
   phpmyadmin: http://185.136.140.19:8110
   ara dashboard: http://185.136.140.19:8120
   cockpit: https://185.136.140.19:8130
   prometheus: http://185.136.140.19:9090
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
   dragon@TESTBED-FULL-manager:~$

Configuration repository update
-------------------------------

.. code-block:: console

   $ tox -qe full-xenial-ansible25 prepare-manager
   $ tox -qe full-xenial-ansible25 ceph-fetch-keys

Destroy
=======

.. code-block:: console

   $ tox -qe full-xenial-ansible25 destroy
