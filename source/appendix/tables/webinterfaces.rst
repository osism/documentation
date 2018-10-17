=============
Webinterfaces
=============

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
