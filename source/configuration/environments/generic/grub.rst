====
Grub
====

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``debops.grub``
   * - **Repository**
     - https://github.com/debops/debops
   * - **Documentation**
     - https://docs.debops.org/en/master/ansible/roles/grub/defaults/main.html#grub-configuration-options

Blacklist a module
==================

.. code-block:: yaml

   ##########################
   # grub

   grub__default_configuration:
     - name: 'cmdline_linux_default'
         value:
           - modprobe.blacklist=qla2xxx

Disable predictable network interface names
===========================================

.. code-block:: yaml

   ##########################
   # grub

   grub__default_configuration:
     - name: 'cmdline_linux_default'
         value:
           - net.ifnames=0
           - biosdevname=0

.. _enable-iommu:

Enable IOMMU
============

Intel
-----

.. code-block:: yaml

   ##########################
   # grub

   grub__default_configuration:
     - name: 'cmdline_linux_default'
         value:
           - intel_iommu=on

AMD
---

.. code-block:: yaml

   ##########################
   # grub

   grub__default_configuration:
     - name: 'cmdline_linux_default'
         value:
           - iommu=pt
           - iommu=1

Support of Docker capabilities
==============================

.. note::

   Memory and swap accounting incur an overhead of about 1% of the total available memory
   and a 10% overall performance degradation, even if Docker is not running.

.. code-block:: console

   $ docker info
   [...]
   WARNING: No swap limit support

This is actual the default in ``debops grub`` https://github.com/debops/debops/blob/master/ansible/roles/grub/defaults/main.yml#L138

.. code-block:: yaml

   ##########################
   # grub

   grub__default_configuration:
     - name: 'cmdline_linux_default'
         value:
           - cgroup_enable=memory
           - swapaccount=1
