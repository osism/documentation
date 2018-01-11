============================
Generate Kolla secrets file
============================

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
