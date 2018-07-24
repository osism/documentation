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

* ``environments/configuration.yml``

Blacklist a module:

  .. code-block:: yaml

     ##########################
     # grub

     grub_kernel_options:
       - modprobe.blacklist=qla2xxx

Disable predictable network interface names:

  .. code-block:: yaml

     ##########################
     # grub

     grub_kernel_options:
       - net.ifnames=0
       - biosdevname=0
