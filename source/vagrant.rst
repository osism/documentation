===================
Vagrant environment
===================

Vagrant environment available at https://github.com/osism/vagrant.

Prepare host
============

.. code-block:: shell

   $ ansible-playbook playbook-vagrant -i localhost,
   $ sudo add-apt-repository ppa:ansible/ansible
   $ sudo apt-get update
   $ sudo apt-get install ansible

Configure environment
=====================

.. todo:: Explain configuration (node numbers, resources, networks) of vagrant environment here.

Provision step by step
======================

Create nodes
------------

.. note:: Run the following commands on the vagrant host.

1. Create instances

   .. code-block:: shell

      $ vagrant up --no-provision

2. Copy publich ssh key

   .. code-block:: shell

      $ vagrant provision --provision-with prepare

Check nodes
-----------

.. note:: Run the following commands on the vagrant host.

.. code-block:: shell

   $ vagrant status
   Current machine states:

   osism-controller-0        running (virtualbox)
   osism-controller-1        running (virtualbox)
   osism-controller-2        running (virtualbox)
   osism-controller-3        running (virtualbox)
   osism-compute-0           running (virtualbox)
   osism-compute-1           running (virtualbox)
   osism-compute-2           running (virtualbox)
   osism-network-0           running (virtualbox)
   osism-network-1           running (virtualbox)
   osism-network-2           running (virtualbox)
   osism-storage-0           running (virtualbox)
   osism-storage-1           running (virtualbox)
   osism-storage-2           running (virtualbox)
   osism-storage-3           running (virtualbox)
   osism-manager             running (virtualbox)

   This environment represents multiple VMs. The VMs are all listed
   above with their current state. For more information about a specific
   VM, run `vagrant status NAME`.

Prepare manager node
--------------------

.. note:: Run the following commands on the vagrant host.

1. Create the operator user on the manager node

   .. code-block:: shell

      $ vagrant provision --provision-with operator

2. Prepare the manager node

   .. code-block:: shell

      $ vagrant provision --provision-with bootstrap

3. Clone the configuration repository on the manager node

   .. code-block:: shell

      $ vagrant provision --provision-with configuration

4. Generate the environment specific ``hosts`` file

   .. code-block:: shell

      $ vagrant provision --provision-with custom-hosts

5. Start the helper containers on the manager node

   .. code-block:: shell

      $ vagrant provision --provision-with manager

Prepare remaining nodes
-----------------------

.. note:: Log in on the manager node by running ``./ssh.sh`` and run the following commands on the manager node.

1. Create the operator user on the nodes

   .. code-block:: shell

      $ osism-generic operator --limit 'all:!manager' -u vagrant --key-file /opt/ansible/secrets/id_rsa.vagrant -e ansible_user=vagrant

2. Gather facts

   .. code-block:: shell

      $ osism-generic facts

3. Prepare the nodes

   .. code-block:: shell

      $ osism-generic bootstrap

Deploy ceph
-----------

.. note:: Log in on the manager node by running ``./ssh.sh`` and run the following commands on the manager node.

1. Gather facts

   .. code-block:: shell

      $ osism-ceph facts

2. Deploy monitor containers

   .. code-block:: shell

      $ osism-ceph mons

3. Deploy manager containers

   .. code-block:: shell

      $ osism-ceph mgrs

3. Deploy osd containers

   .. code-block:: shell

      $ osism-ceph osds

Deploy helper
------------

.. note:: Log in on the manager node by running ``./ssh.sh`` and run the following commands on the manager node.

1. Deploy helper services like phpMyAdmin or ceph client

   .. code-block:: shell

      $ osism-infrastructure helper

Check ceph
----------

.. note:: Log in on the manager node by running ``./ssh.sh`` and run the following commands on the manager node.

.. console-block:: shell

   dragon@osism-manager:~$ ceph status
     cluster:
       id:     20e33ae4-016e-43f9-9cd1-cd8e78838d9e
       health: HEALTH_OK
 
     services:
       mon: 3 daemons, quorum osism-storage-0,osism-storage-1,osism-storage-2
       mgr: osism-storage-1(active), standbys: osism-storage-0, osism-storage-2
       osd: 12 osds: 12 up, 12 in
 
     data:
       pools:   5 pools, 160 pgs
       objects: 0 objects, 0 bytes
       usage:   24635 MB used, 87240 MB / 109 GB avail
       pgs:     160 active+clean

   dragon@osism-manager:~$ ceph osd lspools
   1 images,2 volumes,3 vms,4 backups,5 metrics,

Deploy infrastructure services
------------------------------

.. note:: Log in on the manager node by running ``./ssh.sh`` and run the following commands on the manager node.

1. Gather facts

.. code-block:: shell

   $ osism-kolla _ facts

2. Deploy generic containers like fluentd

.. code-block:: shell

   $ osism-kolla deploy common

3. Deploy elasticsearch

.. code-block:: shell

   $ osism-kolla deploy elasticsearch

4. Deploy haproxy

.. code-block:: shell

   $  osism-kolla deploy haproxy

5. Deploy kibana

.. code-block:: shell

   $ osism-kolla deploy kibana

6. Deploy memcached

.. code-block:: shell

   $ osism-kolla deploy memcached

7. Deploy mariadb

.. code-block:: shell

   $ osism-kolla deploy mariadb

8. Deploy rabbitmq

.. code-block:: shell

   $ osism-kolla deploy rabbitmq

.. note:: Deploy multiple services with ``osism-kolla deploy mariadb,rabbitmq,...``.

Deploy openstack
----------------

.. note:: Log in on the manager node by running ``./ssh.sh`` and run the following commands on the manager node.

1. Deploy keystone with ``osism-kolla deploy keystone``

.. code-block:: shell

   $

2. Deploy glance with ``osism-kolla deploy glance``

.. code-block:: shell

   $

3. Deploy heat with ``osism-kolla deploy heat``

.. code-block:: shell

   $

4. Deploy horizon with ``osism-kolla deploy horizon``

.. code-block:: shell

   $

5. Deploy cinder with ``osism-kolla deploy cinder``

.. code-block:: shell

   $

6. Deploy nova with ``osism-kolla deploy nova``

.. code-block:: shell

   $

7. Deploy neutron with ``osism-kolla deploy neutron``

.. code-block:: shell

   $
