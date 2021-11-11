==============
Infrastructure
==============

.. contents::
   :depth: 2

Common
======

.. code-block:: console

   $ osism-kolla deploy common

The common role includes the following services:

* cron
* fluentd
* kolla_toolbox

HAProxy
=======

Please read certificate configuration :ref:`haproxy-self-signed-cert`

For using ``spice`` as ``nova_console`` please read :ref:`nova-console-spice`

.. code-block:: console

   $ osism-kolla deploy haproxy

.. _kibana_index_delete:

Logging
=======

.. code-block:: console

   $ osism-kolla deploy elasticsearch
   $ osism-kolla deploy kibana

It could be necessary to restart ``fluentd`` container, e.g. during training sessions.

.. code-block:: console

   $ docker restart fluentd

It is possible that the error ``Your Kibana index is out of date, reset it or use the X-Pack upgrade assistant``
occurs when calling the Kibana Application from the browser

https://github.com/elastic/kibana/issues/14934

.. image:: /images/kibana-index-out-of-date.png

In this case the ``.kibana`` index must be removed manually.

.. code-block:: console

   $ curl -X DELETE http://api-int.osism.local:9200/.kibana
   {"acknowledged":true}

Login to Kibana webinterface ``http://KOLLA_INTERNAL_VIP_ADDRESS:5601/`` with username
``kibana`` and the password located at ``environments/kolla/secrets.yml`` in the
variable ``kibana_password``.

If the Kibana webinterface is not callable after the first deployment (``503 Service Unavailable``) and a
``docker logs kibana`` shows the error ``Index .kibana belongs to a version of Kibana that cannot be
automatically migrated. Reset it or use the X-Pack upgrade assistant`` the ``.kibana`` index must also
be removed manually.

Then reload the Kibana application in the browser and create a new index
pattern (index pattern: ``flog-*``, time filter field name: ``@timestamp``).

Openstack-Client
================

.. code-block:: console

   $ osism-infrastructure openstackclient

You can if needed deploy the Openstackclient.
For configuration of the client see :ref:`how to test Openstack-Client <test-openstack>`.
