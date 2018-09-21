=====
Kolla
=====

Ocata -> Pike
=============

Docker
------

.. note::

   This task is only necessary on Ubuntu 16.04 because there the ``python-docker`` package is too old.

.. note::

   It's a good idea to do a Docker upgrade as part of an OpenStack upgrade.

.. code-block:: none

   fatal: [20-10.betacloud.xyz]: FAILED! => {"changed": true, "failed": true, "msg": "'Traceback (most recent call last):\\n  File \"/tmp/ansible_Lrxpgg/ansible_module_kolla_docker.py\", line 804, in main\\n    dw = DockerWorker(module)\\n  File \"/tmp/ansible_Lrxpgg/ansible_module_kolla_docker.py\", line 218, in __init__\\n    self.dc = get_docker_client()(**options)\\n  File \"/tmp/ansible_Lrxpgg/ansible_module_kolla_docker.py\", line 201, in get_docker_client\\n    return docker.APIClient\\nAttributeError: \\'module\\' object has no attribute \\'APIClient\\'\\n'"}

.. code-block:: console

   $ osism-generic docker

Inventory
---------

* Add new host groups to ``inventory/hosts`` to the ``environment: kolla`` section

.. code-block:: ini

   # neutron

   [...]

   [neutron-bgp-dragent:children]
   network

.. code-block:: ini

   # neutron

   [...]

   [openvswitch:children]
   network
   compute

.. code-block:: ini

   ##########################################################
   # environment: kolla

   [...]

   [redis:children]
   control

Pike -> Queens
==============

Queens -> Rocky
===============
