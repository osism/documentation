======
Ironic
======

Secure erased failed, SATA devices are locked
=============================================

If the ``enable_ata_secure_erase`` parameter in the ``[deploy]`` section
is set to ``True`` (the default value) during cleaning, the SATA disks
may be locked after an interruption of the process and have to be unlocked
manually with an empty string as password during reboot.

To solve this you have to boot with a rescue system (e.g. TinyIPA) and
then execute the following comand: ``hdparm --security-disable '' /dev/sdX``.
