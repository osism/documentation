=====
Notes
=====

Reboot a system
===============

.. note:: Run this command on the manager node.

.. code-block:: shell

   $ osism-generic reboot --limit 20-12.betacloud.xyz

   PLAY [Reboot systems] **********************************************************

   TASK [Reboot system] ***********************************************************
   changed: [20-12.betacloud.xyz]

   PLAY RECAP *********************************************************************
   20-12.betacloud.xyz        : ok=1    changed=1    unreachable=0    failed=0

Update facts
============

.. note:: Run this command on the manager node.

.. code-block:: shell

   $ osism-generic facts

   PLAY [Gather facts for all hosts] **********************************************

   TASK [setup] *******************************************************************
   ok: [20-11.betacloud.xyz]
   ok: [20-10.betacloud.xyz]
   ok: [50-10.betacloud.xyz]
   ok: [50-11.betacloud.xyz]
   ok: [50-12.betacloud.xyz]
   ok: [10-11.betacloud.xyz]
   ok: [30-10.betacloud.xyz]
   ok: [20-12.betacloud.xyz]
   ok: [30-11.betacloud.xyz]

   PLAY [Gather facts for all hosts (if using --limit)] ***************************

   TASK [setup] *******************************************************************
   skipping: [30-11.betacloud.xyz] => (item=20-11.betacloud.xyz)
   skipping: [30-11.betacloud.xyz] => (item=20-10.betacloud.xyz)
   [...]

   PLAY RECAP *********************************************************************
   10-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   20-10.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   20-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   20-12.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   30-10.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   30-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   50-10.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   50-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   50-12.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0

Update configuration
====================

There are two possibilities to update the configuration repository on the manager node.

On the seed node change into the manager environment and use the following command. This will update the configuration repository on the manager node.

.. code-block:: shell

   $ ./run.sh configuration

On the manager node use the following command to update the configuration repository.

.. code-block:: shell

   $ osism-generic configuration

Generate self-signed certificates
=================================

.. note:: Run this command on the manager node.

.. note:: ``10-11.betacloud.xyz`` is the manager node.

.. code-block:: shell

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
