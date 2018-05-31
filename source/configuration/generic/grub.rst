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

  .. code-block:: yaml

     ##########################
     # grub

     grub_kernel_options:
       - modprobe.blacklist=qla2xxx
