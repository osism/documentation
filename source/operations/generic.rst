=======
Generic
=======

Run commands
============

.. code-block:: console

   $ osism-ansible generic all -m shell -a date
   testbed-node-0.osism.local | SUCCESS | rc=0 >>
   Sun Dec  2 10:28:42 UTC 2018

   testbed-node-1.osism.local | SUCCESS | rc=0 >>
   Sun Dec  2 10:28:42 UTC 2018
   [...]

Force NTP sync
==============

.. code-block:: console

   $ sudo chronyc -a 'burst 4/4'
   200 OK
   200 OK
   $ sudo chronyc -a makestep
   200 OK
   200 OK

you can use osism custom, ``environments/custom/playbook-force-timesync.yml``

.. code-block:: console

   ---
   - name: Force NTP time sync with chronyc
     hosts: all
     gather_facts: no

     vars:
       chronyc_options:
         - burst 4/4
         - makestep

     tasks:
       - name: Execute chronyc
         command: "/usr/bin/chronyc -a '{{ item }}'"
         with_items: "{{ chronyc_options }}"
         run_once: true
         become: yes

       - name: Sync hardware clock
         command: "/sbin/hwclock --systohc --utc"
         run_once: true
         become: yes

and execute with command

.. code-block:: console

   osism-run custom force-timesync -l <inventoryname>

Check if reboot required
========================

.. note:: Run this command on the manager node.

.. code-block:: console

   $ osism-generic check-reboot

   PLAY [Check if system reboot is required] **************************************

   TASK [Check if /var/run/reboot-required exist] *********************************
   ok: [testbed-manager.osism.local]
   [...]

   TASK [Print message if /var/run/reboot-required exist] *************************
   ok: [testbed-manager.osism.local] => {
       "msg": "Reboot of testbed-manager.osism.local required"
   }
   [...]

   PLAY RECAP *********************************************************************
   testbed-manager.osism.local        : ok=2    changed=0    unreachable=0    failed=0
   [...]

Reboot a system
===============

.. note:: Run this command on the manager node.

.. code-block:: console

   $ osism-generic reboot --limit testbed-node-0.osism.local

   PLAY [Reboot systems] **********************************************************

   TASK [Reboot system] ***********************************************************
   changed: [testbed-node-0.osism.local]

   PLAY RECAP *********************************************************************
   testbed-node-0.osism.local        : ok=1    changed=1    unreachable=0    failed=0

Upgrade packages
================

.. note:: Run this command on the manager node.

.. code-block:: console

   $ osism-generic upgrade-packages
   PLAY [Upgrade packages] ********************************************************

   TASK [Update package cache] ****************************************************
   ok: [testbed-node-0.osism.local]

   TASK [Upgrade packages] ********************************************************
   ok: [1testbed-node-0.osism.local]

   TASK [Remove useless packages from the cache] **********************************
   ok: [testbed-node-0.osism.local]

   TASK [Remove dependencies that are no longer required] *************************
   ok: [testbed-node-0.osism.local]
   [...]

   PLAY RECAP *********************************************************************
   testbed-node-0.osism.local        : ok=4    changed=0    unreachable=0    failed=0
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

Update rsyslog configuration
============================

.. code-block:: console

   $ osism-generic common --skip-tags always --tags logging
