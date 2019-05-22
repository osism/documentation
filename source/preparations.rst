============
Preparations
============

.. contents::
   :local:

Manual installation
===================

The manual installation is completely possible without network connectivity.

Preparations
------------

* Download the latest ISO image for Ubuntu 18.04 from http://cdimage.ubuntu.com/releases/18.04/release/

  * Use the ``ubuntu-18.04.2-server-amd64.iso`` image
  * Do not use the ``ubuntu-18.04.2-live-server-amd64.iso`` image
  * The version number may be different, always use the latest available version of 18.04 LTS

* Create a bootable USB stick from this ISO image. Alternatively you can also work with a CD
* Perform a hardware RAID configuration if necessary
* Boot bare-metal server from this USB stick/CD

Partitioning
------------

* The use of a RAID is recommended
* The use of a LVM2 is recommended
* The use of own file systems for the following mountpoints is recommended

  * ``/``
  * ``/home``
  * ``/tmp``
  * ``/var/lib/docker`` (do not set the nosuid flag on ``/var/lib/docker``)
  * ``/var/log/audit``
  * ``/var/log``
  * ``/var``

* The use of a swap partition is recommended

When using XFS as the file system for ``/var/lib/docker``, note the following: Running on XFS without d_type support now causes Docker to skip the attempt to use the overlay or overlay2 driver.

  * https://linuxer.pro/2017/03/what-is-d_type-and-why-docker-overlayfs-need-it/
  * https://docs.docker.com/storage/storagedriver/overlayfs-driver/

Installation
------------

* Choose ``English`` as language
* Choose ``Install Ubuntu Server``
* Choose ``English`` as language (again)
* Choose your location (e.g. ``Germany``)
* Choose ``en_US.UTF-8`` as locale
* Choose the keyboard layout from a list, use ``English (US)``
* Choose and configure the primary network interface

  * Depending on the environment, the network may not work at this point.
    Then select any interface and then select ``Do not configure the network at this time``
    in the next step.

* Set the hostname (the hostname is ``60-10`` and not ``60-10.betacloud.xyz``)
* Set ``ubuntu`` as full name for the new user
* Set ``ubuntu`` as the username for the account
* Set a password for the account

  * The account is only needed initially and can be deleted
    after completion of the bootstrap.

* Choose ``Manual`` as partitioning method and execute the partitioning according to
  company specifications

  * The use of LVM2 and RAID1 is recommended.
  * Do not assign the entire storage to the LV for ``/``.
  * Booting from a ``/boot`` logical volume on a software raid is possible.
  * At this point, only configure devices that are required for the system
    installation. Devices which are dedicated for e.g. Docker or Ceph are
    not configured here.

* Choose ``No automatic updates``
* Choose ``OpenSSH server`` as software to install
* After completion, restart the system

.. note::

   ``python-minimal`` must be installed on the systems.

Post-processing
---------------

After the first boot depending on the environment it is necessary to create the network
configuration for the management interface manually, because for example bonding or VLANs
should be used.

* https://baturin.org/docs/iproute2/
* https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-vlan_on_bond_and_bridge_using_ip_commands

.. code-block:: console

   # modprobe bonding
   # ip link add bond0 type bond
   # ip link set bond0 type bond miimon 100 mode 802.3ad
   # ip link set enp8s0f0 down
   # ip link set enp8s0f0 master bond0
   # ip link set enp8s0f1 down
   # ip link set enp8s0f1 master bond0
   # ip link set bond0 up
   # cat /proc/net/bonding/bond0

.. code-block:: console

   # ip link add link bond0 name vlan101 type vlan id 101
   # ip link set vlan101 up

.. code-block:: console

   $ ip address add 172.17.60.10/16 dev vlan101
   # ip route add default via 172.17.40.10

* You may have to set the nameservers in ``/etc/resolv.conf``. Temporarily remove the ``127.0.0.53`` entry.

* At the beginning it is sufficient to be able to reach the system via SSH. The network configuration is
  rolled out during the bootstrap. Therefore a manual configuration is sufficient and recommended.

Seed node
=========

Execute the following commands on the seed node.

* Install required packages

  .. code-block:: console

     $ sudo apt install git python3-pip python3-virtualenv sshpass

* Clone the configuration repository

  .. code-block:: console

     $ git clone ssh://git@git.betacloud-solutions.de:10022/customers/xxx/cfg-yyy.git

If necessary, the deployment key can be used for the initial transfer of the repository.

For this, the following content is added in ``~/.ssh/config`` and the SSH privte key is
stored in ``~/.ssh/id_rsa.configuration``.

.. code-block:: none

   Host git.betacloud-solutions.de
     HostName git.betacloud-solutions.de
     User git
     Port 10022
     IdentityFile ~/.ssh/id_rsa.configuration

