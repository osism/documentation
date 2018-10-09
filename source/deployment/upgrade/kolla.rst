=====
Kolla
=====

Ocata -> Pike
=============

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

* HAProxy: when using an overlay configuration file sync it with the Pike version from https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/kolla/files/overlays/haproxy/haproxy.cfg.pike

* Mistral: Redis is now required by default, enabled & deploy it (add ``redis`` host group to inventory, enable deployment with``enable_redis: "yes"``, add ``redis_master_password`` to ``secrets.yml``)

* Ceilometer: The Ceilometer API was dropped. Remove all ``ceilometer / metering`` endpoints from Keystone and remove the ``ceilometer-api`` host group from the inventory

* Horizon: After the upgrade cleanup and regenerate the cached files with ``docker exec -it horizon rm /var/lib/kolla/.local_settings.md6sum.txt && docker restart horizon``

Notes
-----

* Ceilometer: After the upgrade remove the ``ceilometer_api`` container & image from all controller nodes and remove the configuration directory ``/etc/koll/ceilometer-api``

* Nova: Upgrade the controller (``osism-kolla upgrade nova -l controller``) followed by the compute notes (``osism-kolla upgrade nova -l compute``)

Pike -> Queens
==============

Queens -> Rocky
===============
