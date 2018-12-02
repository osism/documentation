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

   $ echo "options vxlan log_ecn_error=N" sudo tee /etc/modprobe.d/osism-vxlan.conf
