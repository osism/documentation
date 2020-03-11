=====
Kolla
=====

Preparations
============

When using overlay configuration files at ``environments/kolla/files/overlays``,
the following overlay files need to be synchronized. Customer specific changes
to the current files need to be copied manually to the new overlay configuration
files.

HAProxy
-------

* When updating to *Rocky* - Synchronize `haproxy.cfg`_ to
  ``environments/kolla/files/overlays/haproxy/haproxy.cfg``.

* When updating to *Stein* - Synchronize `haproxy_main.cfg`_ to
  ``environments/kolla/files/overlays/haproxy/haproxy_main.cfg``. The old
  ``environments/kolla/files/overlays/haproxy/haproxy.cfg`` need to be deleted.

.. _haproxy.cfg: https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/kolla/files/overlays/haproxy/haproxy.cfg.rocky
.. _haproxy_main.cfg: https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/kolla/files/overlays/haproxy/haproxy_main.cfg.stein

Horizon
-------

* The file ``environments/kolla/files/overlays/horizon/local_settings.j2`` need
  to be removed.

* Copy `custom_local_settings`_ to
  ``environments/kolla/files/overlays/horizon/custom_local_settings``.

.. _custom_local_settings: https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/kolla/files/overlays/horizon/custom_local_settings

Backup MariaDB
--------------

Backup MariaDB databases before the upgrade on one of the control nodes:

The password for MariaDB can be found in the file ``environments/kolla/secrets.yml`` in the variable
``database_password``.

.. code-block:: console

   docker exec -t mariadb innobackupex -u root -p DATABASE_PASSWORD /tmp/mariadb
   docker cp mariadb:/tmp/mariadb $PWD/mariadb

See :ref:`MariaDB Backup` for further details.

Upgrading from Ocata to Pike
============================

* https://docs.openstack.org/releasenotes/kolla/pike.html
* https://docs.openstack.org/releasenotes/kolla-ansible/pike.html

Upgrading Docker
----------------

.. note::

   This task is only necessary on Ubuntu 16.04 because the ``python-docker``
   package is outdated.

* When encountering the following error message, Docker need to be upgraded!

.. code-block:: none

   fatal: [20-10.betacloud.xyz]: FAILED! => {"changed": true, "failed": true, "msg": "'Traceback (most recent call last):\\n  File \"/tmp/ansible_Lrxpgg/ansible_module_kolla_docker.py\", line 804, in main\\n    dw = DockerWorker(module)\\n  File \"/tmp/ansible_Lrxpgg/ansible_module_kolla_docker.py\", line 218, in __init__\\n    self.dc = get_docker_client()(**options)\\n  File \"/tmp/ansible_Lrxpgg/ansible_module_kolla_docker.py\", line 201, in get_docker_client\\n    return docker.APIClient\\nAttributeError: \\'module\\' object has no attribute \\'APIClient\\'\\n'"}

See :ref:`Docker` on how to upgrade Docker.

Inventory
---------

* New host groups need to be added to file ``inventory/hosts``:

.. code-block:: ini
   :caption: inventory/hosts

   ##########################################################
   # environment: kolla
   
   [redis:children]
   control
   
   # neutron
   
   [neutron-bgp-dragent:children]
   network
   
   [openvswitch:children]
   network
   compute


Configuration
-------------

* Mistral: Redis is now required by default.
  In file ``environments/kolla/configuration.yml`` the deployment need to be
  enabled by adding parameter ``enable_redis: "yes"``.

  .. code-block:: yaml
     :caption: enviornments/kolla/configuration.yml

     enable_redis: yes

  In file ``environments/kolla/secrets.yml`` new parameter
  ``redis_master_password`` need to be set.

  .. code-block:: console
  
     pwgen -1 32
     aevooVaeceeh2aisaeRah2ufieHee7oh
     ansible-vault edit environments/kolla/secrets.yml
  
  
  .. code-block:: yaml
     :caption: enviornments/kolla/secrets.yml
  
     redis_master_password: aevooVaeceeh2aisaeRah2ufieHee7oh

* Ceilometer: The Ceilometer API was dropped.
  All ``ceilometer / metering`` endpoints from Keystone
  (openstack endpoint list) and the ``ceilometer-api`` host group need to be
  removed.

Notes
-----

* Ceilometer: After the upgrade, the ``ceilometer_api`` container and image
  need to be removed from all control nodes, as well as the configuration
  directory ``/etc/kolla/ceilometer-api``.

Upgrading from Pike to Queens
=============================

* https://docs.openstack.org/releasenotes/kolla/queens.html
* https://docs.openstack.org/releasenotes/kolla-ansible/queens.html

Configuration
-------------

* RabbitMQ: New parameter ``rabbitmq_monitoring_password`` need to be added
  to ``environments/kolla/secrets.yml``

.. code-block:: console

   pwgen -1 32
   we7oey4wifeilieK9ii1uighiraJoWoo
   ansible-vault edit environments/kolla/secrets.yml


.. code-block:: yaml
   :caption: enviornments/kolla/secrets.yml

   rabbitmq_monitoring_password: we7oey4wifeilieK9ii1uighiraJoWoo

Upgrading from Queens to Rocky
==============================

