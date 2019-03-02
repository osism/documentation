==============
Infrastructure
==============

Execute the following commands on the manager node.

Common
======

.. code-block:: console

   $ osism-kolla deploy common

Logging
=======

.. code-block:: console

   $ osism-kolla deploy haproxy
   $ osism-kolla deploy elasticsearch
   $ osism-kolla deploy kibana

.. note::

   It is possible that the error ``Your Kibana index is out of date, reset it or use the X-Pack upgrade assistant``
   occurs when calling the Kibana Application from the browser.

   .. image:: /images/kibana-index-out-of-date.png

   In this case the ``.kibana`` index must be removed manually.

   .. code-block:: console

      $ curl -X DELETE http://KOLLA_INTERNAL_VIP_ADDRESS:9200/.kibana
      {"acknowledged":true}

   Then reload the Kibana application in the browser and create a new index
   pattern (index pattern: ``flog-*``, time filter field name: ``@timestamp``).

   https://github.com/elastic/kibana/issues/14934
