======
Mirror
======

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.mirror``
   * - **Repository**
     - https://github.com/osism/ansible-mirror
   * - **Documentation**
     - ---

APT repository
==============

Docker registry
===============

If the registry is started on one of the controller nodes, the registry port must
be adjusted from 5000 to 5001. Otherwise there will be a conflict with the Keystone
service.

.. code-block:: yaml
   :caption: environments/infrastructure/configuration.yml

   registry_port: 5001

Files
=====
