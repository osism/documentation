=====
Kolla
=====

Preparations
============

* HAProxy: when using an overlay configuration file sync it with the new version from https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/kolla/files/overlays/haproxy/haproxy.cfg.RELEASE (for version <= Rocky)

* HAProxy: when using an overlay configuration file sync it with the new version from https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/kolla/files/overlays/haproxy/haproxy_main.cfg.RELEASE (for version <= Stein)

* Horizon: for versions < Rocky: when using an overlay configuration file sync it with the new version from https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/kolla/files/overlays/horizon/local_settings.j2.RELEASE

  * if you upgrade to >= Rocky, this file is removed from the repository

* Horizon: for versions >= Rocky: when using an overlay configuration file environments/kolla/files/overlays/horizon/local_settings.j2 , replace it by https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/kolla/files/overlays/horizon/custom_local_settings

* gather facts with ``osism-generic facts`` before the upgrade

* backup MariaDB databases before the upgrade

Notes
=====

* Horizon: after the upgrade cleanup and regenerate the cached files with ``docker exec -it horizon rm /var/lib/kolla/.local_settings.md5sum.txt && docker restart horizon``

* Nova: Upgrade the controller (``osism-kolla upgrade nova -l controller``) followed by the compute nodes (``osism-kolla upgrade nova -l compute``)

* Elasticsearch: After the ugprade of Elasticsearch enable the shard allocation.

  .. code-block:: console

     curl -X PUT "http://api-int.osism.local:9200/_cluster/settings?pretty" -H 'Content-Type: application/json' -d'
     {
       "persistent": {
         "cluster.routing.allocation.enable": null
       }
     }
     '

Ocata -> Pike
=============

* https://docs.openstack.org/releasenotes/kolla/pike.html
* https://docs.openstack.org/releasenotes/kolla-ansible/pike.html

Docker
------

.. note::

   This task is only necessary on Ubuntu 16.04 because there the ``python-docker`` package is too old.

.. note::

   It's a good idea to do a Docker upgrade as part of an OpenStack upgrade.

.. code-block:: none

   fatal: [20-10.betacloud.xyz]: FAILED! => {"changed": true, "failed": true, "msg": "'Traceback (most recent call last):\\n  File \"/tmp/ansible_Lrxpgg/ansible_module_kolla_docker.py\", line 804, in main\\n    dw = DockerWorker(module)\\n  File \"/tmp/ansible_Lrxpgg/ansible_module_kolla_docker.py\", line 218, in __init__\\n    self.dc = get_docker_client()(**options)\\n  File \"/tmp/ansible_Lrxpgg/ansible_module_kolla_docker.py\", line 201, in get_docker_client\\n    return docker.APIClient\\nAttributeError: \\'module\\' object has no attribute \\'APIClient\\'\\n'"}

.. code-block:: console

   $ osism-generic docker

Inventory
---------

* Add new host groups to ``inventory/hosts`` to the ``environment: kolla`` section

.. code-block:: ini

   # neutron

   [...]

   [neutron-bgp-dragent:children]
   network

.. code-block:: ini

   # neutron

   [...]

   [openvswitch:children]
   network
   compute

.. code-block:: ini

   ##########################################################
   # environment: kolla

   [...]

   [redis:children]
   control

Configuration
-------------

* Mistral: Redis is now required by default, enabled & deploy it (add ``redis`` host group to inventory, enable deployment with ``enable_redis: "yes"`` in ``environments/kolla/configuration.yml``, add ``redis_master_password`` to ``environments/kolla/secrets.yml``)

* Ceilometer: The Ceilometer API was dropped. Remove all ``ceilometer / metering`` endpoints from Keystone (openstack endpoint list) and remove the ``ceilometer-api`` host group from the inventory

Notes
-----

* Ceilometer: After the upgrade remove the ``ceilometer_api`` container & image from all controller nodes and remove the configuration directory ``/etc/kolla/ceilometer-api``

Pike -> Queens
==============

* https://docs.openstack.org/releasenotes/kolla/queens.html
* https://docs.openstack.org/releasenotes/kolla-ansible/queens.html

Configuration
-------------

* RabbitMQ: add new parameter ``rabbitmq_monitoring_password`` to ``secrets.yml``

Queens -> Rocky
===============

* https://docs.openstack.org/releasenotes/kolla/rocky.html
* https://docs.openstack.org/releasenotes/kolla-ansible/rocky.html

Inventory
---------

* Add new host groups to ``inventory/hosts`` to the ``environment: kolla`` section

  .. code-block:: ini

     # neutron

     [...]

     [neutron-infoblox-ipam-agent:children]
     network

     [ironic-neutron-agent:children]
     network

Configuration
-------------

* in ``environments/kolla/configuration.yml`` change ``serial`` to ``kolla_serial``
* in ``environments/kolla/files/overlays`` add the gnocci ceph keyfile and configuration file to the ``gnocchi``
  directory, the ceph keyfiles and configuration files in the ``gnocchi-metricd``, ``gnocchi-statsd``, and ``gnocchi-api``
  directories can be removed
