======
Kibana
======

.. contents::
   :local:

Search / Discover
=================

https://www.elastic.co/guide/en/kibana/current/search.html

* ``programname:"neutron-server"``
* ``Hostname:"30-10"``

LogTrail
========

https://github.com/sivasamyk/logtrail

Your Kibana index is out of date, reset it or use the X-Pack upgrade assistant.
===============================================================================

.. image:: /images/kibana-index-out-of-date.png

In this case the ``.kibana`` index must be removed manually.

.. code-block:: console

   $ curl -X DELETE http://api-int.osism.local:9200/.kibana
   {"acknowledged":true}

Then reload the Kibana application in the browser and create a new index
pattern (index pattern: ``flog-*``, time filter field name: ``@timestamp``).

https://github.com/elastic/kibana/issues/14934
