==========================
Preparation of the servers
==========================

.. contents::
   :depth: 2

The manual installation of a system is described below. The use of an installation server
is recommended

The manual node installation is possible without network connectivity.

Preparations
============

* Download the latest ISO image for Ubuntu 22.04 from

  * https://www.releases.ubuntu.com/22.04/
  * Use the ``ubuntu-22.04.1-live-server-amd64.iso`` image
  * The version number may be different, always use the latest available version of 22.04 LTS

* Or use the prepared ISO, provided at https://github.com/osism/node-image

  * Details on the use can be found there
  * Only works with specific disc layouts (listed in the README)

Manual Installation
===================

.. note::

   The screenshots and instructions were created with Ubuntu 20.04. It is similar with Ubuntu 22.04,
   but the screenshots differ.

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

* Set the hostname (the hostname is ``node`` and not ``node.systems.osism.xyz``)

  * Adapt the host name accordingly as you need it yourself. ``node`` is only an
    example.

* Set ``ubuntu`` as full name for the new user
* Set ``ubuntu`` as the username for the account

  * The later used operator user ``dragon`` is created during the bootstrap
    and should not be created during the installation.

* Set a password for the account

  * The account is only needed initially and can be deleted
    after completion of the bootstrap.

* Choose ``Manual`` as partitioning method and execute the partitioning according to
  company specifications

  * Details can be found in section :ref:`partitioning`

* Choose ``No automatic updates``
* Choose ``OpenSSH server`` as software to install

  .. note::

     Do not install any other software component. Everything you need will be installed
     later by OSISM. In particular, it is not necessary to install a desktop environment.

* After completion, restart the system

.. note::

   ``python3-minimal`` must be installed on the systems.

.. _partitioning:

Node Partitioning
-----------------

* The use of a UEFI is recommended
* The use of a RAID is recommended

  .. note::

     We prefer the use of software RAIDs to make us less dependent on hardware. But there is nothing against
     using hardware RAIDs.

* The use of a LVM2 is recommended

  * ``system`` is recommended as the name for the volume group

  .. note::

     Dedicated disks may be provided for ``/var/lib/docker`` on the controller nodes. In this case, do
     not use an LV for ``/var/lib/docker`` but the devices provided for it.

* Do not configure devices that are not required for the operating system

The use of own file systems for the following mountpoints is recommended. The minimum size and a recommended name
for the logical volume are noted.

  * ``/`` (10 GByte, logical volume ``root``)
  * ``/home`` (2 GByte, logical volume ``home``)
  * ``/tmp`` (5 GByte, logical volume ``tmp``)
  * ``/var/lib/ceph`` (50 GByte, logical volume ``ceph``) (optional for storage nodes)
  * ``/var/lib/docker`` (30 GByte, logical volume ``docker``, do not set the ``nosuid`` flag on ``/var/lib/docker``)
  * ``/var/log/audit`` (1 GByte, logical volume ``audit``)
  * ``/var`` (10 GByte, logical volume ``var``)
  * ``swap`` (min 8 GByte, logical volume ``swap``)

  .. note::

     The size of the individual partitions is minimal. Depending on the node type, the individual
     partitions should be made larger. This applies in particular to ``/var/lib/docker``. On controllers
     at least 100 GByte should be used.

     A later enlargement is possible during operation.

     .. code-block::

        # lvextend -L +10G /dev/mapper/system-docker
        # resize2fs -p /dev/mapper/system-docker

The following is a sample view from the Ubuntu installer. This view may vary depending on the environment.

.. image:: /images/installation-partition-disks.png

.. note::

   When using XFS as the file system for ``/var/lib/docker``, note the following: Running on XFS
   without d_type support now causes Docker to skip the attempt to use the overlay or overlay2 driver.

   https://docs.docker.com/storage/storagedriver/overlayfs-driver/

Screenshots
-----------

Step by step of manual installation with screenshots.

* Boot via CD-ROM/ISO Ubuntu and choose ``Install Ubuntu Server``

  .. image:: /images/manual-installation/01-grub.png

* Select language ``English``

  .. image:: /images/manual-installation/02-language.png

* Select your country, e.g. Europe/Germany

  .. image:: /images/manual-installation/03-country.png
  .. image:: /images/manual-installation/04-location.png
  .. image:: /images/manual-installation/05-location.png

* Choose ``en_US.UTF-8`` as locale

  .. image:: /images/manual-installation/06-locales.png

* Do **not** detect Keyboard layout

  .. image:: /images/manual-installation/07-keyboard-detect.png