* https://docs.openstack.org/releasenotes/kolla/rocky.html
* https://docs.openstack.org/releasenotes/kolla-ansible/rocky.html

Inventory
---------

* New host groups need to be added to file ``inventory/hosts``:

.. code-block:: ini
   :caption: inventory/hosts

   ##########################################################
   # environment: kolla

   # neutron

   [neutron-infoblox-ipam-agent:children]
   network

   [ironic-neutron-agent:children]
   network

Configuration
-------------

* In file ``environments/kolla/configuration.yml``, if set, change ``serial`` to
  ``kolla_serial``.
* In file ``environments/kolla/files/overlays`` add the gnocci ceph keyfile and
  configuration file to the ``gnocchi`` directory, The ceph keyfiles and
  configuration files in the ``gnocchi-metricd``, ``gnocchi-statsd``, and
  ``gnocchi-api`` directories can be removed.
* The ``glance_registry`` containers on the control nodes can be removed,
  the service was deprecated in *Queens* and will be removed in *Stein* release.

  .. code-block:: console

     docker stop glance_registry
     docker rm glance_registry

Elasticsearch
-------------

Upgrading Elasticsearch might fail, because it still has pending operations when
trying to perform a synced flush. Normally it does not matter if some
logging data is lost while upgrading Elasticsearch, therefore
``osism-kolla deploy elasticsearch`` can be used instead of
``osism-kolla upgrade elasticsearch``, to stop all operations on the cluster
immediately before restarting.

Kibana
------

The Elasticsearch index ``.kibana`` might have to be deleted (or updated) after
the Upgrade. See :ref:`kibana_index_delete`.
Dashboards and saved searches in Kibana, will be lost after deleting the index.

Upgrading from Rocky to Stein
=============================

Inventory
---------

* New host group need to be added to file ``inventory/hosts``:

.. code-block:: ini
   :caption: inventory/hosts

   # neutron

   [neutron-metering-agent:children]
   neutron

MariaDB
-------

* Backups are possible beginning with *Stein* release

.. code-block:: yaml
   :caption: enviornments/kolla/configuration.yml

   enable_mariabackup: "yes"

.. code-block:: yaml
   :caption: enviornments/kolla/secrets.yml

   mariadb_backup_database_password: password

Glance
------

* The location of file
  ``environments/kolla/files/overlays/glance-api/ceph.client.glance.keyring``
  has moved to
  ``environments/kolla/files/overlays/glance/ceph.client.glance.keyring``.

HAProxy
-------

* In file ``environments/kolla/configuration.yml`` set
  ``kolla_enable_tls_internal: "no"``.

* File ``environments/kolla/files/overlays/haproxy/haproxy.cfg`` is no longer
  used and can be deleted.

* File ``environments/kolla/files/overlays/haproxy/haproxy_main.cfg`` need to
  added with the following content:

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

Running the upgrade
===================

When using the ``osism-kolla upgrade`` command, the currently running container
is shut down. Next the Docker image for the upgraded version is pulled, and
finally the new container is started. It might be advisable to first pull the
Docker image and then run ``osism-kolla upgrade``. See
:ref:`Deploying Openstack Services` for how to use ``osism-kolla pull``.

Gathering Ansible facts
-----------------------

.. code-block:: console

   osism-generic facts

Common
------

.. code-block:: console

   osism-kolla upgrade common

HAProxy
-------

.. code-block:: console

   osism-kolla upgrade haproxy

Logging
-------

.. code-block:: console

   osism-kolla upgrade elasticsearch
   osism-kolla upgrade kibana

Infrastructure
--------------

.. code-block:: console

   osism-kolla upgrade memcached
   osism-kolla upgrade mariadb
   osism-kolla upgrade rabbitmq
   osism-kolla upgrade redis
   osism-kolla upgrade openvswitch

Storage (optional)
------------------

.. code-block:: console

   osism-kolla upgrade iscsi
   osism-kolla upgrade multipath

OpenStack services
------------------

.. code-block:: console

   osism-kolla upgrade keystone
   osism-kolla upgrade horizon
   osism-kolla upgrade glance
   osism-kolla upgrade cinder
   osism-kolla upgrade neutron
   osism-kolla upgrade heat
   osism-kolla upgrade placement # beginning from Stein release

Nova
----

* Upgrade nova on the control nodes first:

.. code-block:: console

   osism-kolla upgrade nova -l controller

* Upgrade nova on the compute nodes:

.. code-block:: console

   osism-kolla upgrade nova -l compute

If additional optional services are deployed in your environment, run the
upgrade for those services as well:

.. code-block:: console

   osism-kolla upgrade SERVICE_NAME

After the upgrade
=================

Horizon
-------

* After the upgrade the cache need to be cleaned and regenerated. Run the
  following command on all control nodes:

.. code-block:: console

   docker exec -it horizon rm /var/lib/kolla/.local_settings.md5sum.txt
   docker restart horizon

Elasticsearch
-------------

* After the ugprade of Elasticsearch, the shard allocation need to be enabled.

.. code-block:: console

   curl -X PUT "http://api-int.osism.local:9200/_cluster/settings?pretty" -H 'Content-Type: application/json' -d'
   {
     "persistent": {
       "cluster.routing.allocation.enable": null
     }
   }
   '
