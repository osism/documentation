=========
OpenStack
=========

Debugging services
==================

Sometimes OpenStack services are hard to debug, when there is important logging
information missing. If a service is not running as expected, but no useful
logging information is produced by the service, attaching via ``strace`` to the
process of the service might reveal, what the process is doing.

Find the process id of the OpenStack service in question.

.. code-block:: console

   pgrep -a cinder-volume
   2814

Attach with strace to the process.

.. code-block:: console

   strace -p 2814

Nested virtualisation
=====================

AMD
---

.. code-block:: console

   echo "options kvm-amd nested=y" | sudo tee /etc/modprobe.d/kvm-nested-virtualization.conf
   sudo modprobe -r kvm_amd
   sudo modprobe kvm_amd
   cat /sys/module/kvm_amd/parameters/nested
   Y
   docker restart nova_libvirt

Intel
-----

.. code-block:: console

   echo "options kvm-intel nested=y" | sudo tee /etc/modprobe.d/kvm-nested-virtualization.conf
   sudo modprobe -r kvm_intel
   sudo modprobe kvm_intel
   cat /sys/module/kvm_intel/parameters/nested
   Y
   docker restart nova_libvirt

References
----------

* https://docs.openstack.org/devstack/latest/guides/devstack-with-nested-kvm.html

Support of QCOW2 images
=======================

Do not use QCOW2 images. Only use RAW images.

* https://support.metacloud.com/hc/en-us/articles/234955888-Converting-QCOW2-Images-to-RAW-with-Ceph-Root-Disk
* http://docs.metacloud.com/latest/user-guide/converting-images/

Performance tweaks via image extra properties
=============================================

* https://redhatstackblog.redhat.com/2017/01/18/9-tips-to-properly-configure-your-openstack-instance/
* http://ceph.com/planet/more-recommendations-for-ceph-and-openstack/

Virtio SCSI
===========

Set ``hw_scsi_model=virtio-scsi`` and ``hw_disk_bus=scsi``.

.. code-block:: console

   $ openstack image set
     --property hw_scsi_model=virtio-scsi
     --property hw_disk_bus=scsi
     <name or ID of your image>

Virtio Multiqueuing
===================

OS/distribution type
====================

Set ``os_type`` (``linux`` or ``windows``) and ``os_distro``.

Possible values for ``os_distro`` can be found under

https://docs.openstack.org/python-glanceclient/latest/cli/property-keys.html.

Alternatively, the program ``osinfo-query`` contained in the package ``libosinfo-bin`` can be used.

.. code-block:: console

   $ osinfo-query os
    Short ID    | Name                    | Version | ID
   -------------+-------------------------+---------+---------------------------------
    altlinux1.0 | Mandrake RE Spring 2001 | 1.0     | http://altlinux.org/altlinux/1.0
    altlinux2.0 | ALT Linux 2.0           | 2.0     | http://altlinux.org/altlinux/2.0
   [...]

Empty action list in Mistral
============================

Solution
--------

You have to populate the database.

.. code-block:: console

   $ docker exec -it mistral_api mistral-db-manage --config-file /etc/mistral/mistral.conf populate

RPCVersionCapError
==================

RPC (Remote Procedure Call) versions of Nova services are not allowed to differ too much
For example a `nova-compute` service from OpenStack Pike release will not be able to
communicate to a `nova-conductor` service from OpenStack Rocky release.

By default, the Nova services try to use the oldest RPC version. It detects this version
automatically by searching the database for the service with the oldest version. This
behaviour can be adjusted with the `upgrade_levels` parameters.