Manager node
============

Execute the following commands on the seed node. Execute the commands within the
manager environment (``cd environments/manager``).

You can use a different folder location for the virtual environment that will be created by setting
the environment variable ``VENV_PATH``. This is required for example if your current folder path
contains blank characters.

Various Ansible configurations can be adjusted via environment variables. For example, to query the
password for using ``sudo``, add ``ANSIBLE_BECOME_ASK_PASS=True``. If ``secrets.yml`` files are
encrypted with Ansible Vault, ``ANSIBLE_ASK_VAULT_PASS=True`` is added.

An overview with all parameters can be found at: http://docs.ansible.com/ansible/devel/reference_appendices/config.html#environment-variables

* Creation of the necessary operator user

  .. code-block:: console

     $ ANSIBLE_USER=ubuntu ./run.sh operator

  * If at the beginning the login with a password is required, ``ANSIBLE_ASK_PASS=True`` must be set.
  * If at the beginning the login with an SSH key is required, the key has to be added on the manager
    node to ``authorized_keys`` of the user specified in ``ANSIBLE_USER``.
  * If the error ``/bin/sh: 1: /usr/bin/python: not found`` occurs, Python must first be installed on
    the manager node with ``ANSIBLE_USER=ubuntu ./run.sh python``.
  * To verify the creation of the operator user, use the private key file ``id_rsa.operator``:
    ``ssh -i id_rsa.operator dragon@10.49.20.10``.
  * A typical call to create the operator user looks like this.

    .. code-block:: console

       $ ANSIBLE_BECOME_ASK_PASS=True \
         ANSIBLE_ASK_VAULT_PASS=True \
         ANSIBLE_ASK_PASS=True \
         ANSIBLE_USER=ubuntu \
         ./run.sh operator

  .. warning::

     If the operator user was already created when the operating system was provisioned, this
     role must still be executed. ``ANSIBLE_USER`` is then adjusted accordingly.

     The UID and GID must also be checked. If it is not ``45000``, it must be adapted accordingly.

     .. code-block:: console

        # usermod -u 45000 dragon
        # groupmod -g 45000 dragon

        # chgrp dragon /home/dragon/
        # chown dragon /home/dragon/

        # find /home/dragon -group 1000 -exec chgrp -h dragon {} \;
        # find /home/dragon -user 1000 -exec chown -h dragon {} \;

* If Ansible Vault is used, the ``ANSIBLE_ASK_VAULT_PASS`` variable will be used accordingly

  .. code-block:: console

     $ export ANSIBLE_ASK_VAULT_PASS=True

* Configuration of the network

  .. code-block:: console

     $ ./run.sh network

  * The network configuration already present on a system should be saved before this step.
  * We are currently still using ``/etc/network/interfaces``. Therefore rename all files below ``/etc/netplan`` to ``X.unused``.
  * Upon completion of this step, a system reboot should be performed to ensure that the
    configuration is functional and reboot secure. Since network services are not
    restarted automatically, later changes to the network configuration are not effective
    without a manual restart of the network service or reboot of the nodes.
  * A reboot is performed to activate and test the network configuration.
    The reboot must be performed before the bootstrap is performed.

    .. code-block:: console

       $ ./run.sh reboot

* Bootstrap of the manager node

  .. code-block:: console

     $ ./run.sh bootstrap


  * After the bootstrap check if a reboot is required by checking if the file
    ``/var/run/reboot-required`` exists.  Regardless of whether a reboot is
    necessary or not, a reboot should be performed.

* Transfer configuration repository

  .. code-block:: console

     $ ./run.sh configuration

* Deployment of necessary manager services

  .. code-block:: console

     $ ./run.sh manager

Configuration
=============

There are three possibilities to update the configuration repository on the manager node.

On the seed node change into the manager environment and use the following command. This will update the configuration repository on the manager node.

.. code-block:: console

   $ ./run.sh configuration

On the manager node use the following command to update the configuration repository.

.. code-block:: console

   $ osism-generic configuration

Alternatively, Git itself can be used on the manager node to update the repository.

.. code-block:: console

   $ cd /opt/configuration
   $ ssh-agent bash -c 'ssh-add ~/.ssh/id_rsa.configuration; git pull'

Infrastructure services
=======================

The deployment of these infrastructure services is optional.

Execute the following commands on the manager node.

Cobbler
-------

.. code-block:: console

   $ osism-infrastructure cobbler

Mirror
------

.. code-block:: console

   $ osism-infrastructure mirror

After the bootstrap of the mirror services they have to be synchronized. Depending on
the bandwidth, this process will take several hours.

.. code-block:: console

   $ osism-mirror images
   $ osism-mirror packages