* Choose Keyboard Country ``English (US)``

  .. image:: /images/manual-installation/08-keyboard-select.png

* Keyboard layout ``English (US)``

  .. image:: /images/manual-installation/09-keyboard-layout.png

* Choose your Hostname, e.g. node, manager, compute, controller, ctrl, com, sto, ...

  .. image:: /images/manual-installation/10-hostname.png

* Full name of User, ``ubuntu``

  .. image:: /images/manual-installation/11-username-full.png

* username ``ubuntu``

  .. image:: /images/manual-installation/12-username.png

* Set password

  .. image:: /images/manual-installation/13-password.png
  .. image:: /images/manual-installation/14-password-reenter.png

* Set Timezone, e.g. ``Europe/Berlin``

  .. image:: /images/manual-installation/15-timezone.png

* Partitioning - Choose the ``Guided - use entire disk and set up LVM`` entry

  .. image:: /images/manual-installation/16-partition.png

* Choose the first disk

  .. image:: /images/manual-installation/17-partition.png

* Write the changes to disk

  .. image:: /images/manual-installation/18-partition.png

* Continue with the suggested value

  .. image:: /images/manual-installation/19-partition.png

* ``Configure the Logical Volume Manager``

  .. image:: /images/manual-installation/20-partition.png

* Write the changes to disk

  .. image:: /images/manual-installation/21-partition.png

* Delete all suggested Logical Volumes

  .. image:: /images/manual-installation/22-partition.png
  .. image:: /images/manual-installation/23-partition.png

* Create LVs like here :ref:`partitioning` with ext4

  .. image:: /images/manual-installation/24-partition.png
  .. image:: /images/manual-installation/25-partition.png
  .. image:: /images/manual-installation/26-partition.png
  .. image:: /images/manual-installation/27-partition.png
  .. image:: /images/manual-installation/28-partition.png
  .. image:: /images/manual-installation/29-partition.png
  .. image:: /images/manual-installation/30-partition.png
  .. image:: /images/manual-installation/31-partition.png
  .. image:: /images/manual-installation/32-partition.png
  .. image:: /images/manual-installation/33-partition.png
  .. image:: /images/manual-installation/34-partition.png

* For ``swap`` LV use ``swap area``

  .. image:: /images/manual-installation/35-partition-swap.png
  .. image:: /images/manual-installation/36-partition-swap.png

* The partitioning should look like this

  .. image:: /images/manual-installation/37-partition.png

* Write the changes to disk

  .. image:: /images/manual-installation/38-partition.png

* Installation will be started

  .. image:: /images/manual-installation/39-installation.png

* Proxy?

  .. image:: /images/manual-installation/40-proxy.png
  .. image:: /images/manual-installation/41-installation.png

* Choose ``No automatic updates``

  .. image:: /images/manual-installation/42-autoupdate.png

* Choose ``OpenSSH server`` to install

  .. image:: /images/manual-installation/43-openssh.png
  .. image:: /images/manual-installation/44-installation.png

* After finished installation, choose ``Continue`` for reboot

  .. image:: /images/manual-installation/45-complete.png

* After reboot the installed Grub looks like this

  .. image:: /images/manual-installation/46-installed-grub.png

* Finaly the login prompt appears

  .. image:: /images/manual-installation/47-installed-prompt.png

Post-processing
===============

EFI partitions
--------------

* https://askubuntu.com/questions/1066028/install-ubuntu-18-04-desktop-with-raid-1-and-lvm-on-machine-with-uefi-bios

.. code-block:: console

   # lsblk
   NAME                MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
   sda                   8:0    0 59.6G  0 disk
   ├─sda1                8:1    0  476M  0 part  /boot/efi
   └─sda2                8:2    0 59.2G  0 part
     └─md0               9:0    0 59.1G  0 raid1
       ├─system-root   253:0    0  9.3G  0 lvm   /
       ├─system-swap   253:1    0  7.5G  0 lvm   [SWAP]
       ├─system-tmp    253:2    0  1.9G  0 lvm   /tmp
       ├─system-audit  253:3    0  952M  0 lvm   /var/log/audit
       ├─system-var    253:4    0  9.3G  0 lvm   /var
       ├─system-docker 253:5    0  9.3G  0 lvm   /var/lib/docker
       └─system-home   253:6    0  1.9G  0 lvm   /home
   sdb                   8:16   0 59.6G  0 disk
   ├─sdb1                8:17   0  476M  0 part
   └─sdb2                8:18   0 59.2G  0 part
     └─md0               9:0    0 59.1G  0 raid1
       ├─system-root   253:0    0  9.3G  0 lvm   /
       ├─system-swap   253:1    0  7.5G  0 lvm   [SWAP]
       ├─system-tmp    253:2    0  1.9G  0 lvm   /tmp
       ├─system-audit  253:3    0  952M  0 lvm   /var/log/audit
       ├─system-var    253:4    0  9.3G  0 lvm   /var
       ├─system-docker 253:5    0  9.3G  0 lvm   /var/lib/docker
       └─system-home   253:6    0  1.9G  0 lvm   /home

