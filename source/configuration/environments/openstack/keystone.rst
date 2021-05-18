========
Keystone
========

LDAP integration
================

* https://docs.openstack.org/keystone/latest/admin/configuration.html#integrate-identity-with-ldap

The configuration of a domain is stored in an overlay configuration file of Kolla. The name of
the domain is stored in the file named ``environments/kolla/files/overlays/keystone/domains/keystone.DOMAIN.conf``.

.. code-block:: ini

   [identity]
   driver = ldap

   [resource]
   driver = sql

   [assignment]
   driver = sql

   [role]
   driver = sql

   [ldap]
   url = ldaps://ldap.intern.betacloud.io
   user = uid=keystone,ou=services,dc=betacloud,dc=io
   password = supersecret
   suffix = dc=betacloud,dc=io
   query_scope = sub
   page_size = 0
   chase_referrals = False

   user_attribute_ignore = password,tenant_id,tenants
   user_enabled_attribute = userAccountControl
   user_enabled_default = 512
   user_enabled_invert = false
   user_enabled_mask = 2
   user_filter =
   user_id_attribute = uid
   user_mail_attribute = mail
   user_name_attribute = uid
   user_objectclass = inetOrgPerson
   user_tree_dn = ou=users,dc=betacloud,dc=io

To use the domain, the domain must be created after Keystone has been deployed or reconfigured.

.. code-block:: console

   $ openstack --os-cloud service domain create --or-show DOMAIN
   +-------------+------------+
   | Field       | Value      |
   +-------------+------------+
   | description |            |
   | enabled     | True       |
   | id          | 1ef08b0... |
   | name        | DOMAIN     |
   | tags        | []         |
   +-------------+------------+
