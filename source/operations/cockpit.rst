=======
Cockpit
=======

Untrusted host
==============

.. image:: /images/cockpit-untrusted-host.png

To solve the problem, log in manually to the addresses stored in the ``/etc/cockpit/machines.d/`` files.

.. code-block:: console

   $ ssh 192.168.50.10
   The authenticity of host '192.168.50.10 (192.168.50.10)' can't be established.
   ECDSA key fingerprint is SHA256:85eXWkwB3SCEEXVEJ9VeuE+zTBP6AVq3t3ehd5pckWY.
   Are you sure you want to continue connecting (yes/no)? yes
   Warning: Permanently added '192.168.50.10' (ECDSA) to the list of known hosts.
   [...]
