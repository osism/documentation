======
Custom
======

* base directory: ``environments/custom``

The custom environment is used to store any additional playbooks and services.

.. note::

   Where possible, playbooks are integrated into ``osism-ansible``.
   Additional services are implemented in a separate role as needed.

Playbooks
=========

* Playbooks are provided with the prefix ``playbook-`` and the file extension ``.yml``, completely so then ``playbook-NAME.yml``
* Playbooks can be executed via ``osism-run custom NAME``

Here is an example playbook ``playbook-cronjobs.yml`` that creates a cronjob for collecting facts on the manager node on a regular basis.

It is executed with ``osism-run custom cronjobs``.

.. code-block:: yaml

   ---
   - name: Custom playbook cronjobs
     hosts: manager
     gather_facts: false

     tasks:
     - name: Run helper scripts non-interactive
       cron:
         name: INTERACTIVE
         env: yes
         value: "false"
         cron_file: osism
         user: "{{ operator_user }}"
       become: true

     - name: Gather facts
       cron:
         name: "gather facts"
         minute: "15"
         hour: "*/6"
         job: /usr/local/bin/osism-run-without-secrets generic facts
         cron_file: osism
         user: "{{ operator_user }}"
       become: true

Services
========

* Services are provided with the prefix ``playbook-service-`` and the file extension ``.yml``, completely so then ``playbook-service-NAME.yml``
* Playbooks can be executed via ``osism-run custom service-NAME``
* Configuration template files and the ``docker-compose.yml`` file can be placed in the directory ``templates/NAME``.
* Define required configuration parametes in the ``configuration.yml`` file.
* Define required image parameters in the ``images.yml`` file.
* Define required secret parameters in the ``secrets.yml`` file.

Netbox
------

Service ``netbox`` that starts a Netbox service for IPA & inventory management on the manager node.

It is executed with ``osism-run custom service-netbox``.

* ``playbook-service-netbox.yml``

.. code-block:: yaml

   ---
   - name: Custom service netbox
     hosts: manager
     gather_facts: no

     tasks:
     - name: Create required directories
       file:
         path: "{{ item }}"
         state: directory
         owner: "{{ operator_user }}"
         group: "{{ operator_group }}"
         mode: 0755
       become: true
       with_items:
         - "{{ custom_netbox_docker_compose_directory }}"
         - "{{ custom_netbox_configuration_directory }}"

     - name: Copy configuration files
       template:
         src: "{{ item.src }}"
         dest: "{{ item.dest }}"
         mode: 0644
         owner: "{{ operator_user }}"
         group: "{{ operator_group }}"
       with_items:
         - src: netbox/configuration.py.j2
           dest: "{{ custom_netbox_configuration_directory }}/configuration.py"

     - name: Copy docker-compose.yml file
       template:
         src: netbox/docker-compose.yml.j2
         dest: "{{ custom_netbox_docker_compose_directory }}/docker-compose.yml"
         owner: "{{ operator_user }}"
         group: "{{ operator_group }}"
         mode: 0640

     - name: Pull images
       command: "docker-compose -f {{ custom_netbox_docker_compose_directory }}/docker-compose.yml pull"
       register: result
       changed_when: ('Downloaded' in result.stdout)

     - name: Run service
       command: "docker-compose -f {{ custom_netbox_docker_compose_directory }}/docker-compose.yml up -d --remove-orphans --no-build"
       register: result
       changed_when: ('Creating' in result.stdout or 'Recreating' in result.stdout)

* Create ``templates/netbox`` directory

* ``templates/netbox/docker-compose.yml.j2``

.. code-block:: yaml

   ---
   version: '3'
   services:
     netbox:
       image: "{{ custom_netbox_netbox_image }}"
       depends_on:
         - postgres
       environment:
         SUPERUSER_NAME: dragon
         SUPERUSER_EMAIL: operations@betacloud.io
         SUPERUSER_PASSWORD: {{ custom_netbox_superuser_password }}
       volumes:
         - "./configuration/configuration.py:/configuration.py:ro"
         - config:/etc/netbox-nginx
         - static:/opt/netbox/netbox/static
     nginx:
       image: "{{ custom_netbox_nginx_image }}"
       command: nginx -g 'daemon off;' -c /etc/netbox-nginx/nginx.conf
       depends_on:
         - netbox
       ports:
         - "{{ custom_netbox_host }}:{{ custom_netbox_port }}:80"
       volumes:
         - config:/etc/netbox-nginx
         - static:/opt/netbox/netbox/static
     postgres:
       image: "{{ custom_netbox_postgres_image }}"
       env_file:
         - configuration/postgres.env
       volumes:
         - data:/var/lib/postgresql/data
   volumes:
     config:
       driver: local
     data:
       driver: local
     static:
       driver: local

* ``templates/netbox/configuration.py.j2``

