.. _configuration-environment-monitoring:

==========
Monitoring
==========

Base directory: ``environments/monitoring``

Ceph
====

For Prometheus to be able to scrape data from the Ceph exporter, it needs to know on which node
the exporter runs. You can use any Ceph monitor node here.

* ``environments/monitoring/configuration.yml``

.. code-block:: yaml

   prometheus_scraper_ceph_target_host: 10.0.23.17
