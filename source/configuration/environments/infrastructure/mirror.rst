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

.. contents::
   :local:

It is recommended to deploy the mirror services on a dedicated system.

APT repository mirror
=====================

Docker registry mirror
======================

Service configuration
---------------------

If the registry service is started on one of the controller nodes, the registry service port
must be adjusted from ``5000`` to e.g. ``5001``. Otherwise there will be a port conflict with
the OpenStack Keystone service.

.. code-block:: yaml
   :caption: environments/infrastructure/configuration.yml

   registry_port: 5001

By default the registry service listens on the IPv4 address of the management interface.
This can be changed with the ``registry_host`` parameter.

The following entry is stored by default in the configuration repository.

.. code-block:: yaml
   :caption: environments/infrastructure/configuration.yml

   registry_host: "{{ hostvars[inventory_hostname]['ansible_' + management_interface]['ipv4']['address'] }}"

It is also possible to bind the registry service to more than one address port pair.
Additional pairs can be added to the ``registry_ports`` parameter. Below is the default
of the role.

.. code-block:: yaml
   :caption: environments/infrastructure/configuration.yml

   registry_ports:
     - "{{ registry_host }}:{{ registry_port }}:5000"

Mirrored images
---------------

The images to be mirrored are specified in the ``configuration-mirror-images.yml`` file.

To mirror the images, execute ``osism-mirror images`` after deployment.

.. code-block:: yaml
   :caption: environments/infrastructure/configuration-mirror-images.yml

   ---
   ##########################
   # versions

   ceph_version: luminous
   openstack_version: rocky
   repository_version: 2019.4.0

   ceph_manager_version: 2019.4.0
   kolla_manager_version: 2019.4.0
   osism_manager_version: 2019.4.0

   ##########################
   # mirror-images

   docker_registry_external: index.docker.io
   docker_registry_internal: registry.local
   docker_namespace: osism

   remove_local_docker_images: false
