=====
Kolla
=====

* base directory: ``environments/kolla``

.. note ::

   The documentation for ``kolla-ansible`` can be found on https://docs.openstack.org/kolla-ansible/latest/.

Generate secrets
================

* ``environments/kolla/secets.yml``

.. code-block:: console

   $ wget https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/scripts/generate-secrets.py
   $ wget https://raw.githubusercontent.com/osism/cfg-cookiecutter/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/kolla/secrets.yml.pike
   $ python generate-secrets.py -p secrets.yml.pike
   $ mv secrets.yml.pike secrets.yml
   $ rm generate-secrets.py

.. note::

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

HAProxy
=======

Set the ``kolla_internal_fqdn`` in ``environments/kolla/configuration.yml``.

Generate self-signed certificates
---------------------------------

.. note:: Run this command on the manager node.

.. note:: ``10-11.betacloud.xyz`` is the manager node.

.. code-block:: console

   $ osism-kolla _ certificates --limit 10-11.betacloud.xyz
   PLAY [Apply role certificates] *************************************************

   TASK [certificates : Ensuring config directories exist] ************************
   ok: [10-11.betacloud.xyz] => (item=certificates/private)

   TASK [certificates : Creating SSL configuration file] **************************
   ok: [10-11.betacloud.xyz] => (item=openssl-kolla.cnf)

   TASK [certificates : Creating Key] *********************************************
   ok: [10-11.betacloud.xyz] => (item=/etc/kolla//certificates/private/haproxy.key)

   TASK [certificates : Creating Server Certificate] ******************************
   ok: [10-11.betacloud.xyz] => (item=/etc/kolla//certificates/private/haproxy.crt)

   TASK [certificates : Creating CA Certificate File] *****************************
   ok: [10-11.betacloud.xyz]

   TASK [certificates : Creating Server PEM File] *********************************
   ok: [10-11.betacloud.xyz]

   PLAY RECAP *********************************************************************
   10-11.betacloud.xyz        : ok=6    changed=0    unreachable=0    failed=0

On the manager node the self-signed certificate is located in ``/etc/kolla/certificates/haproxy.pem``.

If the ``pem`` file is not created correctly that is not a problem. Then just use the output of
``cat /etc/kolla/certificates/private/haproxy.*``.

Set ``kolla_enable_tls_external: "yes"`` in ``environments/kolla/configuration.yml`` and add the
content of the self-signed certificate to the ``kolla_external_fqdn_cert`` parameter in the
``environments/kolla/secrets.yml`` file.

You should also add the self-signed certificate to the list of trusted certifcates on every computer
that uses the external API. The workflow is different for different Linux distributions.
Many programs, such as ``OpenStackClient`` or ``cURL``,  also offer an ``--insecure`` parameter as
a temporary solution.

Cinder
======

iSCSI support
-------------

* ``environments/kolla/configuration.yml``

.. code-block:: yaml

   enable_cinder_backend_iscsi: yes
   enable_cinder_backend_lvm: no

* ``inventory/hosts``

.. code-block:: ini

   [iscsid:children]
   compute
   storage
   ironic-conductor

   [multipathd:children]
   compute
   storage

   [tgtd:children]
   storage

Neutron
=======

Multiple provider networks
--------------------------

* ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   network_interfaces:
   [...]
    - device: eth3
      auto: true
      family: inet
      method: manual
      mtu: 1500

    - device: eth4
      auto: true
      family: inet
      method: manual
      mtu: 1500

* ``environments/kolla/configuration.yml`` or ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   enable_neutron_provider_networks: "yes"

* ``environments/kolla/configuration.yml`` or ``inventory/host_vars/<hostname>.yml``

.. code-block:: yaml

   neutron_bridge_name: br-eth3,br-eth4
   neutron_external_interface: eth3,eth4
