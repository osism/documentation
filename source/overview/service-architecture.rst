====================
Service architecture
====================

The following sections describe the services which are deployed by the framework.

Infrastructure
==============

* ARA -- records Ansible playbook runs
* Homer -- operations dashboard
* Netbox -- IP address management (IPAM) and data center infrastructure management (DCIM) tool
* OSISM -- Open Source Infrastructure & Service Manager
* Patchman -- Linux Patch Status Monitoring System
* phpMyAdmin -- administration tool for MySQL and MariaDB
* Nexus

.. note::

   It is possible to integrate other services. Support for additional services on request (info@osism.tech).

Logging & Monitoring
====================

* Elasticsearch
* Fluentd
* Grafana
* Kibana
* Netdata
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
* Keycloak

.. note::

   Clustered services can also be run as single instance.

Controller
==========

* Aodh, Ceilometer, Gnocchi -- telemetry framework
* Barbican -- key management service
* Cinder -- block storage service
* Cloudkitty -- billing service
* Designate -- DNS service
* Glance -- image service
* Heat -- orchestration service
* Horizon -- dashboard
* Ironic -- baremetal service
* Keystone -- identity service
* Magnum -- container infrastructure management service
* Manila -- shared filesystems service
* Mistral -- workflow service
* Nova -- compute service
* Octavia -- loadbalancer service
* Placement -- resource provider inventory allocation service
* Rally -- benchmark service
* Senlin -- clustering service for managing homogeneous objects

.. note::

   It is possible to integrate other services. Support for additional services on request (info@osism.tech).

Resources
=========

Compute
-------

* KVM
* QEMU

.. note::

   It is possible to integrate other hypervisors. Support for other hypervisors on request (info@osism.tech).

   A list of supported hypervisors can be found at

   https://docs.openstack.org/nova/queens/admin/configuration/hypervisors.html.

Network
-------

* Open Virtual Network (OVN)
* Open vSwitch (OVS)

.. note::

   It is possible to integrate other network backends. Support for other network backends on request (info@osism.tech).

   A list of supported network drivers can be found at

   https://github.com/openstack?q=networking.

.. warning::

    Not supported feature
 
    * Distributed Virtual Routing (DVR), Octavia won't work 
    * Linux Bridge (Kolla discontinued support)

Storage
-------

* Ceph (including RGW/S3 and CephFS)
* GlusterFS

.. note::

   It is possible to integrate other storage backends. Support for other storage backends on request (info@osism.tech).

   A list of possible storage drivers can be found at

   https://docs.openstack.org/cinder/queens/configuration/block-storage/volume-drivers.html.
