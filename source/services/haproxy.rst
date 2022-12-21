=======
HAProxy
=======

Manual failover
===============

* Although HAProxy runs on multiple nodes, the virtual IP addresses can only be assigned to one node.
  That means that only one HAProxy instance is used at the same time.

* Keepalived manages the virtual IP addresses and initiates an automatic failover if one node fails.
  There is no official way to manually tell keepalived to failover the VIP. But if you restart the
  keepalived container on the active node, the VIP will be moved to another node.

.. code-block:: console

   $ docker restart keepalived

* Another possibility is the use of a additional dummy interface. However, it is necessary to maintain
  keepalived configuration as an overlay file.

  https://www.virtualtothecore.com/en/manual-failover-of-keepalived/

Change certificate
==================

After Tran:
-----------

* Replace the file ``environments/kolla/certificates/haproxy.pem``. You can encrypt the ``haproxy.pem`` with ansible vault password.

.. code-block:: yaml

   environments/kolla/certifcates/haproxy.pem
     -----BEGIN CERTIFICATE-----
     [...]
     -----END CERTIFICATE-----
     -----BEGIN RSA PRIVATE KEY-----
     [...]
     -----END RSA PRIVATE KEY-----

* Key and certificates in PEM format are stored consecutively in the following order:

  - server public key
  - server private key (without any password)
  - intermediate CA certificates

Bevor Train:
-----------

* Update the certificate in the file ``environments/kolla/secrets.yml`` (``kolla_external_fqdn_cert``)
  The order of certificates is important:

  - server private key
  - server public key
  - intermediate CA certificates (if any)
  - CA root certificate

* Reconfigure HAProxy with ``osism-kolla reconfigure loadbalancer``

Validate configuration
----------------------

.. code-block:: console

   $ osism-kolla config loadbalancer

.. code-block:: console

   $ docker exec -it haproxy haproxy -c -V -f /etc/haproxy/haproxy.cfg
   Configuration file is valid

Restart HAProxy to load new certificate
---------------------------------------

.. code-block:: console

   osism-ansible generic all -m shell -a 'docker restart haproxy' -l control
