=======
Cobbler
=======

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.cobbler``
   * - **Repository**
     - https://github.com/osism/ansible-cobler
   * - **Documentation**
     - ---

* http://cobbler.github.io

Network
=======

Distributions
=============

* For each distribution, an entry is added to the ``cobbler_distributions`` dictionary in the ``configuration.yml`` file.

  .. code-block:: yaml

     cobbler_distributions:
       [...]
       - name: ubuntu-server-xenial
         arch: x86_64
         url: http://releases.ubuntu.com/16.04/ubuntu-16.04.3-server-amd64.iso

Profiles
========

* Place preseed files in the ``files/cobbler`` directory, e.g. ``files/cobbler/ubuntu-server-xenial-controller.preseed``.
* For each profile, an entry is added to the ``cobbler_profiles`` dictionary in the ``configuration.yml`` file.

  .. code-block:: yaml

     cobbler_profiles:
       [...]
       - name: ubuntu-server-xenial-controller
         file: "{{ configuration_directory }}/environments/infrastructure/files/cobbler/ubuntu-server-xenial-controller.preseed"
         params:
           distro: ubuntu-server-xenial-x86_64

Preseed
-------

* https://wiki.debian.org/DebianInstaller/Preseed
* https://www.debian.org/releases/stable/amd64/apb.html.en
* https://www.debian.org/releases/stretch/example-preseed.txt
* https://wikitech.wikimedia.org/wiki/PartMan
* https://wikitech.wikimedia.org/wiki/PartMan/Auto
* https://wikitech.wikimedia.org/wiki/PartMan/AutoRaid
* https://www.bishnet.net/tim/blog/2015/01/29/understanding-partman-autoexpert_recipe/

Systems
=======

* For each system, an entry is added to the ``cobbler_systems`` dictionary in the ``configuration.yml`` file.

  .. code-block:: yaml

     cobbler_systems:
     [...]
       - name: 20-12
         params:
           power_address: 172.16.20.12
           power_pass: password
           power_type: ipmilan
           power_user: openstack
           profile: ubuntu-server-xenial-controller
           interfaces:
             ip_address-enp5s0f0: 172.16.21.12
             mac_address-enp5s0f0: aa:bb:cc:dd:ee:ff
             management-enp5s0f0: true
           kernel_options:
             "netcfg/choose_interface": enp5s0f0
