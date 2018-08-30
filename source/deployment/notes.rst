=====
Notes
=====

Update rsyslog configuration
============================

.. code-block:: console

   $ osism-generic common --skip-tags always --tags logging

sudo: unknown uid 42401: who are you?
=====================================

* https://bugs.launchpad.net/kolla-ansible/+bug/1680139

Solution: Stop the ``nscd`` service.

Deleting all partitions
=======================

.. code-block:: console

   $ sudo dd if=/dev/zero of=/dev/sdc bs=512 count=1 conv=notrunc
