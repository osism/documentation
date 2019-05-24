============
Installation
============

The manual node installation is completely possible without network connectivity.

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

  * The later used operator user ``dragon`` is created during the bootstrap
    and should not be created during the installation.

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