.. code-block:: console

   # dd if=/dev/sda1 of=/dev/sdb1

.. code-block:: console

   # efibootmgr -v | grep ubuntu
   Boot0000* ubuntu	HD(1,GPT,f6b80cef-a636-439a-b2c2-e30bc385eada,0x800,0xee000)/File(\EFI\UBUNTU\SHIMX64.EFI)
   Boot0018* ubuntu	HD(1,GPT,f6b80cef-a636-439a-b2c2-e30bc385eada,0x800,0xee000)/File(\EFI\UBUNTU\GRUBX64.EFI)

.. code-block:: console

   # efibootmgr -c -d /dev/sdb -p 1 -L "ubuntu2" -l "\EFI\UBUNTU\GRUBX64.EFI"
   # efibootmgr -c -d /dev/sdb -p 1 -L "ubuntu2" -l "\EFI\UBUNTU\SHIMX64.EFI"

Network
-------

After the first boot depending on the environment it is necessary to create the network
configuration for the management interface manually, because for example bonding or VLANs
should be used.

The following examples shows how the configuration can be done with ``netplan`` or ``iproute2``.

.. note::

   The examples are not the final network configuration. It is a minimal sample network
   configuration for initial access to the systems.

   The example configuration differs depending on the environment. The configuration is
   not a recommendation for the network design. It's just an example configuration.

   It is not necessary to manually create the finale network configuration. The final
   network configuration of the environment is defined during the creation of the
   configuration repository. The network final network configuration is depoyed during
   the bootstrap on the systems.

iproute2
~~~~~~~~

* https://baturin.org/docs/iproute2/
* https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-vlan_on_bond_and_bridge_using_ip_commands
* https://www.kernel.org/doc/Documentation/networking/bonding.txt

.. code-block:: console

   # modprobe bonding
   # ip link add bond0 type bond
   # ip link set bond0 type bond miimon 100 mode 802.3ad lacp_rate 1
   # ip link set eno1 down
   # ip link set eno1 master bond0
   # ip link set eno2 down
   # ip link set eno2 master bond0
   # ip link set bond0 up
   # cat /proc/net/bonding/bond0

.. code-block:: console

   # ip link add link bond0 name vlan101 type vlan id 101
   # ip link set vlan101 up

.. code-block:: console

   # ip address add 172.17.60.10/16 dev vlan101
   # ip route add default via 172.17.40.10

* You may have to set the nameservers in ``/etc/resolv.conf``. Temporarily remove the ``127.0.0.53`` entry.

Netplan
~~~~~~~

* https://netplan.io/examples
* configure ``/etc/netplan/01-netcfg.yaml``

.. code-block:: yaml

   ---
   network:
     version: 2
     renderer: networkd
     ethernets:
       eno1:
	 dhcp4: no
       eno2:
	 dhcp4: no
     bonds:
       bond0:
	 dhcp4: no
	 interfaces:
	   - eno1
	   - eno2
	 parameters:
	   mode: 802.3ad
	   lacp-rate: fast
           mii-monitor-interval: 100
     vlans:
       vlan101:
	 id: 101
	 link: bond0
	 addresses: [ "172.17.60.10/16" ]
	 routes:
	  - to: 0.0.0.0/0
	    via: 172.17.40.10
	 nameservers:
	   search: [ betacloud.xyz ]
	   addresses: [ "8.8.8.8", "8.8.4.4" ]

.. code-block:: console

   # netplan apply

ACPI Error
----------

If you see this messages in ``dmesg``, logs or ``journal``

.. code-block:: console

   ACPI Error: SMBus/IPMI/GenericSerialBus write requires Buffer of length 66, found length 32 (20150930/exfield-418)
   ACPI Error: Method parse/execution failed [\_SB.PMI0._PMM] (Node ffff8807ff5bd438), AE_AML_BUFFER_LIMIT (20150930/psparse-542)
   ACPI Exception: AE_AML_BUFFER_LIMIT, Evaluating _PMM (20150930/power_meter-338)

blacklist and unload kernel module ``acpi_power_meter``.

* https://access.redhat.com/solutions/48109
