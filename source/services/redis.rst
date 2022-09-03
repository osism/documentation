=====
Redis
=====

.. contents::
   :depth: 2

Bad file format reading the append only file
============================================

.. code-block:: console

   tail /var/log/kolla/redis/redis.log
   7:M 15 Jun 2022 09:20:39.239 * Reading RDB preamble from AOF file...
   7:M 15 Jun 2022 09:20:39.240 * Reading the remaining AOF tail...
   7:M 15 Jun 2022 09:20:40.215 # Bad file format reading the append only file: make a backup of your AOF file, then use ./redis-check-aof --fix <filename>

.. code-block:: console

   docker run -it \
              -v /var/lib/docker/volumes/redis/_data:/var/lib/redis \
              <repository>/osism/redis:<release> bash
   redis-check-aof --fix /var/lib/redis/redis-staging-ao.aof
   The AOF appears to start with an RDB preamble.
   Checking the RDB preamble to start:
   [offset 0] Checking RDB file --fix
   [offset 26] AUX FIELD redis-ver = '5.0.7'
   [offset 40] AUX FIELD redis-bits = '64'
   [offset 52] AUX FIELD ctime = '1655208150'
   [offset 67] AUX FIELD used-mem = '7538360'
   [offset 83] AUX FIELD aof-preamble = '1'
   [offset 85] Selecting DB ID 0
   [offset 13574] Checksum OK
   [offset 13574] \o/ RDB looks OK! \o/
   [info] 108 keys read
   [info] 105 expires
   [info] 105 already expired
   RDB preamble is OK, proceeding with AOF tail...
   0x         267b799: Expected prefix '*', got: '
   AOF analyzed: size=40352407, ok_up_to=40351641, diff=766
   This will shrink the AOF from 40352407 bytes, with 766 bytes, to 40351641 bytes
   Continue? [y/N]: y
   Successfully truncated AOF
   exit
