=====
Kolla
=====

* base directory: ``environments/kolla``

Generate secrets.yml file
=========================

.. code-block:: shell

   $ curl -o generate_passwords.py https://raw.githubusercontent.com/openstack/kolla-ansible/master/kolla_ansible/cmd/genpwd.py
   $ curl -o secrets.yml https://raw.githubusercontent.com/openstack/kolla-ansible/master/etc/kolla/passwords.yml
   $ python generate_passwords.py -p secrets.yml

.. note::

   Depending on the environment, additional parameters must be added manually in this file.
   These parameters are not yet included in the upstream of ``kolla-ansible``.

   Currently the following additional parameters are available:

   * ``prometheus_database_password``
   * ``kolla_external_fqdn_cert``

The ``secrets.yml`` file should be encrypted with Ansibe Vault.

* https://docs.ansible.com/ansible/2.4/vault.html

Generate self-signed certificates
=================================

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

Set ``kolla_enable_tls_external: "yes"`` in ``environments/kolla/configuration.yml`` and add the
content of the self-signed certificate to the ``kolla_external_fqdn_cert`` parameter in the
``environments/kolla/secrets.yml`` file.
