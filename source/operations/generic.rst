=======
Generic
=======

Check if reboot required
========================

.. note:: Run this command on the manager node.

.. code-block:: console

   $ osism-generic check-reboot

   PLAY [Check if system reboot is required] **************************************

   TASK [Check if /var/run/reboot-required exist] *********************************
   ok: [10-11.betacloud.xyz]
   [...]

   TASK [Print message if /var/run/reboot-required exist] *************************
   ok: [10-11.betacloud.xyz] => {
       "msg": "Reboot of 10-11.betacloud.xyz required"
   }
   [...]

   PLAY RECAP *********************************************************************
   10-11.betacloud.xyz        : ok=2    changed=0    unreachable=0    failed=0
   [...]

Reboot a system
===============

.. note:: Run this command on the manager node.

.. code-block:: console

   $ osism-generic reboot --limit 20-12.betacloud.xyz

   PLAY [Reboot systems] **********************************************************

   TASK [Reboot system] ***********************************************************
   changed: [20-12.betacloud.xyz]

   PLAY RECAP *********************************************************************
   20-12.betacloud.xyz        : ok=1    changed=1    unreachable=0    failed=0

Upgrade packages
================

.. note:: Run this command on the manager node.

.. code-block:: console

   $ osism-generic upgrade-packages
   PLAY [Upgrade packages] ********************************************************

   TASK [Update package cache] ****************************************************
   ok: [10-11.betacloud.xyz]

   TASK [Upgrade packages] ********************************************************
   ok: [10-11.betacloud.xyz]

   TASK [Remove useless packages from the cache] **********************************
   ok: [10-11.betacloud.xyz]

   TASK [Remove dependencies that are no longer required] *************************
   ok: [10-11.betacloud.xyz]
   [...]

   PLAY RECAP *********************************************************************
   10-11.betacloud.xyz        : ok=4    changed=0    unreachable=0    failed=0
   [...]
