====================
Service architecture
====================

The following sections describe the services that the framework deploys.

Deployment
==========

* Aptly -- repository management tool
* Cobbler -- linux installation server
* OSISM -- OpenStack Infrastructure & Service Manager

Logging
=======

* Elasticsearch
* Fluentd
* Kibana
* Rsyslog

Monitoring
==========

* Grafana
* Icinga2
* Prometheus

Infrastructure
==============

* HAProxy / Keepalived
* MariaDB Galera Cluster
* Memcached
* RabbitMQ Cluster

OpenStack
=========

* Aodh
* Ceilometer
* Cinder
* Glance
* Gnocchi
* Heat
* Horizon
* Keystone
* Magnum
* Mistral
* Nova
* Panko

Compute
=======

* KVM

.. note::

   It is possible to integrate external virtualization solutions.

Storage
=======

* Ceph
* Swift

.. note::

   It is possible to integrate external storage backends.
