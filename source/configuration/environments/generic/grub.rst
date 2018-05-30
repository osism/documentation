====
Grub
====

* role: ``debops.grub`` (https://github.com/debops/ansible-grub)

* ``environments/configuration.yml``

  .. code-block:: yaml

     ##########################
     # grub

     grub_kernel_options:
       - modprobe.blacklist=qla2xxx
