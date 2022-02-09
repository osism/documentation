==========
Monitoring
==========

The monitoring system comprises of Prometheus and Grafana. Prometheus is
configured as data collector and alert manager. Grafana is used for
visualisation. Grafana can also be configured as alert manager. The alert
manager is responsible for sending notifications via various communication
channels like Email, Slack, PagerDuty and several others.

Prepare configuration repository
================================

* enable Prometheus/Grafana in ``environments/kolla/configuration.yml``

.. code-block:: yaml

   enable_grafana: "yes"
   enable_prometheus: "yes"

* Data retention policies for Prometheus can be configured via command line
  arguments:

.. code-block:: yaml

   prometheus_cmdline_extras: "--storage.tsdb.retention.time=90d --storage.tsdb.retention.size=50GB"

* Grafana unified alerting can be enabled as following.
  See `Grafana documentation <https://grafana.com/docs/grafana/latest/alerting/unified-alerting/>`_.
  With Grafana unified alerting the alerts from Prometheus can be handled within
  Grafana.  Add the file ``environments/kolla/files/overlays/grafana/grafana.ini``
  with the following content to the configuration repository.

.. code-block:: yaml

   [alerting]
   enabled = false

   [unified_alerting]
   enabled = true

   [smtp]
   enable = true
   from_address = alerts@osism.local

* Add Prometheus rule files and Grafana dashboards to the configuation
  repository. Clone the `kolla-operations <https://github.com/osism/kolla-operations.git>`_
  repository and copy all files from grafana and prometheus directory to the
  configuration repository. This will install a set of metrics definitions and
  alert rules for OpenStack services.

.. code-block:: shell

   git clone https://github.com/osism/kolla-operations.git
   cp -r kolla-operations/grafana cfg-osism/environments/kolla/files/overlays/
   cp -r kolla-operations/prometheus cfg-osism/environments/kolla/files/overlays/

* If you want to use Prometheus alert manager, place the configuration in
  ``environments/kolla/files/overlays/prometheus/prometheus-alertmanager.yml``.
  See `Prometheus alert manager documentation <https://prometheus.io/docs/alerting/latest/configuration/>`_.

.. code-block:: yaml

   ---
   global:
     resolve_timeout: 5m
     smtp_require_tls: false
     smtp_smarthost: localhost:25
     smtp_from: alerts@osism.local
   route:
     receiver: default-receiver
     group_wait: 30s
     group_interval: 5m
     repeat_interval: 4h
   receivers:
     - name: default-receiver
       email_configs:
         - to: monitoring@osism.local
           send_resolved: true

Run Monitoring deployment
=========================

Run Prometheus and Grafana deployments:

.. code-block:: console

   osism-kolla deploy prometheus
   osism-kolla deploy grafana

* The Grafana Dashboard will be available on the internal network at
  ``http://api-int.osism.local:3000``.

* The Prometheus web console will be available on the internal network at
  ``http://api-int.osism.local:9091``.

* The Prometheus Alert Manager web console will be available on the internal
  network at ``http://api-int.osism.local:9093``.
