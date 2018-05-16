=======
Cleanup
=======

TMOUT: readonly variable
========================

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

.. code-block:: console

   $ sudo su -
   configuration error - unknown item 'FAIL_DELAY' (notify administrator)

Remove the uncommented ``FAIL_DELAY`` line from ``/etc/login.defs``.
