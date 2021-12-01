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

OVS ports
=========

* Port with OVS tag ``32``

.. code-block:: console

   docker exec -it openvswitch_vswitchd ovs-vsctl show
   ...
           Port "tap44874148-5b"
               tag: 32
               Interface "tap44874148-5b"
                   type: internal
   ...

Ports with tag 4095 - mark "dead"
=================================

* https://www.suse.com/support/kb/doc/?id=000018712
* Port with OVS tag ``4095``

.. code-block:: console

   docker exec -it openvswitch_vswitchd ovs-vsctl show
   ...
             Port "tapc0f9a508-89"
               tag: 4095
               Interface "tapc0f9a508-89"
                   type: internal
   ...

* Port in ``OpenStack``

.. code-block:: console

   # openstack --os-cloud admin port list | grep c0f9a508-89
   | ID             | Name | MAC Address | Fixed IP Addresses                                |
   | c0f9a508-89... |      | fa:16:...   | {"subnet_id": "subnetUUID", "ip_address": "IP"}   |

* Sometimes there is no port in ``OpenStack``

.. code-block:: console

   # openstack --os-cloud admin port list | grep c0f9a508-89
   | ID             | Name | MAC Address | Fixed IP Addresses                                |

* OpenStack ``port show``

.. code-block:: console

   # openstack --os-cloud admin port show c0f9a508-89...
   +-----------------------+-----------------+
   | Field                 | Value           |
   +-----------------------+-----------------+
   ...
   | binding:vif_type      | binding_failed  |
   ...
   +-----------------------+-----------------+

* Port on host ``DOWN``

.. code-block:: console

   # ip address show tapc0f9a508-89
   356: tapc0f9a508-89: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
       link/ether 2a:fb:4b:a3:45:f2 brd ff:ff:ff:ff:ff:ff

* Delete port in ``OpenStack`` if present

.. code-block:: console

   # openstack --os-cloud admin port delete c0f9a508-89...

* Delete port in ``OVS``

.. code-block:: console

   # docker exec -it openvswitch_vswitchd ovs-vsctl del-port br-int tapc0f9a508-89

* The following command could be used for ``monitoring`` those ports

.. code-block:: console

   # docker exec -it openvswitch_vswitchd ovs-vsctl show | grep -c -B1 "tag: 4095"
   5
   # docker exec -it openvswitch_vswitchd ovs-vsctl show | grep -B1 "tag: 4095"
           Port "tapc0f9a508-89"
               tag: 4095
   ...

Orphaned ports - without tag
============================

.. code-block:: console

   docker exec -it openvswitch_vswitchd ovs-vsctl show
   ...
           Port "tap7f14056f-61"
               Interface "tap7f14056f-61"
                   type: internal
           Port "tap646cf885-cf"
               Interface "tap646cf885-cf"
                   type: internal
   ...

* Those ports drop many packages, this costs CPU time

.. code-block:: console

   # docker exec -it openvswitch_vswitchd ovs-ofctl dump-ports br-int
   ...
     port "tap7f14056f-61": rx pkts=, bytes=, drop=123456789, errs=, frame=, over=, crc=
           tx pkts=, bytes=, drop=123456789, errs=, coll=

* Port in ``OpenStack``

.. code-block:: console

   # openstack --os-cloud admin port list | grep 7f14056f-61
   | ID             | Name | MAC Address | Fixed IP Addresses                                |
   | 7f14056f-61... |      | fa:16:...   | {"subnet_id": "subnetUUID", "ip_address": "IP"}   |

* Sometimes there is no port in ``OpenStack``

.. code-block:: console

   # openstack --os-cloud admin port list | grep 7f14056f-61
   | ID             | Name | MAC Address | Fixed IP Addresses                                |

* Port on host ``DOWN``

.. code-block:: console

   # ip address show tap7f14056f-61
   356: tap7f14056f-61: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
       link/ether 2a:fb:4b:a3:45:f2 brd ff:ff:ff:ff:ff:ff

* Delete port in ``OpenStack`` if present

.. code-block:: console

   # openstack --os-cloud admin port delete 7f14056f-61...

* Delete port in ``OVS``

.. code-block:: console

   # docker exec -it openvswitch_vswitchd ovs-vsctl del-port br-int tap7f14056f-61

* The following command could be used for ``monitoring`` those ports

.. code-block:: console

   # docker exec -it openvswitch_vswitchd ovs-vsctl show | grep -A1 "Port " | grep -v tag | grep -i interface | grep -c tap
   5
   # docker exec -it openvswitch_vswitchd ovs-vsctl show | grep -A1 "Port " | grep -v tag | grep -i interface | grep tap
               Interface "tap7f14056f-61"
   ...
