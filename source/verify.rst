================
Verify operation
================

.. toctree::
   :maxdepth: 2

   verify/elasticsearch
   verify/grafana
   verify/haproxy
   verify/kibana
   verify/mariadb
   verify/memcached
   verify/rabbitmq
   verify/keystone
   verify/glance
   verify/cinder

Prepare OpenStack environment
=============================

For the verification of the OpenStack services it is necessary to prepare the OpenStack enviornment in the configuration repository.
The ``clouds.yml`` file should be adapted accordingly. It is not recommended to store passwords in plain text in the confiugration repository.

.. code-block:: yaml

   ---
   clouds:
     testbed:
       auth:
         username: testbed
         password: password
         project_name: testbed
        auth_url: https://api-1.betacloud.io:5000/v3
        project_domain_name: default
        user_domain_name: default
      identity_api_version: 3
      verify: false

A project ``testbed`` and a user ``testbed`` are to be created accordingly.
