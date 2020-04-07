============
Open vSwitch
============

* http://docs.openvswitch.org/en/latest/faq/issues/

vxlan: non-ECT from ADDRESS with TOS=0x2
========================================

.. code-block:: console

   $ dmesg | tail -n 10
   [22645061.223507] vxlan: non-ECT from 10.48.30.11 with TOS=0x2
   [22645061.374522] vxlan: non-ECT from 10.48.30.11 with TOS=0x2
   [22645061.374590] vxlan: non-ECT from 10.48.30.11 with TOS=0x2
   [22645061.374599] vxlan: non-ECT from 10.48.30.11 with TOS=0x2
   [22645061.376204] vxlan: non-ECT from 10.48.30.10 with TOS=0x2
   [22645061.377116] vxlan: non-ECT from 10.48.30.10 with TOS=0x2
   [22645061.411986] vxlan: non-ECT from 10.48.30.11 with TOS=0x2
   [22645061.531827] vxlan: non-ECT from 10.48.30.11 with TOS=0x2
   [22645062.894827] vxlan: non-ECT from 10.48.30.10 with TOS=0x2
   [22645063.367127] vxlan: non-ECT from 10.48.30.11 with TOS=0x2

.. code-block:: console

   $ echo N | sudo tee /sys/module/vxlan/parameters/log_ecn_error

.. code-block:: console

   $ echo "options vxlan log_ecn_error=N" | sudo tee /etc/modprobe.d/osism-vxlan.conf

wakeup due to [POLLIN] on fd 38 (unknown anon_inode:[eventpoll]) at ../lib/dpif-netlink.c:2786 (99% CPU usage)
==============================================================================================================

* https://mail.openvswitch.org/pipermail/ovs-discuss/2019-May/048608.html
* https://bugs.launchpad.net/ubuntu/+source/openvswitch/+bug/1827264
* https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=949845

.. code-block:: none

   2020-04-07T05:22:46.785Z|04080|poll_loop(handler111)|INFO|Dropped 1336248 log messages in last 6 seconds (most recently, 0 seconds ago) due to excessive rate
   2020-04-07T05:22:46.785Z|04081|poll_loop(handler111)|INFO|wakeup due to [POLLIN] on fd 38 (unknown anon_inode:[eventpoll]) at ../lib/dpif-netlink.c:2786 (99% CPU usage)

.. code-block:: console

   $ docker exec -it openvswitch_vswitchd ovs-appctl version
   ovs-vswitchd (Open vSwitch) 2.10.0

.. code-block:: console

   $ docker exec -it openvswitch_vswitchd bash
   # ovs-vsctl set Open_vSwitch . other-config:n-handler-threads=1
   # ovs-vsctl set Open_vSwitch . other-config:n-revalidator-threads=1
