======
Ubuntu
======

Hold packages
=============

Manually
--------

To prevent the update of a package, although a newer version is available, the package must be set to hold.

.. code-block:: console

   $ sudo apt-mark hold linux-firmware linux-generic
   linux-firmware set on hold.
   linux-generic set on hold.

   $ sudo apt-mark showhold
   linux-firmware
   linux-generic

Packages on hold will not be updated anymore.

.. code-block:: console

   $ sudo apt-get dist-upgrade
   [...]
   The following packages have been kept back:
     linux-firmware linux-generic linux-headers-generic linux-image-generic
   [...]

To check the changelog of packages on hold, the following call can be used

https://wiki.debianforum.de/Pakete_auf_hold_setzen

.. code-block:: console

   $ dpkg -l | awk '$1=="hi" {printf "%s %s %s\n", $2, $3, $4}' | while read pkg ver arch; do apt-get -qq changelog $pkg | sed "/$pkg ($ver)/q" | pager; done

With ``unhold`` the lock can be removed again.

.. code-block:: console

   $ apt-mark unhold linux-firmware linux-generic
   Canceled hold on linux-firmware.
   Canceled hold on linux-generic.

Automatically
-------------

Create a playbook with the name ``playbook-hold.yml`` in the environment ``generic``. Packages can be defined via the parameter ``packages_hold``.

.. code-block:: yaml

   ---
   - name: Hold packages
     hosts: all
     gather_facts: no

     vars:
       packages_hold:
         - linux-firmware
         - linux-generic

     tasks:
     - name: Hold package
       command: "apt-mark hold {{ item }}"
       register: result
       changed_when: "'was already set on hold' not in result.stdout"
       become: true
       with_items: "{{ packages_hold }}"

The playbook can now be executed with ``osism-run``.

.. code-block:: console

    $ osism-run generic hold -l 10-11.betacloud.xyz
    PLAY [Hold packages] *********************************************

    TASK [Hold package] ***********************************************
    ok: [10-11.betacloud.xyz] => (item=linux-firmware)
    ok: [10-11.betacloud.xyz] => (item=linux-generic)

    PLAY RECAP *********************************************************
    10-11.betacloud.xyz : ok=1    changed=0    unreachable=0    failed=0

To unlock packages again, create an additional playbook ``playbook-unhold.yml`` and use ``unhold`` instead of ``hold``.
