====================
Service architecture
====================

The following sections describe the services that the framework deploys.

Infrastructure
==============

* ARA -- records Ansible playbook runs
* Aptly -- repository management tool
* Cobbler -- linux installation server
* Dokuwiki -- simple to use wiki software
* Netbox -- IP address management (IPAM) and data center infrastructure management (DCIM) tool
* OSISM -- OpenStack Infrastructure & Service Manager
* Registry - docker registry server
* phpMyAdmin -- administration tool for MySQL and MariaDB

.. note::

   It is possible to integrate other services. The support of an other service on request (info@osism.io).

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

   The integration into an existing monitoring is also possible.

.. note::

   The integration of other systems, e.g. firewall appliances or network hardware, is possible.

Shared services
===============

* HAProxy / Keepalived
* MariaDB Galera Cluster
* Memcached
* RabbitMQ Cluster

.. note::

   Clustered services can also be run as a single instance.

Controller
==========

* Aodh, Ceilometer, Gnocchi, Panko -- telemetry framework
* Cinder -- block storage service
* Glance -- image service
* Heat -- orchestration service
* Horizon -- dashboard
* Keystone -- identity service
* Magnum -- container infrastructure management service
* Mistral -- workflow service
* Nova -- compute service

.. note::

   It is possible to integrate other OpenStack services. The support of an other OpenStack service on request (info@osism.io).

Resources
=========

Compute
-------

* KVM
* QEMU

.. note::

   It is possible to integrate other hypervisors. The support of an other hypervisor on request (info@osism.io).

   A list of possible hypervisors can be found on https://docs.openstack.org/nova/queens/admin/configuration/hypervisors.html.

Network
-------

* Open vSwitch
* Linux Bridge

.. note::

   It is possible to integrate other network backends. The support of an other network backend on request (info@osism.io).

   A list of possible network drivers can be found on https://github.com/openstack?q=networking.

Storage
-------

* Ceph

.. note::

   It is possible to integrate other storage backends. The support of an other storage backend on request (info@osism.io).

   A list of possible storage drivers can be found on https://docs.openstack.org/cinder/queens/configuration/block-storage/volume-drivers.html.

Service Overview
================

The following services are accessible with a webbrowser. The used interface, nodes and port are
configurable in the configuration repository.

=============== ======== ================== ==================
**Service**     **Port** **Interface**      **Node**
--------------- -------- ------------------ ------------------
ARA             8120     console_interface  manager
Ceph dashboard  7000     kolla_internal_vip network/controller
Cockpit         8130     console_interface  manager
Grafana         3000     kolla_external_vip network/controller
Grafana         3000     kolla_internal_vip network/controller
Horizon           80     kolla_external_vip network/controller
Horizon           80     kolla_internal_vip network/controller
Horizon w/ TLS   443     kolla_external_vip network/controller
Kibana          5601     kolla_external_vip network/controller
Kibana          5601     kolla_internal_vip network/controller
phpMyAdmin      8110     console_interface  manager
Prometheus      9090     kolla_internal_vip network/controller
Rally           8090     console_interface  manager
=============== ======== ================== ==================