Disabled services in the Nova database are still considered. So you should delete them
from Nova, when they are not present anymore (and therefore won't be upgraded).


If there are disabled services with old versions still registered with Nova, you will
receive an error like the following:

.. code-block:: console

   Exception during message handling: RPCVersionCapError: Requested message version, 5.0 is incompatible.  It needs to be equal in major version and less than or equal in minor version as the specified version cap 4.17.
   12:05:33.840 35 ERROR oslo_messaging.rpc.server Traceback (most recent call last):
   12:05:33.840 35 ERROR oslo_messaging.rpc.server   File "/var/lib/kolla/venv/local/lib/python2.7/site-packages/oslo_messaging/rpc/server.py", line 163, in _process_incoming
   12:05:33.840 35 ERROR oslo_messaging.rpc.server     res = self.dispatcher.dispatch(message)
   12:05:33.840 35 ERROR oslo_messaging.rpc.server   File "/var/lib/kolla/venv/local/lib/python2.7/site-packages/oslo_messaging/rpc/dispatcher.py", line 265, in dispatch
   12:05:33.840 35 ERROR oslo_messaging.rpc.server     return self._do_dispatch(endpoint, method, ctxt, args)
   12:05:33.840 35 ERROR oslo_messaging.rpc.server   File "/var/lib/kolla/venv/local/lib/python2.7/site-packages/oslo_messaging/rpc/dispatcher.py", line 194, in _do_dispatch
   12:05:33.840 35 ERROR oslo_messaging.rpc.server     result = func(ctxt, **new_args)
   12:05:33.840 35 ERROR oslo_messaging.rpc.server   File "/var/lib/kolla/venv/local/lib/python2.7/site-packages/nova/conductor/manager.py", line 1396, in schedule_and_build_instances
   12:05:33.840 35 ERROR oslo_messaging.rpc.server     limits=host.limits, host_list=host_list)
   12:05:33.840 35 ERROR oslo_messaging.rpc.server   File "/var/lib/kolla/venv/local/lib/python2.7/site-packages/nova/compute/rpcapi.py", line 1064, in build_and_run_instance
   12:05:33.840 35 ERROR oslo_messaging.rpc.server     cctxt.cast(ctxt, 'build_and_run_instance', **kwargs)
   12:05:33.840 35 ERROR oslo_messaging.rpc.server   File "/var/lib/kolla/venv/local/lib/python2.7/site-packages/oslo_messaging/rpc/client.py", line 151, in cast
   12:05:33.840 35 ERROR oslo_messaging.rpc.server     self._check_version_cap(msg.get('version'))
   12:05:33.840 35 ERROR oslo_messaging.rpc.server   File "/var/lib/kolla/venv/local/lib/python2.7/site-packages/oslo_messaging/rpc/client.py", line 128, in _check_version_cap
   12:05:33.840 35 ERROR oslo_messaging.rpc.server     version_cap=self.version_cap)
   12:05:33.840 35 ERROR oslo_messaging.rpc.server RPCVersionCapError: Requested message version, 5.0 is incompatible.  It needs to be equal in major version and less than or equal in minor version as the specified version cap 4.17.
   12:05:33.840 35 ERROR oslo_messaging.rpc.server

To verify your problem, take a look inside the `nova` database at the `services` table.
You can find the service version in the `version` column.

Output before and after removing old disabled `nova-compute` services:

.. code-block:: console

   nova-consoleauth.log: 12:38:01.998 7 INFO nova.compute.rpcapi [req-7bc75c8d-a3c2-4961-81d3-91e2cfe2f382 - - - - -] Automatically selected compute RPC version 4.17 from minimum service version 22
   ...
   $ openstack compute service delete...
   ...
   nova-consoleauth.log: 13:43:15.488 7 INFO nova.compute.rpcapi [req-48feeaab-63f0-44a7-b2fe-90134ec61d82 - - - - -] Automatically selected compute RPC version 5.0 from minimum service version 35

Solution 1
----------

* You have to upgrade all your registered Nova services. They are allowed to differ one release,
  but not more.
* You have to delete old disabled services from the Nova database.

.. code-block:: console

   $ openstack compute service list
   $ openstack compute service delete ...

Solution 2
----------

To verify your problem, take a look inside the `nova` database at the `services` table.
You can find the service version in the `version` column. If this `version` numbers are the same, please restart `nova_compute` on hypervisors.

.. code-block:: console

   $ docker restart nova_compute

* order of upgrade nova

  * first the hypervisors, after restart the old RPC version number is used, because the controller are on old version
  * after upgrade of controller, the new RPC version number is choosen by controller, but computes are on the old RPC version number

Instance Allocation
===================

If you see a similar message in ``nova-compute.log``

.. code-block:: console

   hostA
   Instance 44c356ef-edd0-43a3-bd46-17aed65ea1a6 has allocations against this compute host
   but is not found in the database.

you can fix this with the following workflow

openstack placement client
--------------------------

* search for the UUID of the hypervisor

