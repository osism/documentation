==============
Infrastructure
==============

.. contents::
   :local:

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

.. code-block:: console

   $ osism-kolla deploy haproxy

Logging
=======

.. code-block:: console

   $ osism-kolla deploy elasticsearch
   $ osism-kolla deploy kibana

It is possible that the error ``Your Kibana index is out of date, reset it or use the X-Pack upgrade assistant``
occurs when calling the Kibana Application from the browser (https://github.com/elastic/kibana/issues/14934).

.. image:: /images/kibana-index-out-of-date.png

In this case the ``.kibana`` index must be removed manually.

.. code-block:: console

   $ curl -X DELETE http://KOLLA_INTERNAL_VIP_ADDRESS:9200/.kibana
   {"acknowledged":true}

If the Kibana webinterface is not callable after the first deployment (``503 Service Unavailable``) and a
``docker logs kibana`` shows the error ``Index .kibana belongs to a version of Kibana that cannot be
automatically migrated. Reset it or use the X-Pack upgrade assistant`` the ``.kibana`` index must also
be removed manually.

Then reload the Kibana application in the browser and create a new index
pattern (index pattern: ``flog-*``, time filter field name: ``@timestamp``).
