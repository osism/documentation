.. _ubuntu-manual-installation-screenshots:

========================================
Ubuntu manual Installation - Screenshots
========================================

* Boot via CD-ROM/ISO Ubuntu and choose ``Install Ubuntu Server``

  .. image:: /images/manual-installation/01-grub.png

* Select language ``English``

  .. image:: /images/manual-installation/02-language.png

* Select your country, e.g. Europe/Germany

  .. image:: /images/manual-installation/03-country.png
  .. image:: /images/manual-installation/04-location.png
  .. image:: /images/manual-installation/05-location.png

* Choose ``en_US.UTF-8`` as locale

  .. image:: /images/manual-installation/06-locales.png

* Do **not** detect Keyboard layout

  .. image:: /images/manual-installation/07-keyboard-detect.png

* Choose Keyboard Country ``English (US)``

  .. image:: /images/manual-installation/08-keyboard-select.png

* Keyboard layout ``English (US)``

  .. image:: /images/manual-installation/09-keyboard-layout.png

* Choose your Hostname, e.g. 60-10, manager, compute, controller, ctrl, com, sto, ...

  .. image:: /images/manual-installation/10-hostname.png

* Full name of User, ``ubuntu``

  .. image:: /images/manual-installation/11-username-full.png

* username ``ubuntu``

  .. image:: /images/manual-installation/12-username.png

* Set password

  .. image:: /images/manual-installation/13-password.png
  .. image:: /images/manual-installation/14-password-reenter.png

* Set Timezone, e.g. ``Europe/Berlin``

  .. image:: /images/manual-installation/15-timezone.png

* Partitioning - Choose the ``Guided - use entire disk and set up LVM`` entry

  .. image:: /images/manual-installation/16-partition.png

* Choose the first disk

  .. image:: /images/manual-installation/17-partition.png

* Write the changes to disk

  .. image:: /images/manual-installation/18-partition.png

* Continue with the suggested value

  .. image:: /images/manual-installation/19-partition.png

* ``Configure the Logical Volume Manager``

  .. image:: /images/manual-installation/20-partition.png

* Write the changes to disk

  .. image:: /images/manual-installation/21-partition.png

* Delete all suggested Logical Volumes

  .. image:: /images/manual-installation/22-partition.png
  .. image:: /images/manual-installation/23-partition.png

* Create LVs like here :ref:`partitioning` with ext4

  .. image:: /images/manual-installation/24-partition.png
  .. image:: /images/manual-installation/25-partition.png
  .. image:: /images/manual-installation/26-partition.png
  .. image:: /images/manual-installation/27-partition.png
  .. image:: /images/manual-installation/28-partition.png
  .. image:: /images/manual-installation/29-partition.png
  .. image:: /images/manual-installation/30-partition.png
  .. image:: /images/manual-installation/31-partition.png
  .. image:: /images/manual-installation/32-partition.png
  .. image:: /images/manual-installation/33-partition.png
  .. image:: /images/manual-installation/34-partition.png

* For ``swap`` LV use ``swap area``

  .. image:: /images/manual-installation/35-partition-swap.png
  .. image:: /images/manual-installation/36-partition-swap.png

* The partitioning should look like this

  .. image:: /images/manual-installation/37-partition.png

* Write the changes to disk

  .. image:: /images/manual-installation/38-partition.png

* Installation will be started

  .. image:: /images/manual-installation/39-installation.png

* Proxy?

  .. image:: /images/manual-installation/40-proxy.png
  .. image:: /images/manual-installation/41-installation.png

* Choose ``No automatic updates``

  .. image:: /images/manual-installation/42-autoupdate.png

* Choose ``OpenSSH server`` to install

  .. image:: /images/manual-installation/43-openssh.png
  .. image:: /images/manual-installation/44-installation.png

* After finished installation, choose ``Continue`` for reboot

  .. image:: /images/manual-installation/45-complete.png

* After reboot the installed Grub looks like this

  .. image:: /images/manual-installation/46-installed-grub.png

* Finaly the login prompt appears

  .. image:: /images/manual-installation/47-installed-prompt.png
