====
NBDE
====

Network Bound Disk Encryption.

.. image:: /images/nbde/tang.png


in "Linux Disk Encryption Security" (LUKS) are more then 8 keyslots which can use with passwords, keys or can use it with Clevis and tang

Clevis is a playable client-side unlock framework, which can work with tpm tang or even in combination with  Shamir's Secret Sharing. Clevis work with jose jwe library

Tang is the Server part which advice public a key, hold private key about this advisement, the Communication is very similar to ssh key, it  is base to jose library and handle this with Jason Web Encryption.

the boot procedure looks as follow

.. image:: /images/nbde/clevis_boot.png

in detail clevis has to installed in initramfs to open a network connections to a tang server
and validate deposit keychain in luks keyslot to open the luks encrypted disks.

Luks should prevent to expose secrets or credentials. Maybe in the cases if disks are stolen from a Cloud Service Provider or in support cases if disks send back to the vendor. Clevis Framework support to deploy setups automatically without entering luks passphrases from a operator.

 

tang
====

.. warning::

   When upgrading, the TANG service is restarted. As a result, it comes of the Systems during reboot could wait until tang service is present in cause of NDBE.

* ``environments/manager/configuration.yml``

.. code-block:: yaml
   
   tang_enable: true

.. note::

   It is recommended to update the tang services one by one.

.. code-block:: console

   $ osism apply tang


clevis
======

* ``environments/manager/configuration.yml``

.. code-block:: yaml
   
   clevis_enable: true

.. note::

   It is recommended to update the tang services one by one.

.. code-block:: console

   $ osism apply clevis



* ``environments/configuration.yml``



Build an encrypted image
========================

.. warning::

   As a requirement it is needed a KVM/qemu setup to build this.
   
   https://github.com/osism/openstack-ironic-images/pull/39/files

   The prepared preseed file can find here: encrypt_preseed.cfg.template

   Please don't use documented cryptphase password !
   And please replace https://github.com/<some-operator-rsa>.keys
   with a valid rsa key.

   

   Create qcow2 a image:

.. code-block:: console

   $ virt-install --virt-type kvm  \
      --name focal-build \ 
      --ram 1024 \
      --location=http://archive.ubuntu.com/ubuntu/dists/focal/main/installer-amd64 \
      --initrd-inject http/encrypt_preseed.cfg   \
      --disk /var/lib/libvirt/images/focale.qcow2,bus=virtio,size=10,format=qcow2 \
      --network network=default   \
      --graphics vnc,listen=0.0.0.0 \
      --noautoconsole   \
      --os-type=linux \
      --os-variant=ubuntu20.04

   Remove crendentials from qcow2 a image:

.. code-block:: console
    
    $ virt-sysprep -d focale.qcow2    --keys-from-stdin

    
    Upload encrypted OpenStack image:


.. code-block:: console

   $ openstack --os-cloud betacloud image create \
     --container-format bare  \  
     --disk-format qcow2 \
     --property architecture='x86_64' \
     --property hw_disk_bus='scsi' \
     --property hw_rng_model='virtio' \
     --property hw_scsi_model='virtio-scsi' \
     --property hypervisor_type='kvm' \
     --shared  \
     --file focale.qcow2 \
     ubuntu-encrypt-base-image-20.04


