========
Hardware
========

.. contents::
   :local:

The test of new hardware is generally not necessary, the failure rate of today's components is pretty low.

A burn in is already done on the manufacturer side and usually is not necessary either.

Storage devices
===============

* https://linux.die.net/man/8/badblocks

stressapptest
-------------

* https://github.com/stressapptest/stressapptest

.. code-block:: console

   # apt-get install stressapptest

.. code-block:: console

   # stressapptest -s 30
   Log: Commandline - stressapptest -s 30
   Stats: SAT revision 1.0.6_autoconf, 64 bit binary
   Log: buildd @ lgw01-amd64-022 on Thu Apr  5 10:28:35 UTC 2018 from open source release
   Log: 1 nodes, 48 cpus.
   Log: Defaulting to 48 copy threads
   Log: Total 257895 MB. Free 254409 MB. Hugepages 0 MB. Targeting 244809 MB (94%)
   Log: Prefer plain malloc memory allocation.
   Log: Using memaligned allocation at 0x7f389f6ff000.
   Stats: Starting SAT, 244809M, 30 seconds
   Log: Region mask: 0x1
   Log: Seconds remaining: 20
   Log: Seconds remaining: 10
   Stats: Found 0 hardware incidents
   Stats: Completed: 1135370.00M in 30.03s 37813.12MB/s, with 0 hardware incidents, 0 errors
   Stats: Memory Copy: 1135370.00M at 37825.20MB/s
   Stats: File Copy: 0.00M at 0.00MB/s
   Stats: Net Copy: 0.00M at 0.00MB/s
   Stats: Data Check: 0.00M at 0.00MB/s
   Stats: Invert Data: 0.00M at 0.00MB/s
   Stats: Disk: 0.00M at 0.00MB/s

   Status: PASS - please verify no corrected errors

fio
---

* https://fio.readthedocs.io/en/latest/fio_doc.html
* https://github.com/axboe/fio/tree/master/examples

.. code-block:: console

   # apt-get install fio

CPU
===

stress-ng
---------

* http://kernel.ubuntu.com/~cking/stress-ng/
* https://wiki.ubuntu.com/Kernel/Reference/stress-ng

.. code-block:: console

   # apt-get install stress-ng

Memory
======

.. note::

   Using memtest86+ (available as a package in Ubuntu) is not possible when using UEFI.

* https://www.memtest86.com
* https://www.memtest86.com/download.htm
* https://www.memtest86.com/technical.htm