.. code-block:: console

   openstack --os-cloud admin resource provider list | grep hostA
   | a411305a-6472-454b-a593-06bfa21e84e0 | hostA            |          2 |

* find allocations of hypervisor

.. code-block:: console

   openstack --os-cloud admin resource provider allocation show a411305a-6472-454b-a593-06bfa21e84e0
   +--------------------------------------+------------+-----------------------------------------------+
   | resource_provider                    | generation | resources                                     |
   +--------------------------------------+------------+-----------------------------------------------+
   | 44c356ef-edd0-43a3-bd46-17aed65ea1a6 |         30 | {'DISK_GB': 10, 'MEMORY_MB': 1024, 'VCPU': 1} |
   +--------------------------------------+------------+-----------------------------------------------+

* delete the allocation

.. code-block:: console

   openstack --os-cloud admin resource provider allocation delete 44c356ef-edd0-43a3-bd46-17aed65ea1a6

curl
----

* first export some variables (Placement Endpoint and Token

.. code-block:: console

   openstack --os-cloud admin endpoint list --service placement
   | 959ce6527fe742e49c5a6e76f40a04c3 | availability-zone | placement  | placement  | True  | admin     | http://api01:8780   |
   | bf471ab6830f4e8faeffbc74e6173c2a | availability-zone | placement  | placement  | True  | public    | https://api02:8780  |
   | de3778d38b674c2c824a9b7a02340c03 | availability-zone | placement  | placement  | True  | internal  | http://api01:8780   |

   export PLACEMENT_ENDPOINT=$(openstack --os-cloud admin endpoint list --service placement | grep internal | awk -F"|" '{ print $8 }')

   openstack --os-cloud admin token issue
   +------------+----------------------------------+
   | Field      | Value                            |
   +------------+----------------------------------+
   | expires    | 2020-02-18T15:19:47+0000         |
   | id         | token                            |
   | project_id | a3a35b63df1941ba9133897f0e89eb5b |
   | user_id    | ddac12227a2540ea97fa4e1db5a651da |
   +------------+----------------------------------+

   export OS_TOKEN=$(openstack --os-cloud admin token issue | grep " id " | awk -F"|" '{ print $3 }')

* search for the UUID of the hypervisor

.. code-block:: console

   curl -s \
        -H "accept: application/json" \
        -H "User-Agent: nova-scheduler keystoneauth1/3.4.0 python-requests/2.14.2 CPython/2.7.5" \
        -H "OpenStack-API-Version: placement 1.17" \
        -H "X-Auth-Token: $OS_TOKEN" \
        "$PLACEMENT_ENDPOINT/resource_providers" \
        | python -m json.tool | grep hostA -A3
            "name": "hostA",
            "parent_provider_uuid": null,
            "root_provider_uuid": "a411305a-6472-454b-a593-06bfa21e84e0",
            "uuid": "a411305a-6472-454b-a593-06bfa21e84e0"

* find allocations of hypervisor

.. code-block:: console

   curl -s \
        -H "accept: application/json" \
        -H "User-Agent: nova-scheduler keystoneauth1/3.4.0 python-requests/2.14.2 CPython/2.7.5" \
        -H "OpenStack-API-Version: placement 1.17" \
        -H "X-Auth-Token: $OS_TOKEN" \
        "$PLACEMENT_ENDPOINT/resource_providers/a411305a-6472-454b-a593-06bfa21e84e0/allocations" \
        | python -m json.tool
        {
            "allocations": {
               "44c356ef-edd0-43a3-bd46-17aed65ea1a6": {
                  "resources": {
                     "DISK_GB": 10,
                     "MEMORY_MB": 1024,
                     "VCPU": 1
                  }
               }
            },
            "resource_provider_generation": 30
         }

* delete the allocation

.. code-block:: console

   curl -s \
        -H "accept: application/json" \
        -H "User-Agent: nova-scheduler keystoneauth1/3.4.0 python-requests/2.14.2 CPython/2.7.5" \
        -H "OpenStack-API-Version: placement 1.17" \
        -H "X-Auth-Token: $OS_TOKEN" \
        "$PLACEMENT_ENDPOINT/allocations/44c356ef-edd0-43a3-bd46-17aed65ea1a6" \
        -X DELETE
