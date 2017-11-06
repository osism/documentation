=======
Cobbler
=======

* http://cobbler.github.io/manuals/2.8.0/

List systems
============

.. code-block:: shell

   $ cobbler system list
      20-10
      20-11
      20-12
      30-10
      30-11
      50-10
      50-11
      50-12

Show system details
===================

.. code-block:: shell

   $ cobbler system report --name 20-12
   Name                           : 20-12
   TFTP Boot Files                : {}
   Comment                        :
   Enable gPXE?                   : <<inherit>>
   Fetchable Files                : {}
   Gateway                        :
   Hostname                       :
   Image                          :
   IPv6 Autoconfiguration         : False
   IPv6 Default Device            :
   Kernel Options                 : {'netcfg/choose_interface': 'enp5s0f0'}
   [...]

Enable provisioning
===================

.. code-block:: shell

   $ cobbler system edit --name 20-12 --netboot-enabled=true
   $ cobbler sync

Power control
=============

* http://cobbler.github.io/manuals/2.8.0/4/5_-_Power_Management.html

.. code-block:: shell

   $ cobbler system poweroff --name 20-12
   $ cobbler system poweron --name 20-12