.. code-block:: python

   ALLOWED_HOSTS = ['*']

   DATABASE = {
       'NAME': 'netbox',
       'USER': 'netbox',
       'PASSWORD': '{{ custom_netbox_db_password }}',
       'HOST': 'postgres',
       'PORT': '',
   }

   SECRET_KEY = '{{ custom_netbox_secret_key }}'

* Add to ``images.yml``

.. code-block:: yaml

   ##########################
   # custom service: netbox

   custom_netbox_netbox_tag: v2.3.3
   custom_netbox_netbox_image: "betacloud/netbox:{{ custom_netbox_netbox_tag }}"

   custom_netbox_nginx_tag: 1.13
   custom_netbox_nginx_image: "nginx:{{ custom_netbox_nginx_tag }}"

   custom_netbox_postgres_tag: 9.6
   custom_netbox_postgres_image: "postgres:{{ custom_netbox_postgres_tag }}"

* Add to ``secrets.yml``

.. code-block:: yaml

   ##########################
   # custom service: netbox

   custom_netbox_db_password: password
   custom_netbox_secret_key: password
   custom_netbox_superuser_password: password

* Add to ``configuration.yml``

.. code-block:: yaml

   ##########################
   # custom service: netbox

   custom_netbox_host: "{{ hostvars[inventory_hostname]['ansible_' + management_interface]['ipv4']['address'] }}"
   custom_netbox_port: 5555

   custom_netbox_configuration_directory: /opt/custom-netbox/configuration
   custom_netbox_docker_compose_directory: /opt/custom-netbox

Grafana
-------

Service ``grafana`` that starts a Grafana service on the manager node.

It is executed with ``osism-run custom service-grafana``.

* Create ``templates/grafana`` directory

.. note::

   The use of a configuration file is optional.

   If necessary, the file ``templates/grafana/grafana.ini.j2`` is created with the contents of
   https://github.com/grafana/grafana/blob/master/conf/sample.ini.

   Subsequent commented blocks are then commented out accordingly.

* ``templates/grafana/docker-compose.yml.j2``

.. code-block:: yaml

   ---
   version: '2'
   services:
     grafana:
       image: "{{ custom_grafana_image }}"
       ports:
         - "{{ custom_grafana_host }}:{{ custom_grafana_port }}:3000"
       volumes:
         - data:/var/lib/grafana
         # - "./configuration/grafana.ini:/etc/grafana/grafana.ini:ro"
   volumes:
     data:
       driver: local

* ``playbook-service-grafana.yml``

.. code-block:: yaml

   ---
   - name: Custom service grafana
     hosts: manager
     gather_facts: no

     tasks:
     - name: Create required directories
       file:
         path: "{{ item }}"
         state: directory
         owner: "{{ operator_user }}"
         group: "{{ operator_group }}"
         mode: 0755
       become: true
       with_items:
         - "{{ custom_grafana_docker_compose_directory }}"
         - "{{ custom_grafana_configuration_directory }}"

     # - name: Copy configuration files
     #   template:
     #     src: "{{ item.src }}"
     #     dest: "{{ item.dest }}"
     #     mode: 0644
     #     owner: "{{ operator_user }}"
     #     group: "{{ operator_group }}"
     #   with_items:
     #     - src: grafana/grafana.ini.j2
     #       dest: "{{ custom_grafana_configuration_directory }}/grafana.ini"

     - name: Copy docker-compose.yml file
       template:
         src: grafana/docker-compose.yml.j2
         dest: "{{ custom_grafana_docker_compose_directory }}/docker-compose.yml"
         owner: "{{ operator_user }}"
         group: "{{ operator_group }}"
         mode: 0640

     - name: Pull images
       command: "docker-compose -f {{ custom_grafana_docker_compose_directory }}/docker-compose.yml pull"
       register: result
       changed_when: ('Downloaded' in result.stdout)

     - name: Run service
       command: "docker-compose -f {{ custom_grafana_docker_compose_directory }}/docker-compose.yml up -d --remove-orphans --no-build"
       register: result
       changed_when: ('Creating' in result.stdout or 'Recreating' in result.stdout)

* Add to ``images.yml``

.. code-block:: yaml

   ##########################
   # grafana

   custom_grafana_tag: 5.2.4
   custom_grafana_image: "{{ docker_registry }}/grafana/grafana:{{ custom_grafana_tag }}"

* Add to ``secrets.yml``

.. code-block:: yaml

   ##########################
   # grafana

   custom_grafana_admin_password: password

* Add to ``configuration.yml``

.. code-block:: yaml

   ##########################
   # grafana

   custom_grafana_host: "{{ hostvars[inventory_hostname]['ansible_' + network_interface]['ipv4']['address'] }}"
   custom_grafana_port: 3000

   custom_grafana_docker_compose_directory: /opt/custom-grafana
   custom_grafana_configuration_directory: /opt/custom-grafana/configuration
