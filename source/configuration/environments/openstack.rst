.. _configuration-environment-openstack:

=========
OpenStack
=========

Base directory: ``environments/kolla``

The documentation for ``kolla-ansible`` can be found at
https://docs.openstack.org/kolla-ansible/latest/.

.. toctree::
   :maxdepth: 2

   openstack/cinder
   openstack/freezer
   openstack/gnocchi
   openstack/heat
   openstack/horizon
   openstack/keystone
   openstack/mistral
   openstack/neutron
   openstack/nova
   openstack/skydive

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

Enable service
==============

* make sure the necessary inventory groups are available in ``inventory/hosts``
* make sure the desired service is supported
* enable the service in ``environments/kolla/configuration.yml``
  (e.g. ``enable_freezer: "yes"`` to activate the service Freezer)

.. _haproxy-self-signed-cert:

HAProxy
=======

Set the ``kolla_internal_fqdn`` in ``environments/kolla/configuration.yml``.

Existing certificates
---------------------

Set ``kolla_enable_tls_external: "yes"`` in
``environments/kolla/configuration.yml`` and add the content of the existing
signed certificate to the ``kolla_external_fqdn_cert`` parameter in the
``environments/kolla/secrets.yml`` file.

.. code-block:: yaml

   kolla_external_fqdn_cert: |
     -----BEGIN CERTIFICATE-----
     [...]
     -----END CERTIFICATE-----
     -----BEGIN RSA PRIVATE KEY-----
     [...]
     -----END RSA PRIVATE KEY-----

Key and certificates in PEM format are stored consecutively in the following
order:

* server certificate
* server private key (without any password)
* intermediate certificates

If the order is not followed, an error occurs when starting HAProxy:
``inconsistencies between private key and certificate loaded from PEM file '/etc/haproxy/haproxy.pem'``.

.. _generation-of-self-signed-certificate:

Generate self-signed certificates
---------------------------------

If no certificate has been created yet, use ``osism-kolla _ certificates``
command to generate a self signed certifacte on the manager node.

.. code-block:: console

   osism-kolla _ certificates
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

The self-signed certificate is located at
``/etc/kolla/certificates/haproxy.pem`` inside the ``manager_kolla-ansible_1``
container on the manager node.

.. code-block:: console

   docker exec -u root -ti manager_kolla-ansible_1 sh -c 'cat /etc/kolla/certificates/private/haproxy.*'

Add the content of the output from the command above to
``kolla_external_fqdn_cert`` parameter at ``environments/kolla/secrets.yml``
of the configuration repository.

Set ``kolla_enable_tls_external: "yes"`` at
``environments/kolla/configuration.yml`` of the configuration repository.

* https://www.meshcloud.io/en/2017/04/18/pem-file-layout-for-haproxy/

You should also add the self-signed certificate to the list of trusted
certifcates on every computer that uses the external API. The workflow is
different for different Linux distributions. Many programs, such as
``OpenStackClient`` or ``cURL``,  also offer an ``--insecure`` parameter as a
temporary solution.
