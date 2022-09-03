=========
OpenStack
=========

Show all instances on a specific compute node
=============================================

.. code-block:: console

   openstack --os-cloud admin server list --all-projects --host 54-02

Show all running instances
==========================

.. code-block:: console

   openstack --os-cloud admin server list --all-projects --power-state running

Enable Luks Encryption
======================

Configuration reference: https://docs.openstack.org/cinder/latest/configuration/block-storage/volume-encryption.html

Look into the luks sections in cinder and nova to enable it:

* :ref:`configuration-environment-openstack-cinder`
* :ref:`configuration-environment-openstack-nova`

.. code-block:: console

   openstack --os-cloud admin volume type create \ 
   --encryption-provider luks \
   --encryption-cipher aes-xts-plain64 \
   --encryption-key-size 256 \
   --encryption-control-location front-end LUKS


