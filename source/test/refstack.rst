========
RefStack
========

.. contents::
   :local:

RefStack is a source of tools for OpenStack interoperability testing.

* https://refstack.openstack.org

Installation
============

.. code-block:: console

   $ git clone https://github.com/openstack/refstack-client
   $ cd refstack-client
   $ ./setup_env

Preparation
===========

* Create required project with at least two user accounts, the role ``_member_`` is sufficient.
* Set the project quota high enough.
* Create a network and a router in the project, assign a gateway to the router, add the network as
  an interface to the router.

Configuration
=============

* ``accounts.yaml``

.. code-block:: yaml

   ---
   - username: svc-refstack-0
     tenant_name: refstack
     password: password

   - username: svc-refstack-1
     tenant_name: refstack
     password: password

* minimal ``tempest.conf`` (https://docs.openstack.org/tempest/latest/sampleconf.html)

.. code-block:: ini

   [auth]
   test_accounts_file = /absolute/path/to/accounts.yaml
   use_dynamic_credentials = false

   [oslo_concurrency]
   lock_path = /tmp/tempest

   [service_available]
   cinder = false
   glance = false
   neutron = false
   nova = false
   swift = false

   [identity]
   auth_version = v3
   region = betacloud-1
   uri_v3 = https://api-1.betacloud.io:5000/v3
   v3_endpoint_type = public

   [identity-feature-enabled]
   api_v2 = false

.. note::

   For the test of Cinder, Glance, Heat, Neutron & Swift no further parameters are necessary,
   these can simply be additionally activated.
   To run all tests, you need some additional parameters:

.. code-block:: ini

   [compute]
   image_ref = 6dd3ee6b-261a-450a-9620-702812ab4259
   image_ref_alt = dd516d0e-8c56-42c9-b801-9169b959fdea
   flavor_ref = 2fe23ff9-c60d-4265-8bad-f7d7ac302db6
   flavor_ref_alt = a5a35226-75c5-41ee-a5c2-19710401c9f7
   fixed_network_name = refstack-internal-net

Execution
=========

* https://refstack.openstack.org/#/guidelines

.. code-block:: console

   $ source .venv/bin/activate
   $ refstack-client test -c tempest.conf -v -- --regex tempest.api.identity.v3.test_tokens.TokensV3Test.test_create_token

.. code-block:: console


   $ wget "https://refstack.openstack.org/api/v1/guidelines/2018.02/tests?target=platform&type=required&alias=true&flag=false" -O 2018.02-test-list.txt
   $ refstack-client test -c tempest.conf -v --test-list 2018.02-test-list.txt

Troubleshooting
===============

* https://arxcruz.net/index.php/2017/09/21/debugging-tempest/
