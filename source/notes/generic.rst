=======
Generic
=======

Tunnel internal networks via SSH with sshuttle
==============================================

* https://github.com/sshuttle/sshuttle

.. code-block:: bash

   $ sshuttle -r dragon@172.17.10.10 10.50.0.0/16 10.49.0.0/16

Does a system support IPMI
==========================

IPMI support available:

.. code-block:: console

   $ sudo dmidecode --type 38
   # dmidecode 3.0
   Getting SMBIOS data from sysfs.
   SMBIOS 3.0 present.

   Invalid entry length (16). Fixed up to 11.
   Handle 0x0058, DMI type 38, 18 bytes
   IPMI Device Information
       Interface Type: KCS (Keyboard Control Style)
       Specification Version: 2.0
       I2C Slave Address: 0x10
       NV Storage Device: Not Present
       Base Address: 0x0000000000000CA2 (I/O)
       Register Spacing: Successive Byte Boundaries

IPMI support not available:

.. code-block:: console

   $ sudo dmidecode --type 38
   # dmidecode 3.0
   Scanning /dev/mem for entry point.
   # No SMBIOS nor DMI entry point found, sorry.

Test of new hardware
====================

The tools listed below can be used to test hardware.

.. note ::

   The test of new hardware is generally not necessary, the failure rate of today's components is pretty low.

   A burn in is already done on the manufacturer side and usually is not necessary either.

* https://github.com/stressapptest/stressapptest

Storage device: badblocks
--------------------------

* https://linux.die.net/man/8/badblocks

CPU: stress-ng
--------------

* http://kernel.ubuntu.com/~cking/stress-ng/

Memory: MemTest86
-----------------

* https://www.memtest86.com
* https://www.memtest86.com/download.htm
* https://www.memtest86.com/technical.htm

Spectre & Meltdown
==================

* https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/SpectreAndMeltdown
* https://github.com/speed47/spectre-meltdown-checker

.. note::

   ``Inspect the script. You never blindly run scripts you downloaded from the Internet, do you?``

.. note::

   Run the current kernel and install ``amd-microcode`` or ``intel-microcode`` package.

.. code-block:: console

   $ curl -L https://meltdown.ovh -o spectre-meltdown-checker.sh
   $ chmod +x spectre-meltdown-checker.sh
   $ sudo ./spectre-meltdown-checker.sh
   Spectre and Meltdown mitigation detection tool v0.37+

   Checking for vulnerabilities on current system
   Kernel is Linux 4.4.0-127-generic #153-Ubuntu SMP Sat May 19 10:58:46 UTC 2018 x86_64
   CPU is AMD EPYC 7251 8-Core Processor
   [...]

Deleting all partitions
=======================

.. code-block:: console

   $ sudo dd if=/dev/zero of=/dev/sdc bs=512 count=1 conv=notrunc
