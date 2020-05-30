============
Requirements
============

Deployment
==========

If the deployment is carried out or supervised by us, direct SSH access to the system
acting as manager is required.

Optimally, a VPN is provided via which all relevant nodes including the remote consoles
can be accessed.

Services & Access
=================

The nodes need access to some external services.

All nodes
---------

* DNS and NTP servers
* Docker Hub / Quay.io
* Official Ubuntu mirrors

.. note::

   * Mirrors for Docker and Ubuntu can be provided within the environment. Then access to
     Docker Hub / Quay.io and Ubuntu mirrors is only required from the manager.

   * If no direct access to external services is possible, the use of an HTTP proxy is
     possible.

Manager node
------------

* GitHub or an internal Git repository server (e.g. Gitlab)
* PyPI

Hardware
========
