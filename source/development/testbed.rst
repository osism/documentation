=======
Testbed
=======

* https://github.com/osism/testbed

Create
======

* Create ``clouds.yml`` file
* If necessary, adapt the environment files in the directory ``etc`` (e.g. to set the flavor type or the public network)
* Create stack: ``$ tox -e full-xenial-ansible25 create``
* Deploy manager: ``$ tox -e full-xenial-ansible25 manager``
* Deploy mirror: ``$ tox -e full-xenial-ansible25 mirror`` (optional)

Destroy
=======

.. code-block:: console

   $ tox -e full-xenial-ansible25 destroy

Usage
=====

Information
-----------

.. code-block:: console

   $ tox -e full-xenial-ansible25 info
   full-xenial-ansible25 runtests: PYTHONHASHSEED='1202754648'
   full-xenial-ansible25 runtests: commands[0] | bash scripts/tox.sh info

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

   $ tox -e full-xenial-ansible25 login
