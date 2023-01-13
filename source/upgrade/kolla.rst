=====
Kolla
=====

Kolla Preparations
==================

When using overlay configuration files at ``environments/kolla/files/overlays``,
the following overlay files need to be synchronized. Customer specific changes
to the current files need to be copied manually to the new overlay configuration
files.

HAProxy Preparations
--------------------

* When updating to *Rocky* - Synchronize `haproxy.cfg`_ to

  ``environments/kolla/files/overlays/haproxy/haproxy.cfg``.

* When updating to *Stein* - Synchronize `haproxy_main.cfg`_ to

  ``environments/kolla/files/overlays/haproxy/haproxy_main.cfg``

  The old ``environments/kolla/files/overlays/haproxy/haproxy.cfg`` need to be deleted.

.. _haproxy.cfg: https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/kolla/files/overlays/haproxy/haproxy.cfg.rocky
.. _haproxy_main.cfg: https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/kolla/files/overlays/haproxy/haproxy_main.cfg.stein

Horizon Preparations
--------------------

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

See :ref:`mariadb_backup` for further details.

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

   osism apply facts

Upgrade Common
--------------

.. code-block:: console

   osism-kolla upgrade common

Upgrade HAProxy
---------------

.. code-block:: console

   osism-kolla upgrade loadbalancer

Upgrade Logging
---------------

.. code-block:: console

   osism-kolla upgrade elasticsearch
   osism-kolla upgrade kibana

Upgrade Infrastructure
----------------------

.. code-block:: console

   osism-kolla upgrade memcached
   osism-kolla upgrade mariadb
   osism-kolla upgrade rabbitmq
   osism-kolla upgrade redis
   osism-kolla upgrade openvswitch

Upgrade Storage (optional)
--------------------------

.. code-block:: console

   osism-kolla upgrade iscsi
   osism-kolla upgrade multipathd

Upgrade OpenStack Services
--------------------------

.. code-block:: console

   osism-kolla upgrade keystone
   osism-kolla upgrade horizon
   osism-kolla upgrade glance
   osism-kolla upgrade cinder
   osism-kolla upgrade neutron
   osism-kolla upgrade heat
   osism-kolla upgrade placement # beginning from Stein release

Upgrade Nova
------------

* Upgrade nova on the control nodes first:

.. code-block:: console

   osism-kolla upgrade nova -l control

* Upgrade nova on the compute nodes:

.. code-block:: console

   osism-kolla upgrade nova -l compute

If additional optional services are deployed in your environment, run the
upgrade for those services as well:

.. code-block:: console

   osism-kolla upgrade SERVICE_NAME

After the upgrade
=================

Fix Horizon
-----------

* After the upgrade the cache need to be cleaned and regenerated. Run the
  following command on all control nodes:

.. code-block:: console

   docker exec -it horizon rm /var/lib/kolla/.local_settings.md5sum.txt
   docker restart horizon

Fix Elasticsearch
-----------------

* After the ugprade of Elasticsearch, the shard allocation need to be enabled.

.. code-block:: console

   curl -X PUT "http://api-int.osism.local:9200/_cluster/settings?pretty" -H 'Content-Type: application/json' -d'
   {
     "persistent": {
       "cluster.routing.allocation.enable": null
     }
   }
   '

Remove old Docker images
========================

Verify none of the old images is running anymore.

.. code-block:: console

   docker ps --filter=label=de.osism.release.openstack=victoria

Remove old version images.

.. code-block:: console

   docker rmi $(docker image ls --quiet --filter=label=de.osism.release.openstack=victoria)
