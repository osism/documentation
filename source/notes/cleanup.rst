=======
Cleanup
=======

warning: setlocale: LC_ALL: cannot change locale (en_US.UTF-8)
==============================================================

Description
-----------

.. code-block:: console

   -bash: warning: setlocale: LC_ALL: cannot change locale (en_US.UTF-8)

Solution
--------

.. code-block:: console

   $ sudo locale-gen en_US.UTF-8
   $ sudo update-locale LANG=en_US.UTF-8

TMOUT: readonly variable
========================

Description
-----------

.. code-block:: console

   $ ssh dragon@xxx
   ------------------------------------------------------------------------------
   * WARNING                                                                    *
   * You are accessing a secured system and your actions will be logged along   *
   * with identifying information. Disconnect immediately if you are not an     *
   * authorized user of this system.                                            *
   ------------------------------------------------------------------------------
   Last login: Wed May 16 06:15:07 2018 from xxx
   -bash: TMOUT: readonly variable

Solution
--------

Check the ``/etc/profile`` file for a double block. Remove everything from ``# BEGIN MANAGED BY OPENSTACK-ANSIBLE-SECURITY`` to ``# END MANAGED BY OPENSTACK-ANSIBLE-SECURITY``.

.. code-block:: shell

   # BEGIN MANAGED BY OPENSTACK-ANSIBLE-SECURITY
   # Set a 600 second timeout for sessions
   TMOUT=600
   readonly TMOUT
   export TMOUT
   # END MANAGED BY OPENSTACK-ANSIBLE-SECURITY
   # BEGIN MANAGED BY ANSIBLE-HARDENING
   # Set a 3600 second timeout for sessions
   TMOUT=3600
   readonly TMOUT
   export TMOUT
   # END MANAGED BY ANSIBLE-HARDENING


unknown item 'FAIL_DELAY'
=========================

Description
-----------

.. code-block:: console

   $ sudo su -
   configuration error - unknown item 'FAIL_DELAY' (notify administrator)

Solution
--------

Remove the uncommented ``FAIL_DELAY`` line from ``/etc/login.defs``.

OPENSTACK-ANSIBLE-SECURITY block in /etc/ssh/sshd_config
========================================================

Description
-----------

The renaming of the Ansible hardening role results on older environments in a double configuration block in the ``/etc/ssh/sshd_config`` configuration file.

Solution
--------

Remove everything from ``# BEGIN MANAGED BY OPENSTACK-ANSIBLE-SECURITY`` to ``# END MANAGED BY OPENSTACK-ANSIBLE-SECURITY``. Restart the ``ssh`` service with ``systemctl restart ssh``.

.. code-block:: none

   # BEGIN MANAGED BY OPENSTACK-ANSIBLE-SECURITY
   [...]
   # END MANAGED BY OPENSTACK-ANSIBLE-SECURITY
   # BEGIN MANAGED BY ANSIBLE-HARDENING
   [...]
   # END MANAGED BY ANSIBLE-HARDENING

ssh: Too many authentication failures
=====================================

Description
-----------

.. code-block:: console

   $ ssh -i id_rsa.operator dragon@10.11.12.13
      Received disconnect from 10.11.12.13 port 22:2: Too many authentication failures
      Authentication failed.

Solution
--------

Sometimes this is caused by too many files in ``~/.ssh/``. You can use the ``IdentitiesOnly`` option as a workaround.

.. code-block:: console

   $ ssh -o IdentitiesOnly=yes -i id_rsa.operator dragon@10.11.12.13
