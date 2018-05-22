=======
Generic
=======

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
