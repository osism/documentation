====================
Ceph RGW integrating with OpenStack Keystone
====================

Prepare configuration repository
================================

For Ceph-Ansible add following  ceph_conf_overrides in ``environments/ceph/configuration.yml`` to config:

.. code-block:: yaml

  ceph_conf_overrides:

    "client.rgw.{{ hostvars[inventory_hostname]['ansible_hostname'] }}.rgw0":
      "rgw content length compat": "true"
      "rgw enable apis": "swift, s3, swift_auth, admin"
      "rgw keystone accepted roles": "_member_, member, admin"
      "rgw keystone accepted admin roles": "admin"
      "rgw keystone admin domain": "default"
      "rgw keystone admin password": "{{ ceph_rgw_keystone_password }}"
      "rgw keystone admin project": "service"
      "rgw keystone admin tenant": "service"
      "rgw keystone admin user": "ceph_rgw"
      "rgw keystone api version": "3"
      "rgw keystone url": "https://api-int.testbed.osism.xyz:5000"
      "rgw keystone verify ssl": "false"
      "rgw keystone implicit tenants": "true"
      "rgw s3 auth use keystone": "true"
      "rgw swift account in url": "true"
      "rgw swift versioning enabled": "true"
      "rgw verify ssl": "true"
      "rgw enforce swift acls": "true"

Copy the ``ceph_rgw_keystone_password`` from ``environments/kolla/secrets.yml`` to ``environments/ceph/secrets.yml``

.. code-block:: yaml

  ceph_rgw_keystone_password: <copy from environments/kolla/secrets.yml >

Add following configuration in ``environments/kolla/configuration.yml``

.. code-block:: yaml

  enable_ceph_rgw: true # Feature from Xena onwards
  enable_swift: false # Feature for swift on disk, not through ceph.
  enable_swift_s3api: true
  enable_ceph_rgw_keystone: true
  ceph_rgw_swift_compatibility: false
  ceph_rgw_swift_account_in_url: true
  enable_ceph_rgw_loadbalancer: true
  ceph_rgw_hosts:
    - host: testbed-node-0
      ip: 192.168.16.10
      port: 8081
    - host: testbed-node-1
      ip: 192.168.16.11
      port: 8081
    - host: testbed-node-2
      ip: 192.168.16.12
      port: 8081


Run Ceph rgws and kolla ceph-rgw deployment 
======================

Run deployment to create the ceph rgws and the config Openstack config.

.. code-block:: console

   osism apply ceph-rgws

   osism apply ceph-rgw

