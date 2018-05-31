======
Common
======

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.common``
   * - **Repository**
     - https://github.com/osism/ansible-common
   * - **Documentation**
     - ---

Microcode installation
======================

The parameter ``install_microcode_package_common`` can be used to install
the packages ``intel-microcode`` and ``amd64-microcode``.

* ``environments/configuration.yml``

  .. code-block:: yaml

     ##########################
     # common

     install_microcode_package_common: yes
