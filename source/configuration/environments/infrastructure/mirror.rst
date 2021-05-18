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
   :depth: 2

It is recommended to deploy the mirror services on a dedicated system.

APT repository mirror
=====================

Service configuration
---------------------

For the activation of the deployment of the aptly service, the parameter ``configure_aptly``
is set to ``yes`` in ``environments/infrastructure/configuration.yml``.

.. code-block:: yaml

   configure_aptly: yes

GPG details are set via the ``aptly_configuration`` parameter in ``environments/infrastructure/configuration.yml``.

.. code-block:: yaml

   aptly_configuration:
     full_name: Betacloud Solutions GmbH
     email_address: info@betacloud-solutions.de
     gpg_password: "{{ aptly_gpg_password }}"

The used password ``aptly_gpg_password`` is set in ``environments/infrastructure/secrets.yml`` file.

.. code-block:: yaml

   aptly_gpg_password: password

By default the aptly service listens on the IPv4 address of the management interface.
This can be changed with the ``aptly_nginx_host`` parameter.

The following entry is stored by default in the configuration repository in ``environments/infrastructure/configuration.yml``.

.. code-block:: yaml

   aptly_nginx_host: "{{ hostvars[inventory_hostname]['ansible_' + management_interface]['ipv4']['address'] }}"

It is also possible to bind the aptly service to more than one address port pair.
Additional pairs can be added to the ``aptly_nginx_ports`` parameter. Below is the default
of the role in file ``environments/infrastructure/configuration.yml``.

.. code-block:: yaml

   aptly_nginx_ports:
     - "{{ aptly_nginx_host }}:{{ aptly_nginx_port }}:80"

Mirrored repositories
---------------------

The repositories to be mirrored are specified in the ``configuration.yml`` file in
the ``infrastructure`` environment.

To mirror the repositories, execute ``osism-mirror packages`` after deployment, configured in ``environments/infrastructure/configuration.yml``.

.. code-block:: yaml

   aptly_repository_keys:
     - https://download.docker.com/linux/ubuntu/gpg

   aptly_repositories:
     - name: "{{ ansible_distribution_release }}-docker"
       architecture: amd64
       distribution: "{{ ansible_distribution_release }}"
       repository: "https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable"
     - name: "{{ ansible_distribution_release }}"
       architecture: amd64
       distribution: "{{ ansible_distribution_release }}"
       repository: "http://de.archive.ubuntu.com/ubuntu/ {{ ansible_distribution_release }} main restricted universe multiverse"
     - name: "{{ ansible_distribution_release }}-backports"
       architecture: amd64
       distribution: "{{ ansible_distribution_release }}"
       repository: "http://de.archive.ubuntu.com/ubuntu/ {{ ansible_distribution_release }}-backports main restricted universe multiverse"
     - name: "{{ ansible_distribution_release }}-security"
       architecture: amd64
       distribution: "{{ ansible_distribution_release }}"
       repository: "http://de.archive.ubuntu.com/ubuntu/ {{ ansible_distribution_release }}-security main restricted universe multiverse"
     - name: "{{ ansible_distribution_release }}-updates"
       architecture: amd64
       distribution: "{{ ansible_distribution_release }}"
       repository: "http://de.archive.ubuntu.com/ubuntu/ {{ ansible_distribution_release }}-updates main restricted universe multiverse"

Docker registry mirror
======================

Service configuration
---------------------

For the activation of the deployment of the registry service, the parameter ``configure_registry``
is set to ``yes`` in ``environments/infrastructure/configuration.yml``.

.. code-block:: yaml

   configure_registry: yes

If the registry service is started on one of the controller nodes, the registry service port
must be adjusted from ``5000`` to e.g. ``5001``. Otherwise there will be a port conflict with
the OpenStack Keystone service. Configure  in ``environments/infrastructure/configuration.yml``

.. code-block:: yaml

   registry_port: 5001

By default the registry service listens on the IPv4 address of the management interface.
This can be changed with the ``registry_host`` parameter.

The following entry is stored by default in the configuration repository in ``environments/infrastructure/configuration.yml``.

.. code-block:: yaml

   registry_host: "{{ hostvars[inventory_hostname]['ansible_' + management_interface]['ipv4']['address'] }}"

It is also possible to bind the registry service to more than one address port pair.
Additional pairs can be added to the ``registry_ports`` parameter. Below is the default
of the role in ``environments/infrastructure/configuration.yml``.

.. code-block:: yaml

   registry_ports:
     - "{{ registry_host }}:{{ registry_port }}:5000"

Mirrored images
---------------

The images to be mirrored are specified in the ``configuration-mirror-images.yml`` file.

To mirror the images, execute ``osism-mirror images`` after deployment, configured in ``environments/infrastructure/configuration-mirror-images.yml``.

.. code-block:: yaml

   ---
   ##########################
   # versions

   ceph_version: nautilus
   openstack_version: train
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
