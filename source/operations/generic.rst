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

Cronjobs
========

Cronjobs are managed in playbook ``playbook-cronjobs.yml`` in environment ``custom``.

* https://docs.ansible.com/ansible/latest/modules/cron_module.html

The playbook can be rolled out with ``osism-run custom cronjobs``.

Examples can be found in the `cookiecutter repository <https://github.com/osism/cfg-cookiecutter/blob/master/cfg-%7B%7Bcookiecutter.project_name%7D%7D/environments/custom/playbook-cronjobs.yml>`_.

sosreport
=========

Sos is an extensible, portable, support data collection tool primarily aimed at Linux distributions and
other UNIX-like operating systems.

* https://github.com/sosreport/sos

To collect reports from all systems, execute the following command on the manager node.

.. code-block:: shell

   $ osism-generic sosreport

The collected reports can be found on the manager node under ``/opt/archive/sosreport``. Per system and day
there is a tarball with the corresponding MD5 checksum.

.. note::

   Currently only one run per day is possible.

Currently the following plugins are activated.

- apt
- auditd
- block
- devices
- docker
- dpkg
- filesys
- general
- hardware
- kernel
- kvm
- last
- md
- memory
- networking
- pci
- process
- processor
- python
- services
- ssh
- system
- systemd
- ubuntu
- udev
- usb
- xfs
