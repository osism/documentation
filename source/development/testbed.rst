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
