=======
Compute
=======

Nested virtualisation
=====================

.. note:: The activation of nested virtualization will be enabled automatically in the future.
          Until then carry out subsequent manual steps.

AMD
---

.. code-block:: shell

   $ echo "options kvm-amd nested=y" | sudo tee /etc/modprobe.d/kvm-nested-virtualization.conf

.. code-block:: shell

   $ cat /sys/module/kvm_amd/parameters/nested
   Y

Intel
-----


.. code-block:: shell

   $ echo "options kvm-intel nested=y" | sudo tee /etc/modprobe.d/kvm-nested-virtualization.conf

.. code-block:: shell

   $ cat /sys/module/kvm_intel/parameters/nested
   Y

References
----------

* https://docs.openstack.org/devstack/latest/guides/devstack-with-nested-kvm.html
