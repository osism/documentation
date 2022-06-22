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