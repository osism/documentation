====
Nova
====

Virtual GPUs
============

* https://docs.openstack.org/nova/latest/admin/virtual-gpu.html

NVIDIA
------

* https://docs.nvidia.com/grid/latest/grid-vgpu-release-notes-generic-linux-kvm/index.html

* identify the availalbe GPUs

.. code-block:: console

   $ lspci | grep NVIDI
   02:00.0 3D controller: NVIDIA Corporation Device 1b38 (rev a1)
   82:00.0 3D controller: NVIDIA Corporation Device 1b38 (rev a1)
   85:00.0 3D controller: NVIDIA Corporation Device 1b38 (rev a1)
   86:00.0 3D controller: NVIDIA Corporation Device 1b38 (rev a1)

   $ lshw -numeric -C display
   WARNING: you should run this program as super-user.
     *-display
          description: 3D controller
          product: NVIDIA Corporation [10DE:1B38]
          vendor: NVIDIA Corporation [10DE]
   [...]

* resolv the PCI device ID e.g. with https://devicehunt.com

.. image:: /images/devicehunt-nvidia-p40.png

* check https://docs.nvidia.com/grid/gpus-supported-by-vgpu.html

PCI passthrough
===============

* https://docs.openstack.org/nova/latest/admin/pci-passthrough.html
* https://docs.openstack.org/nova/latest/configuration/config.html#pci

* enable IOMMU support (further details at https://www.linux-kvm.org/page/How_to_assign_devices_with_VT-d_in_KVM)

  .. code-block:: console

     $ dmesg | grep IOMMU
     [    0.207515] DMAR-IR: IOAPIC id 12 under DRHD base  0xc5ffc000 IOMMU 6
     [    0.207516] DMAR-IR: IOAPIC id 11 under DRHD base  0xb87fc000 IOMMU 5
     [    0.207518] DMAR-IR: IOAPIC id 10 under DRHD base  0xaaffc000 IOMMU 4
     [    0.207519] DMAR-IR: IOAPIC id 18 under DRHD base  0xfbffc000 IOMMU 3
     [    0.207520] DMAR-IR: IOAPIC id 17 under DRHD base  0xee7fc000 IOMMU 2
     [    0.207522] DMAR-IR: IOAPIC id 16 under DRHD base  0xe0ffc000 IOMMU 1
     [    0.207523] DMAR-IR: IOAPIC id 15 under DRHD base  0xd37fc000 IOMMU 0
     [    0.207525] DMAR-IR: IOAPIC id 8 under DRHD base  0x9d7fc000 IOMMU 7
     [    0.207526] DMAR-IR: IOAPIC id 9 under DRHD base  0x9d7fc000 IOMMU 7
     $ docker exec -it nova_libvirt virt-host-validate
     [...]
     QEMU: Checking if IOMMU is enabled by kernel                               : PASS
     [...]

* check if the nouveau kernel module is loaded

  .. code-block:: console

     $ lsmod | grep nouveau
     nouveau              1503232  0
     mxm_wmi                16384  1 nouveau
     video                  40960  1 nouveau
     ttm                    98304  2 ast,nouveau
     drm_kms_helper        155648  2 ast,nouveau
     drm                   364544  6 ast,ttm,drm_kms_helper,nouveau
     i2c_algo_bit           16384  3 ast,igb,nouveau
     wmi                    20480  2 mxm_wmi,nouveau

* disable nouveau in ``/etc/modprobe.d/blacklist-nvidia-nouveau.conf``

  .. code-block:: console
    
     blacklist nouveau
     options nouveau modeset=0

* rebuild the initramfs and rebbot

  .. code-block:: console

     $ sudo update-initramfs -u
     $ sudo reboot

* enable PCI passthrough module in ``/etc/modprobe.d/vfio.conf``

  .. code-block:: console
 
     options vfio-pci ids=10de:1b38
     options vfio-pci disable_vga=1

* enable the ``PciPassthroughFilter`` scheduler in ``environments/kolla/files/overlays/nova/nova-scheduler.conf``

  .. code-block:: ini

     [filter_scheduler]
     enabled_filters = ..., PciPassthroughFilter

* get vendor and products IDs

  .. code-block:: console

     $ lspci -nn

* specify PCI aliases for the devices in ``environments/kolla/files/overlays/nova/nova-api.conf`` and ``environments/kolla/files/overlays/nova/nova-compute.conf``

  .. code-block:: ini

     [pci]
     alias={"vendor_id": "8086", "product_id":"10fb", "device_type":"type-PCI", "name":"testing"}

* whitelist PCI devices in ``environments/kolla/files/overlays/nova/nova-compute.conf``

  .. code-block:: ini

     [pci]
     passthrough_whitelist = { "address": "0000:41:00.0" }

  .. code-block:: ini

     [pci]
     passthrough_whitelist = { "vendor_id": "8086", "product_id": "10fb" }

* set the ``pci_passthrough:alias"`` property on a flavor

  .. code-block:: console

     $ openstack --os-cloud service flavor set 1C-1GB-10GB --property "pci_passthrough:alias"="testing:1"
