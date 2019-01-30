=======
Generic
=======

Docker
======

.. code-block:: console

   $ systemctl is-active docker
   active

   $ docker -v
   Docker version 17.12.0-ce, build c97c6d6

   $ docker info
   Containers: 0
    Running: 0
    Paused: 0
    Stopped: 0
   Images: 0
   Server Version: 17.12.0-ce
   Storage Driver: overlay2
    Backing Filesystem: extfs
    Supports d_type: true
    Native Overlay Diff: true
   Logging Driver: json-file
   Cgroup Driver: cgroupfs
   Plugins:
    Volume: local
    Network: bridge host macvlan null overlay
    Log: awslogs fluentd gcplogs gelf journald json-file logentries splunk syslog
   Swarm: inactive
   Runtimes: runc
   Default Runtime: runc
   Init Binary: docker-init
   containerd version: 89623f28b87a6004d4b785663257362d1658a729
   runc version: b2567b37d7b75eb4cf325b77297b140ea686ce8f
   init version: 949e6fa
   Security Options:
    apparmor
    seccomp
     Profile: default
   Kernel Version: 4.4.0-119-generic
   Operating System: Ubuntu 16.04.4 LTS
   OSType: linux
   Architecture: x86_64
   CPUs: 16
   Total Memory: 62.8GiB
   Name: host-1
   ID: SCDI:46XK:OMTT:3CYK:AKRM:5TUQ:VENX:NWX5:T4LW:KYSX:RHPY:R2NJ
   Docker Root Dir: /var/lib/docker
   Debug Mode (client): false
   Debug Mode (server): false
   Registry: https://index.docker.io/v1/
   Labels:
   Experimental: false
   Insecure Registries:
    registry-1.osism.io
    127.0.0.0/8
   Live Restore Enabled: false

   WARNING: No swap limit support

   $ docker pull ubuntu:16.04
   16.04: Pulling from library/ubuntu
   22dc81ace0ea: Pull complete
   1a8b3c87dba3: Pull complete
   91390a1c435a: Pull complete
   07844b14977e: Pull complete
   b78396653dae: Pull complete
   Digest: sha256:e348fbbea0e0a0e73ab0370de151e7800684445c509d46195aef73e090a49bd6
   Status: Downloaded newer image for ubuntu:16.04

   $ docker run --rm ubuntu:16.04 uptime
    09:38:55 up 1 day,  2:40,  0 users,  load average: 0.20, 0.11, 0.15


Chrony / NTP
============

.. note::

   The availability of an NTP server can be tested with ``ntpdate``.

   .. code-block:: console

      $ ntpdate -q 1.de.pool.ntp.org
      server 188.68.36.203, stratum 2, offset -0.000631, delay 0.04407
      server 159.69.150.81, stratum 2, offset -0.001407, delay 0.04521
      server 217.144.138.234, stratum 2, offset -0.002570, delay 0.04294
      server 185.242.112.3, stratum 2, offset 0.000577, delay 0.04129
      30 Jan 10:54:07 ntpdate[27123]: adjust time server 185.242.112.3 offset 0.000577 sec

Working
-------

.. code-block:: console

   $ systemctl is-active chrony
   active

   $ systemctl status chrony
   ● chrony.service - LSB: Controls chronyd NTP time daemon
      Loaded: loaded (/etc/init.d/chrony; bad; vendor preset: enabled)
      Active: active (running) since Fri 2017-11-17 14:48:08 UTC; 1 months 28 days ago
        Docs: man:systemd-sysv-generator(8)
       Tasks: 1
      Memory: 1.9M
         CPU: 6.874s
      CGroup: /system.slice/chrony.service
              └─3039 /usr/sbin/chronyd

.. code-block:: console

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

.. code-block:: console

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

The three following containers should run on each node. The ``docker ps`` command can be used for displaying containers.

* ``cron`` with ``registry-1.osism.io/osism/cron:ocata-20171120-0``
* ``fluentd`` with ``registry-1.osism.io/osism/fluentd:ocata-20171120-0``
* ``kolla-toolbox`` with ``registry-1.osism.io/osism/kolla-toolbox:ocata-20171120-0``

.. note::

   Docker registry (``registry-1.osism.io``) as well as the tag (``ocata-20171120-0``) of the image differs from environment to environment.

Helpers
=======

* phpMyAdmin

.. code-block:: console

   $ curl 10.49.20.10:8110

* Rally

.. code-block:: console

   $ curl 10.49.20.10:8090

* Cephclient

.. code-block:: console

   $ ceph -s

* OpenStackClient

.. code-block:: console

   $ openstack --os-cloud admin service list
