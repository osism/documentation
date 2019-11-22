==================================
Provisioning of bare-metal servers
==================================

.. contents::
   :local:

The manual installation of a system is described below.

The use of an installation server is recommended. Cobbler, which is integrated in OSISM,
can be used for this purpose.

When using Cobbler it is only necessary to manually prepare the bare-metal system used as
manager node. The remaining nodes can then be provisioned using Cobbler.

The manual node installation is completely possible without network connectivity.

Preparations
============

* Download the latest ISO image for Ubuntu 18.04 from http://cdimage.ubuntu.com/releases/18.04/release/

  * Use the ``ubuntu-18.04.2-server-amd64.iso`` image
  * Do not use the ``ubuntu-18.04.2-live-server-amd64.iso`` image
  * The version number may be different, always use the latest available version of 18.04 LTS

* Create a bootable USB stick from this ISO image. Alternatively you can also work with a CD
* Perform a hardware RAID configuration if necessary

  .. note::

     We prefer the use of software RAIDs to make us less dependent on hardware. But there is nothing against
     using hardware RAIDs.

* Boot bare-metal server from this USB stick/CD

Manual Installation
===================

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

  * Details can be found in section :ref:`partitioning`

* Choose ``No automatic updates``
* Choose ``OpenSSH server`` as software to install

  .. note::

     Do not install any other software component. Everything you need will be installed
     later by OSISM. In particular, it is not necessary to install a desktop environment.

* After completion, restart the system

.. note::

   ``python-minimal`` must be installed on the systems.

.. _partitioning:

Partitioning
------------

* The use of a UEFI is recommended
* The use of a RAID is recommended

  .. note::

     We prefer the use of software RAIDs to make us less dependent on hardware. But there is nothing against
     using hardware RAIDs.

* The use of a LVM2 is recommended

  .. note::

     Dedicated disks may be provided for ``/var/lib/docker`` on the controller nodes. In this case, do
     not use an LV for ``/var/lib/docker`` but the devices provided for it.

* Do not configure devices that are not required for the operating system

The use of own file systems for the following mountpoints is recommended:

  * ``/`` (10 GByte)
  * ``/home`` (2 GByte)
  * ``/tmp`` (2 GByte)
  * ``/var/lib/docker`` (30 GByte, do not set the ``nosuid`` flag on ``/var/lib/docker``)
  * ``/var/log/audit`` (1 GByte)
  * ``/var`` (10 GByte)
  * ``swap`` (min 8 GByte)

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

   * https://linuxer.pro/2017/03/what-is-d_type-and-why-docker-overlayfs-need-it/
   * https://docs.docker.com/storage/storagedriver/overlayfs-driver/


Preseed Installation
====================

Prepare Ubuntu Server ISO
-------------------------

* Prepare your environment as root

.. code-block:: console

   $ mkdir /dev/shm/ubuntu-seed
   $ sudo mount -o loop,ro ubuntu-18.04.3-server-amd64.iso /mnt/
   $ cp -rT /mnt /dev/shm/ubuntu-seed

* Edit in both files the first entry as ``root``

.. code-block:: console

   $ vim boot/grub/grub.cfg
   menuentry "Install Ubuntu Server OSISM" {
       set gfxpayload=keep
       linux  /install/vmlinuz auto console-setup/ask_detect=false console-setup/layoutcode=us console-setup/modelcode=pc105 debconf/frontend=noninteractive debian-installer=en_US.UTF-8 fb=false initrd=/install/initrd.gz kbd-chooser/method=us keyboard-configuration/layout=USA keyboard-configuration/variant=USA locale=en_US.UTF-8 noapic preseed/file=/cdrom/preseed/osism-ubuntu-server.seed ---
       initrd /install/initrd.gz
   }
   $ vim isolinux/txt.cfg
   label install
     menu label ^Install Ubuntu Server OSISM
     kernel /install/vmlinuz
     append auto console-setup/ask_detect=false console-setup/layoutcode=us console-setup/modelcode=pc105 debconf/frontend=noninteractive debian-installer=en_US.UTF-8 fb=false initrd=/install/initrd.gz kbd-chooser/method=us keyboard-configuration/layout=USA keyboard-configuration/variant=USA locale=en_US.UTF-8 noapic preseed/file=/cdrom/preseed/osism-ubuntu-server.seed vga=788 initrd=/install/initrd.gz ---

.. note::

   Please use ``:w!`` in vim for writing readonly files

* Create preseed file, :ref:`osism-ubuntu-preseed`

.. code-block:: console

   $ cat preseed/osism-ubuntu-server.seed
   ### Localization

   # Preseeding language, country and locale
   d-i debian-installer/locale string en_US.UTF-8
   ...
   ### Boot loader installation

   d-i grub-installer/grub2_instead_of_grub_legacy boolean true
   d-i grub-installer/only_debian boolean false
   d-i grub-installer/with_other_os boolean true
   d-i grub-installer/bootdev string default
   d-i grub-installer/timeout string 5
   # Avoid that last message about the install being complete.
   d-i finish-install/reboot_in_progress note

* Write new md5sum in reference file, md5sum.txt

.. code-block:: console

   $ md5sum boot/grub/grub.cfg
   39c2565e2d6eff27b806f0b41382db66  boot/grub/grub.cfg
   $ grep grub.cfg md5sum.txt
   ...
   39c2565e2d6eff27b806f0b41382db66  ./boot/grub/grub.cfg

   $ md5sum preseed/osism-ubuntu-server.seed
   09361c56b41e218df314478947491cb3  preseed/osism-ubuntu-server.seed
   $ grep osism md5sum.txt
   09361c56b41e218df314478947491cb3  ./preseed/osism-ubuntu-server.seed

* Build ISO file

.. code-block:: console

   $ mkisofs -U -A "UbuntuOSISM" -V "UbuntuOSISM" -volset "UbuntuOSISM" -J -joliet-long -r -v -T -o /path/to/osism-ubuntu-seed.iso -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -eltorito-alt-boot -e boot/grub/efi.img -no-emul-boot /dev/shm/ubuntu-seed/

.. note::

   Please use console, ALT+F4, for debugging

* Download prepared ISO files (https://share.b1-systems.de/index.php/s/scJLAXPXpG7R0TF)


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

* At the beginning it is sufficient to be able to reach the system via SSH.
* It is not necessary to create the entire network configuration. The network configuration is created during
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

.. code-block:: yaml
   :caption: /etc/netplan/01-netcfg.yaml

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
