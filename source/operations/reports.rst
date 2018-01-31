=======
Reports
=======

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
