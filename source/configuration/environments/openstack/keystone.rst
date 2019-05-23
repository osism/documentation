========
Keystone
========

LDAP integration
================

* ``environments/kolla/files/overlays/keystone/domains/keystone.domainname.conf``

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

