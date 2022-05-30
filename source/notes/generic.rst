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

ssh: Too many authentication failures
=====================================

Description
-----------

.. code-block:: console

   $ ssh -i id_rsa.operator dragon@10.11.12.13
      Received disconnect from 10.11.12.13 port 22:2: Too many authentication failures
      Authentication failed.

Solution
--------

Sometimes this is caused by too many files in ``~/.ssh/``. You can use the ``IdentitiesOnly`` option as a workaround.

.. code-block:: console

   $ ssh -o IdentitiesOnly=yes -i id_rsa.operator dragon@10.11.12.13

docker-compose: error getting credentials
=========================================

* https://github.com/docker/docker-credential-helpers/issues/60

.. code-block:: none

   error getting credentials - err: exit status 1, out: Cannot autolaunch D-Bus without X11 $DISPLAY

The problem may occur when using the Docker Compose CLI plugin on older Ubuntu version (before Focal).
It can be fixed by reinstalling the package ``pass``.
