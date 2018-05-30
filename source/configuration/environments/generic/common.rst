======
Common
======

* role: ``osism.common`` (https://github.com/osism/ansible-common)

Microcode installation
======================

The parameter ``install_microcode_package_common`` can be used to install
the packages ``intel-microcode`` and ``amd64-microcode``.

* ``environments/configuration.yml``

  .. code-block:: yaml

     ##########################
     # common

     install_microcode_package_common: yes
