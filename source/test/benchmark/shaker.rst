======
Shaker
======

.. contents::
   :local:

Shaker is a distributed data-plane testing tool built for OpenStack.

* https://github.com/openstack/shaker

Import base image
=================

Shaker needs a base image. The creation of the base image is documented under http://pyshaker.readthedocs.io/en/latest/installation.html#manual-build-with-disk-image-builder.

We offer an unsupported base image under http://share.osism.io/images/shaker/. The import can be executed via the manager node.

.. code-block:: console

   $ curl -s -o /opt/configuration/environments/openstack/shaker.raw http://share.osism.io/images/shaker/shaker-20180109.raw
   $ openstack --os-cloud service image create --min-disk 3 --min-ram 512 --file /configuration/shaker.raw Shaker
   $ rm /opt/configuration/environments/openstack/shaker.raw

.. note::

   It may be a good idea not to add the image publicly and share it only with individual projects.
