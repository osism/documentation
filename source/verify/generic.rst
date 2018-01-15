=======
Generic
=======

Chrony / NTP
============

Working
-------

.. code-block:: shell

   $ chronyc tracking
   Reference ID    : 131.188.3.221 (ntp1.rrze.uni-erlangen.de)
   Stratum         : 3
   Ref time (UTC)  : Mon Jan 15 17:49:55 2018
   System time     : 0.000012268 seconds fast of NTP time
   Last offset     : +0.000010541 seconds
   RMS offset      : 0.000071033 seconds
   Frequency       : 15.916 ppm slow
   Residual freq   : +0.000 ppm
   Skew            : 0.015 ppm
   Root delay      : 0.008568 seconds
   Root dispersion : 0.021940 seconds
   Update interval : 1034.9 seconds
   Leap status     : Normal

   $ chronyc sources
   210 Number of sources = 3
   MS Name/IP address         Stratum Poll Reach LastRx Last sample
   ===============================================================================
   ^- ntp1.wtnet.de                 2  10   377   328    +34us[  +34us] +/-   24ms
   ^* ntp1.rrze.uni-erlangen.de     1  10   377   409    -13us[  -27us] +/- 7480us
   ^- ns2.customer-resolver.net     2  10   377   924  +1399us[+1386us] +/-   47ms

Not working
-----------

.. code-block:: shell

   $ chronyc tracking
   Reference ID    : 127.127.1.1 ()
   Stratum         : 10
   Ref time (UTC)  : Mon Jan 15 18:09:08 2018
   System time     : 0.000000002 seconds slow of NTP time
   Last offset     : +0.000000000 seconds
   RMS offset      : 0.000000000 seconds
   Frequency       : 18.395 ppm slow
   Residual freq   : +0.000 ppm
   Skew            : 0.000 ppm
   Root delay      : 0.000000 seconds
   Root dispersion : 0.000001 seconds
   Update interval : 0.0 seconds
   Leap status     : Not synchronised

   $ chronyc sources
   210 Number of sources = 2
   MS Name/IP address         Stratum Poll Reach LastRx Last sample
   ===============================================================================
   ^? xx.xx.xx.xx                   0  10     0   10y     +0ns[   +0ns] +/-    0ns
   ^? xx.xx.xx.xx                   0  10     0   10y     +0ns[   +0ns] +/-    0ns

Common containers
=================

The three following containers should run on each node.

* ``cron`` with ``registry-1.osism.io/osism/cron:ocata-20171120-0``
* ``fluentd`` with ``registry-1.osism.io/osism/fluentd:ocata-20171120-0``
* ``kolla-toolbox`` with ``registry-1.osism.io/osism/kolla-toolbox:ocata-20171120-0``

.. note::

   Docker registry (``registry-1.osism.io``) as well as the tag (``ocata-20171120-0``) of the image differs from environment to environment.
