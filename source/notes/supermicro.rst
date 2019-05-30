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

Configure and mount Samba share
===============================

Samba service
-------------

Virtual Media
-------------
