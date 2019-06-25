==========
SuperMicro
==========

.. contents::
   :local:

For the public cloud "Betacloud" we use hardware from SuperMicro. Therefore there is
this chapter with hints about SuperMicro.

Copy & paste in the iKVM remote console
=======================================

MacOS
-----

Bind the following command to a hot key, for example with BetterTouchTool (https://folivora.ai).
Copy the text you want to paste into the clipboard. Then press the hot key in the opened iKVM console.

.. code-block:: console

   osascript -e 'tell application "System Events" to keystroke the clipboard as text'

* https://gist.github.com/ethack/110f7f46272447828352768e6cd1c4cb

Reset IPMI password
===================

.. code-block:: console

   $ apt-get install ipmitool
   $ ipmitool user list
   $ ipmitool user set password 2 ADMIN

Configure and mount Samba share
===============================

Samba service
-------------

Virtual Media
-------------

Application Blocked by Java Security
====================================

In older Supermicro systems, Java is still used for the virtual console.

When calling the virtual console via the Java WS file you get the error ``Application Blocked by Java Security``.

.. image:: /images/supermicro-application-blocked-by-java-security.png

In the Java control panel, an exception can be added to the Exception Site List (under Security) (https://techhelpkb.com/why-do-i-see-application-blocked-by-security-settings/).

Then execute the Java WS file again. There is now another safety instruction, which can easily be confirmed.

.. image:: /images/supermicro-running-this-application-may-be-a-security-risk.png

Use of old Java iKVM Viewer with current JRE version
====================================================

In older Supermicro systems, Java is still used for the virtual console.

If the Java iKVM Viewer does not work correctly this is probably due to disabled SSLv3 support.

SSLv3 can be enabled in the ``java.security`` file.

The file can be found in the ``lib/security`` directory of the active JRE installation. On a MacOS e.g.
``/Library/Java/JavaVirtualMachines/jdk1.8.0_74.jdk/Contents/Home/jre/lib/security``. The version of the
used JRE can be obtained by calling ``java -version``.

.. code-block:: ini

   #jdk.tls.disabledAlgorithms=SSLv3, RC4, MD5withRSA, DH keySize < 768
   jdk.tls.disabledAlgorithms=RC4, MD5withRSA, DH keySize < 768
