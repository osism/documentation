=====
Kolla
=====

Base directory: ``environments/kolla``

The documentation for ``kolla-ansible`` can be found on https://docs.openstack.org/kolla-ansible/latest/.

.. toctree::
   :maxdepth: 2

   kolla/cinder
   kolla/freezer
   kolla/gnocchi
   kolla/heat
   kolla/horizon
   kolla/keystone
   kolla/mistral
   kolla/neutron
   kolla/nova
   kolla/skydive

Generate secrets
================

This step is not necessary when using the cookiecutter template.

* ``environments/kolla/secets.yml``

.. code-block:: console

   $ wget https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/scripts/generate-secrets.py
   $ wget https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/kolla/secrets.yml.pike
   $ python generate-secrets.py -p secrets.yml.pike
   $ mv secrets.yml.pike secrets.yml
   $ rm generate-secrets.py

Depending on the environment, additional parameters must be added manually in this file.
These parameters are not yet included in the upstream of ``kolla-ansible``.

Currently the following additional parameters are available:

* ``prometheus_database_password``
* ``kolla_external_fqdn_cert``

The ``secrets.yml`` file should be encrypted with Ansibe Vault.

* https://docs.ansible.com/ansible/2.5/user_guide/vault.html

Inventory
=========

Add host-specific Kolla variables for network interfaces to the inventory.

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # kolla

   network_interface: eth0
   storage_interface: eth1
   tunnel_interface: eth2
   api_interface: eth3

   neutron_external_interface: eth4
   kolla_external_vip_interface: eth5

Use a specific image version
============================

* ``environments/kolla/images.yml``

.. code-block:: yaml

   ---
   [...]
   ##########################
   # project: magnum

   magnum_api_image: "{{ docker_registry }}/osism/magnum-api"
   magnum_api_tag: "pike-latest"

   magnum_conductor_image: "{{ docker_registry }}/osism/magnum-conductor"
   magnum_conductor_tag: "pike-latest"

* possible images for ``ocata``: https://github.com/osism/docker-kolla-ansible/blob/master/files/images-ocata.yml
* possible images for ``pike``: https://github.com/osism/docker-kolla-ansible/blob/master/files/images-pike.yml
* possible images for ``queens``: https://github.com/osism/docker-kolla-ansible/blob/master/files/images-queens.yml

Enable service
==============

* make sure the necessary inventory groups are available in ``inventory/hosts``
* make sure the desired service is supported
* enable the service in ``environments/kolla/configuration.yml`` (e.g. ``enable_freezer: "yes"`` to activate the service Freezer)

HAProxy
=======

Set the ``kolla_internal_fqdn`` in ``environments/kolla/configuration.yml``.

Existing certificates
---------------------

Set ``kolla_enable_tls_external: "yes"`` in ``environments/kolla/configuration.yml`` and add the
content of the existing signed certificate to the ``kolla_external_fqdn_cert`` parameter in the
``environments/kolla/secrets.yml`` file.

The order is important. If this is not followed, an error occurs when starting HAProxy:
``inconsistencies between private key and certificate loaded from PEM file '/etc/haproxy/haproxy.pem'``.

* server certificate
* server private key (without any password)
* intermediate certificates

Generate self-signed certificates
---------------------------------

Run this command on the manager node.

.. code-block:: console

   $ osism-kolla _ certificates
   PLAY [Apply role certificates] *************************************************

   TASK [certificates : Ensuring config directories exist] ************************
   ok: [localhost] => (item=certificates/private)

   TASK [certificates : Creating SSL configuration file] **************************
   ok: [localhost] => (item=openssl-kolla.cnf)

   TASK [certificates : Creating Key] *********************************************
   ok: [localhost] => (item=/etc/kolla//certificates/private/haproxy.key)

   TASK [certificates : Creating Server Certificate] ******************************
   ok: [localhost] => (item=/etc/kolla//certificates/private/haproxy.crt)

   TASK [certificates : Creating CA Certificate File] *****************************
   ok: [localhost]

   TASK [certificates : Creating Server PEM File] *********************************
   ok: [localhost]

   PLAY RECAP *********************************************************************
   localhost        : ok=6    changed=0    unreachable=0    failed=0

On the manager node the self-signed certificate is located in ``/etc/kolla/certificates/haproxy.pem``
inside the ``manager_kolla-ansible_1`` container.

.. code-block:: console

   $ docker exec -it manager_kolla-ansible_1 bash

If the ``pem`` file is not created correctly that is not a problem. Then just use the output of
``cat /etc/kolla/certificates/private/haproxy.*``.

Set ``kolla_enable_tls_external: "yes"`` in ``environments/kolla/configuration.yml`` and add the
content of the self-signed certificate to the ``kolla_external_fqdn_cert`` parameter in the
``environments/kolla/secrets.yml`` file.

.. code-block:: yaml

   kolla_external_fqdn_cert
     -----BEGIN CERTIFICATE-----
     [...]
     -----END CERTIFICATE-----
     -----BEGIN RSA PRIVATE KEY-----
     -----END RSA PRIVATE KEY-----

You should also add the self-signed certificate to the list of trusted certifcates on every computer
that uses the external API. The workflow is different for different Linux distributions.
Many programs, such as ``OpenStackClient`` or ``cURL``,  also offer an ``--insecure`` parameter as
a temporary solution.
