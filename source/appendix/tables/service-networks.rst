================
Service networks
================

Active service networks
=======================

=================== ======================================= =====================
**Service**         **Ansible role**                        **Network**
------------------- --------------------------------------- ---------------------
Ceph client         osism.services.cephclient               ``172.31.100.0/28``
OpenStack client    osism.services.openstackclient          ``172.31.100.16/28``
phpMyAdmin          osism.services.phpymyadmin              ``172.31.100.32/28``
Rally               osism.services.rally                    ``172.31.100.48/28``
Adminer             osism.services.adminer                  ``172.31.100.64/28``
Patchman            osism.services.patchman                 ``172.31.100.80/28``
Keycloak            osism.services.keycloak                 ``172.31.100.144/28``
Health Monitor      osism.services.openstack_health_monitor ``172.31.100.160/28``
Netbox              osism.services.netbox                   ``172.31.100.176/28``
Rundeck             osism.services.rundeck                  ``172.31.100.192/28``
Heimdall            osism.services.homer                    ``172.31.100.208/28``
Jenkins             osism.services.jenkins                  ``172.31.100.224/28``
OpenLDAP            osism.services.openldap                 ``172.31.100.240/28``
Manager             osism.services.manager                  ``172.31.101.0/28``
virtualbmc          osism.services.virtualbmc               ``172.31.101.16/28``
Nexus               osism.services.nexus                    ``172.31.101.32/28``
Traefik             osism.services.traefik                  ``172.31.101.48/28``
Atlantis            osism.services.atlantis                 ``172.31.101.64/28``
Dnsdist             osism.services.dnsdist                  ``172.31.101.80/28``
Zuul                osism.services.zuul                     ``172.31.101.96/28``
=================== ======================================= =====================

Deprecated service networks
===========================

=================== ================================== ====================
**Service**         **Ansible role**                   **Network**
------------------- ---------------------------------- --------------------
Prometheus          osism.services.prometheus          ``172.31.102.0/28``
Prometheus exporter osism.services.prometheus-exporter ``172.31.102.16/28``
Pulp                osism.services.pulp                ``172.31.100.96/28``
Zabbix              osism.services.zabbix              ``172.31.100.112/28``
=================== ================================== ====================
