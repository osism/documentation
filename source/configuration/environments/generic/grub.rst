====
Grub
====

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``debops.grub``
   * - **Repository**
     - https://github.com/debops/ansible-grub
   * - **Documentation**
     - https://docs.debops.org/en/master/ansible/roles/debops.grub/index.html

Blacklist a module
==================

.. code-block:: yaml

   ##########################
   # grub

   grub_kernel_options:
     - modprobe.blacklist=qla2xxx

Disable predictable network interface names
===========================================

.. code-block:: yaml

   ##########################
   # grub

   grub_kernel_options:
     - net.ifnames=0
     - biosdevname=0

Enable IOMMU
============

Intel
-----

.. code-block:: yaml

   ##########################
   # grub

   grub_kernel_options:
     - intel_iommu=on

AMD
---

.. code-block:: yaml

   ##########################
   # grub

   grub_kernel_options:
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

.. code-block:: yaml

   ##########################
   # grub

   grub_kernel_options:
     - cgroup_enable=memory
     - swapaccount=1
