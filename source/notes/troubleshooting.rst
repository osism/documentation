===============
Troubleshooting
===============

sudo: unknown uid 42401: who are you?
=====================================

* https://bugs.launchpad.net/kolla-ansible/+bug/1680139

Solution: Stop the ``nscd`` service.

refusing to convert from file to symlink for /etc/resolv.conf
=============================================================

.. code-block:: console

   $ sudo rm /etc/resolv.conf
   $ sudo ln -s /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