* the ``glance_registry`` containers on the controller nodes can be removed, the service was deprecated in Queens and will be removed in Stein

Elasticsearch
-------------

Upgrading Elasticsearch might fail, because it still has pending operations when trying
to perform a synced flush. Normally it does not matter if you loose some logging data
while upgrading Elasticsearch, so you can use `osism-kolla deploy elasticsearch` instead
of `osism-kolla upgrade elasticsearch`. It basically does the same, but does not wait for
Elasticsearch to stop all operations on the cluster before restarting it.

Kibana
------

You might have to delete (or update) the `.kibana` index in Elasticsearch after the
Upgrade. You will loose dashboards and saved searches in Kibana, if you delete the index.

Rocky -> Stein
==============

Inventory
---------

.. code-block:: ini

   [neutron-metering-agent:children]
   neutron

MariaDB
-------

* backups are possible with >= Stein

  .. code-block:: yaml
     :caption: enviornments/kolla/configuration.yml

     enable_mariabackup: "yes"

  .. code-block:: yaml
     :caption: enviornments/kolla/secrets.yml

     mariadb_backup_database_password: password

Glance
------

* the location of the ``ceph.client.glance.keyring`` changed, move
  ``environments/kolla/files/overlays/glance-api/ceph.client.glance.keyring``
  to ``environments/kolla/files/overlays/glance/ceph.client.glance.keyring``

HAProxy
-------

* add ``kolla_enable_tls_internal: "no"`` to ``environments/kolla/configuration.yml``
* ``environments/kolla/files/overlays/haproxy/haproxy.cfg`` is no longer used
* create ``environments/kolla/files/overlays/haproxy/haproxy_main.cfg`` and add
  custom parameters if necessary

  .. code-block:: none

     #jinja2: lstrip_blocks: True
     global
	 chroot /var/lib/haproxy
	 user haproxy
	 group haproxy
	 daemon
	 log {{ syslog_server }}:{{ syslog_udp_port }} {{ syslog_haproxy_facility }}
	 maxconn {{ haproxy_max_connections }}
	 nbproc {{ haproxy_processes }}
	 {% if (haproxy_processes | int > 1) and (haproxy_process_cpu_map | bool) %}
	     {% for cpu_idx in range(0, haproxy_processes) %}
	 cpu-map {{ cpu_idx + 1 }} {{ cpu_idx }}
	     {% endfor %}
	 {% endif %}
	 stats socket /var/lib/kolla/haproxy/haproxy.sock group kolla mode 660
	 {% if kolla_enable_tls_external | bool or kolla_enable_tls_internal | bool %}
	 ssl-default-bind-ciphers DEFAULT:!MEDIUM:!3DES
	 ssl-default-bind-options no-sslv3 no-tlsv10 no-tlsv11
	 tune.ssl.default-dh-param 4096
	 {% endif %}

     defaults
	 log global
	 option redispatch
	 retries 3
	 timeout http-request {{ haproxy_http_request_timeout }}
	 timeout queue {{ haproxy_queue_timeout }}
	 timeout connect {{ haproxy_connect_timeout }}
	 timeout client {{ haproxy_client_timeout }}
	 timeout server {{ haproxy_server_timeout }}
	 timeout check {{ haproxy_check_timeout }}
	 balance {{ haproxy_defaults_balance }}
	 maxconn {{ haproxy_defaults_max_connections }}

     listen stats
	bind {{ api_interface_address }}:{{ haproxy_stats_port }}
	mode http
	stats enable
	stats uri /
	stats refresh 15s
	stats realm Haproxy\ Stats
	stats auth {{ haproxy_user }}:{{ haproxy_password }}

     frontend status
	 bind {{ api_interface_address }}:{{ haproxy_monitor_port }}
	 {% if api_interface_address != kolla_internal_vip_address %}
	 bind {{ kolla_internal_vip_address }}:{{ haproxy_monitor_port }}
	 {% endif %}
	 mode http
	 monitor-uri /

     # OSISM specific configuration

     listen ceph_dashboard
       option httpchk
       http-check expect status 200
       bind {{ kolla_internal_vip_address }}:8140
     {% for host in groups['ceph-mgr'] %}
       server {{ hostvars[host]['ansible_hostname'] }} {{ hostvars[host]['ansible_' + hostvars[host]['api_interface']]['ipv4']['address'] }}:7000 check inter 2000 rise 2 fall 5
     {% endfor %}

     listen ceph_prometheus
       bind {{ kolla_internal_vip_address }}:9283
     {% for host in groups['ceph-mgr'] %}
       server {{ hostvars[host]['ansible_hostname'] }} {{ hostvars[host]['ansible_' + hostvars[host]['api_interface']]['ipv4']['address'] }}:9283 check inter 2000 rise 2 fall 5
     {% endfor %}

     # customer specific configuration
