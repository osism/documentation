========
RefStack
========

RefStack is a source of tools for OpenStack interoperability testing.

Installation
============

.. code-block:: shell

   $ git clone https://github.com/openstack/refstack-client
   $ cd refstack-client
   $ git clone https://github.com/openstack/tempest.git .tempest
   $ virtualenv .tempest/.venv
   $ source .tempest/.venv/bin/activate
   $ pip install tempest
   $ virtualenv .venv
   $ source .venv/bin/activate
   $ pip install -e .

Preparation
===========

* Create required testbed project with at least two user accounts, the role ``_member_`` is sufficient.
* Set the project quota high enough.
* Create a network and a router in the project, assign a gateway to the router, add the network as
  an interface to the router.

Configuration
=============

accounts.yaml
-------------

.. code-block:: yaml

   ---
   - username: refstack-0
     tenant_name: refstack
     password: password

   - username: refstack-1
     tenant_name: refstack
     password: password

Minimal tempest.conf
--------------------

.. code-block:: ini

   [auth]
   test_accounts_file = /path/to/accounts.yaml
   use_dynamic_credentials = false

   [oslo_concurrency]
   lock_path = /tmp/tempest

   [service_available]
   cinder = true
   glance = true
   neutron = false
   nova = false

   [identity]
   auth_version = v3
   region = betacloud-1
   uri_v3 = https://api-1.betacloud.io:5000/v3
   v3_endpoint_type = public

.. note::

   For the test of Cinder, Glance, Heat, Neutron & Swift no further parameters are necessary,
   these can simply be additionally activated.

Extended tempest.conf
---------------------

.. todo::

   Add extended tempest.conf configuration file here.

Execution
=========

.. code-block:: shell

.. code-block:: shell

   $ wget "https://refstack.openstack.org/api/v1/guidelines/2017.09/tests?target=compute&type=required&alias=true&flag=true" -O 2017.09-test-list.txt

.. code-block:: shell

   $ source .venv/bin/activate
   $ refstack-client test -c tempest.conf -v --test-list 2017.09-test-list.txt

References
==========

* https://arxcruz.net/index.php/2017/09/21/debugging-tempest/
* https://docs.openstack.org/tempest/latest/sampleconf.html
* https://github.com/openstack/refstack-client
* https://refstack.openstack.org/#/
* https://refstack.openstack.org/#/guidelines
