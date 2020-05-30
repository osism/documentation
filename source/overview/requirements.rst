============
Requirements
============

Operating system
================

Deployment is supported on Ubuntu 16.04 and 18.04. Support for Ubuntu 20.04 is in preparation.

The manager node must be at least an Ubuntu 18.04 as of the 2020.2 release. Managers with
Ubuntu 16.04 are no longer supported.

The use of Ubuntu 16.04 is no longer recommended and will not be supported in the future

Other distributions are currently not supported.

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
