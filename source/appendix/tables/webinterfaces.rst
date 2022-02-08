=============
Webinterfaces
=============

The following services are accessible with a webbrowser. The used interface, nodes and port are
configurable in the configuration repository.

=============== ======== ====================== ================== ============ ===========================
**Service**     **Port** **Interface/Address**  **Node**           **Username** **Password**
--------------- -------- ---------------------- ------------------ ------------ ---------------------------
ARA             8120     ``console_interface``  manager            n/a          n/a
Ceph dashboard  8140     ``kolla_internal_vip`` network/controller admin        n/a
Cockpit         8130     ``console_interface``  manager            dragon       ``operator_password``
Grafana         3000     ``kolla_internal_vip`` network/controller grafana      ``grafana_admin_password``
Heimdall        8080     ``console_interface``  manager            n/a          n/a
Horizon           80     ``kolla_internal_vip`` network/controller admin        ``keystone_admin_password``
Horizon w/ TLS   443     ``kolla_external_vip`` network/controller admin        ``keystone_admin_password``
Jenkins         4441     ``console_interface``  manager            jenkins      ``jenkins_password``
Kibana          5601     ``kolla_internal_vip`` network/controller kibana       ``kibana_password``
Netbox          8121     ``console_interface``  manager            admin        ``netbox_superuser_password``
Nexus           8190     ``console_interface``  manager            admin        n/a
Patchman        8150     ``console_interface``  manager            patchman     ``patchman_password``
Prometheus      9090     ``kolla_internal_vip`` network/controller n/a          n/a
RabbitMQ        15672    ``kolla_internal_vip`` network/controller openstack    ``rabbitmq_password``
Rally           8180     ``console_interface``  manager            n/a          n/a
Rundeck         4440     ``console_interface``  manager            n/a          n/a
phpMyAdmin      8110     ``console_interface``  manager            root         ``database_password``
Keycloak        8170     ``console_interface``  manager
UMC             8191     ``console_interface``  manager
UMC w/ TLS      8192     ``console_interface``  manager
Zabbix          8160     ``console_interface``  manager
Vault           8200     ``console_interface``  manager
Cgit            8210     ``console_interface``  manager
=============== ======== ====================== ================== ============ ===========================

``operator_password`` can be found in file ``environments/secrets.yml``. All other passwords can be found
in file ``environments/kolla/secrets.yml``.

For Nexus, run the following on the manager node to read out the initial admin password:

.. code-block:: console

   $ docker exec -it nexus cat /nexus-data/admin.password
   c79304f7-e9db-4b5d-a48a-0678cc0efcdf
