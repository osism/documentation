======
Kibana
======

Search / Discover
=================

* https://www.elastic.co/guide/en/kibana/current/search.html

* ``programname:"neutron-server"``
* ``Hostname:"30-10"``

LogTrail
========

* https://github.com/sivasamyk/logtrail

Your Kibana index is out of date, reset it or use the X-Pack upgrade assistant.
===============================================================================

.. code-block:: console

   $ curl -X DELETE  http://10.49.0.100:9200/.kibana
   {"acknowledged":true}
