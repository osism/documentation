====================
Service architecture
====================

The following sections describe the services which are deployed by the framework.

Infrastructure
==============

* ARA -- records Ansible playbook runs
* Aptly -- repository management tool
* Cobbler -- Linux installation server
* Dokuwiki -- simple to use Wiki software
* Netbox -- IP address management (IPAM) and data center infrastructure management (DCIM) tool
* OSISM -- Open Source Infrastructure & Service Manager
* Registry - Docker registry server
* phpMyAdmin -- administration tool for MySQL and MariaDB

.. note::

   It is possible to integrate other services. Support for additional services on request (info@betacloud-solutions.de).

Logging & Monitoring
====================

* Elasticsearch
* Fluentd
* Grafana
* Icinga2
* Kibana
* Prometheus
* Rsyslog

.. note::

   The integration into existing monitoring systems is possible.

.. note::

   The integration of other systems, e.g. firewall appliances or network hardware, is possible.

Shared services
===============

* HAProxy / Keepalived
* MariaDB Galera Cluster
* Memcached
* RabbitMQ Cluster
* Redis

.. note::

   Clustered services can also be run as single instance.

Controller
==========

* Aodh, Ceilometer, Gnocchi, Panko -- telemetry framework
* Barbican -- key management service
* Cinder -- block storage service
* Cloudkitty -- billing service
* Glance -- image service
* Heat -- orchestration service
* Horizon -- dashboard
* Keystone -- identity service
* Magnum -- container infrastructure management service
* Manila -- shared filesystems service
* Mistral -- workflow service
* Nova -- compute service
* Octavia -- loadbalancer service
* Rally -- benchmark service
* Searchlight -- indexing and search service
* Watcher -- optimization service

.. note::

   It is possible to integrate other services. Support for additional services on request (info@betacloud-solutions.de).

Resources
=========

Compute
-------

* KVM
* QEMU

.. note::

   It is possible to integrate other hypervisors. Support for other hypervisors on request (info@betacloud-solutions.de).

   A list of supported hypervisors can be found at https://docs.openstack.org/nova/queens/admin/configuration/hypervisors.html.

Network
-------

* Linux Bridge
* Open Virtual Network
* Open vSwitch

.. note::

   It is possible to integrate other network backends. Support for other network backends on request (info@betacloud-solutions.de).

   A list of supported network drivers can be found at https://github.com/openstack?q=networking.

Storage
-------

* Ceph
* GlusterFS

.. note::

   It is possible to integrate other storage backends. Support for other storage backends on request (info@betacloud-solutions.de).

   A list of possible storage drivers can be found at https://docs.openstack.org/cinder/queens/configuration/block-storage/volume-drivers.html.
