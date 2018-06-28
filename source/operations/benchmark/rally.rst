=====
Rally
=====

Rally is a Benchmark-as-a-Service project for OpenStack.

* https://github.com/openstack/rally

Configuration
=============

Set ``configure_rally: yes`` in ``environments/infrastructure/configuration.yml`` and deploy Rally with
``osism-infrastructure helper --tags rally``.

Initialisation
==============

.. note::

   The following commands are to be executed on the manager node.

Database
--------

It is required to manually initialise the Rally database.

Run the ``rally db create`` command to create and bootstrap the database.

.. code-block:: console

   $ rally db create
   Creating database: mysql+pymysql://rally:password@database/rally
   Database created successfully

After an upgrade run ``rally db upgrade``.

.. code-block:: console

   $ rally db upgrade
   Upgrading database: mysql+pymysql://rally:password@database/rally
   Database is already up to date

.. note::

   The used database password can be set via the paramter ``rally_database_password`` in the
   ``environments/secrets.yml`` or ``environments/infrastructure/secrets.yml`` file.

Deployment
----------

Create the ``/opt/rally/tests/rally.json`` file with the required cloud details.

.. code-block:: json

   {
       "openstack": {
           "auth_url": "https://api-1.betacloud.io:5000/v3",
           "region_name": "betacloud-1",
           "endpoint_type": "public",
           "admin": {
               "username": "admin",
               "user_domain_name": "Default",
               "password": "password",
               "project_name": "admin",
               "project_domain_name": "Default"
           },
           "https_insecure": true
       }
   }

.. note::

   Use the public endpoint.

Create a deployment with ``rally deployment create``.

.. code-block:: console

   $ rally deployment create --name osism --filename /tests/rally.json
   2017-11-08 15:40:33.789 27 INFO rally.deployment.engines.existing [-] Save deployment 'osism' (uuid=87dd7509-72ad-45f1-86b6-1ea7018ae6bc) with 'openstack' platform.
   +--------------------------------------+---------------------+-------+------------------+--------+
   | uuid                                 | created_at          | name  | status           | active |
   +--------------------------------------+---------------------+-------+------------------+--------+
   | 87dd7509-72ad-45f1-86b6-1ea7018ae6bc | 2017-11-08T15:40:33 | osism | deploy->finished |        |
   +--------------------------------------+---------------------+-------+------------------+--------+
   Using deployment: 87dd7509-72ad-45f1-86b6-1ea7018ae6bc
   ~/.rally/openrc was updated

   HINTS:

   * To use standard OpenStack clients, set up your env by running:
           source ~/.rally/openrc
     OpenStack clients are now configured, e.g run:
           openstack image list

Run ``rally deployment check`` to check the deployment.

.. code-block:: console

   $ rally deployment check
   --------------------------------------------------------------------------------
   Platform openstack:
   --------------------------------------------------------------------------------

   Available services:
   +-------------+----------------+-----------+
   | Service     | Service Type   | Status    |
   +-------------+----------------+-----------+
   | __unknown__ | compute_legacy | Available |
   | __unknown__ | event          | Available |
   | __unknown__ | placement      | Available |
   | __unknown__ | search         | Available |
   | __unknown__ | volumev2       | Available |
   | __unknown__ | volumev3       | Available |
   | ceilometer  | metering       | Available |
   | cinder      | volume         | Available |
   | cloud       | cloudformation | Available |
   | glance      | image          | Available |
   | gnocchi     | metric         | Available |
   | heat        | orchestration  | Available |
   | keystone    | identity       | Available |
   | neutron     | network        | Available |
   | nova        | compute        | Available |
   +-------------+----------------+-----------+

.. note::

   The ``__unknown__`` services are not an error. More details on this on https://bugs.launchpad.net/rally/+bug/1618121,
   in the output of the command ``rally plugin show api_versions``, as well as in the source code.

   .. code::

      __unknown__ service name means that Keystone service
      catalog doesn't return name for this service and Rally can
      not identify service by its type. BUT you still can use
      such services with api_versions context, specifying type of
      service (execute `rally plugin show api_versions` for more
      details)

Run a custom test
=================

.. note::

   Prefabricated tests can be found at the Rally repository: https://github.com/openstack/rally/tree/master/samples/tasks.

Create a test file (``/opt/rally/tests/create-user.yaml``) with the following content.

.. code-block:: yaml

   ---
   KeystoneBasic.create_user:
     -
       args: {}
       runner:
         type: "constant"
         times: 100
         concurrency: 10
       sla:
         failure_rate:
           max: 0

Run the test with ``rally task start /tests/create-user.yaml``.

.. code-block:: console

   $ rally task start /tests/create-user.yaml
   [...]

   --------------------------------------------------------------------------------
   Task e5916fb4-04d6-4ffc-8a63-edab74514976 has 0 error(s)
   --------------------------------------------------------------------------------

   +----------------------------------------------------------------------------------------------------------------------------+
   |                                                    Response Times (sec)                                                    |
   +-------------------------+-----------+--------------+--------------+--------------+-----------+-----------+---------+-------+
   | Action                  | Min (sec) | Median (sec) | 90%ile (sec) | 95%ile (sec) | Max (sec) | Avg (sec) | Success | Count |
   +-------------------------+-----------+--------------+--------------+--------------+-----------+-----------+---------+-------+
   | keystone_v3.create_user | 0.176     | 0.574        | 1.14         | 1.284        | 2.088     | 0.652     | 100.0%  | 100   |
   | total                   | 0.298     | 0.67         | 1.206        | 1.366        | 2.175     | 0.731     | 100.0%  | 100   |
   |  -> duration            | 0.298     | 0.67         | 1.206        | 1.366        | 2.175     | 0.731     | 100.0%  | 100   |
   |  -> idle_duration       | 0.0       | 0.0          | 0.0          | 0.0          | 0.0       | 0.0       | 100.0%  | 100   |
   +-------------------------+-----------+--------------+--------------+--------------+-----------+-----------+---------+-------+

   Load duration: 13.2027
   Full duration: 59.4453

   HINTS:
   * To plot HTML graphics with this data, run:
           rally task report e5916fb4-04d6-4ffc-8a63-edab74514976 --out output.html

   * To generate a JUnit report, run:
           rally task export e5916fb4-04d6-4ffc-8a63-edab74514976 --type junit --to output.xml

   * To get raw JSON output of task results, run:
           rally task report e5916fb4-04d6-4ffc-8a63-edab74514976 --json --out output.json

Render the results file with ``rally task report e5916fb4-04d6-4ffc-8a63-edab74514976 --out /results/e5916fb4-04d6-4ffc-8a63-edab74514976.html``.

.. code-block:: console

   $ rally task report e5916fb4-04d6-4ffc-8a63-edab74514976 --out /results/e5916fb4-04d6-4ffc-8a63-edab74514976.html
   2017-11-08 16:24:52.855 27 INFO rally.api [-] Building 'html' report for the following task(s): 'e5916fb4-04d6-4ffc-8a63-edab74514976'.
   2017-11-08 16:24:52.927 27 INFO rally.api [-] The report has been successfully built.

A Nginx server serving the ``results`` directory is running on the manager node on port ``8090``. The address can be configured with the parameter ``rally_nginx_host``.

.. image:: /images/rally-result-html.png

Run "OpenStack Certification Task"
==================================

The "OpenStack Certification Task" is a collection of configurable tests for the main components
(Cinder, Glance, Keystone, Neutron, Nova) of OpenStack. The necessary files are located in the
Rally Repository (https://github.com/openstack/rally/tree/master/tasks/openstack).

We offer a collection of tests based on it, Available in the repository https://github.com/osism/test/tree/master/openstack/rally.
These tests are used below.

.. note::

   Yes, that is not yet automated and will be improved in the future.

.. code-block:: console

   $ wget https://github.com/osism/test/archive/master.zip
   $ unzip master.zip 'test-master/openstack/rally/*'
   $ rsync -avz test-master/openstack/rally/macro /opt/rally/tests
   $ rsync -avz test-master/openstack/rally/scenario /opt/rally/tests
   $ rsync -avz test-master/openstack/rally/task.yml /opt/rally/tests

.. code-block:: console

   $ [[ ! -e /opt/rally/tests/task/task-arguments.yml ]] && cp test-master/openstack/rally/task-arguments.yml /opt/rally/tests

.. code-block:: console

   $ rm -rf master.zip test-master

File ``task-arguments.yml`` contains all task options:

+------------------------+----------------------------------------------------+
| Name                   | Description                                        |
+========================+====================================================+
| service_list           | List of services which should be tested            |
+------------------------+----------------------------------------------------+
| smoke                  | Dry run without load from 1 user                   |
+------------------------+----------------------------------------------------+
| use_existing_users     | In case of testing cloud with r/o Keystone e.g. AD |
+------------------------+----------------------------------------------------+
| image_name             | Images name that exist in cloud                    |
+------------------------+----------------------------------------------------+
| flavor_name            | Flavor name that exist in cloud                    |
+------------------------+----------------------------------------------------+
| glance_image_location  | URL of image that is used to test Glance upload    |
+------------------------+----------------------------------------------------+
| users_amount           | Expected amount of users                           |
+------------------------+----------------------------------------------------+
| tenants_amount         | Expected amount of tenants                         |
+------------------------+----------------------------------------------------+
| controllers_amount     | Amount of OpenStack API nodes (controllers)        |
+------------------------+----------------------------------------------------+

All options have default values, hoverer user should change them to reflect
configuration and size of tested environment.

.. code-block:: yaml

   ---
   service_list:
     - authentication
     - quota
     - nova
     - neutron
     - keystone
     - cinder
     - glance
   use_existing_users: false
   image_name: ""^(Cirros|cirros).*$""
   flavor_name: "1C-1GB-10GB"
   glance_image_location: "http://share.osism.io/images/cirros/cirros-0.4.0-x86_64-disk.img"
   smoke: true
   users_amount: 1
   tenants_amount: 1
   controllers_amount: 1
   compute_amount: 1
   storage_amount: 1
   network_amount: 1

.. code-block:: console

   $ rally task validate /tests/task.yml --task-args-file /tests/task-arguments.yml
   [...]
   Task syntax is correct :)
   Starting:  Task validation.
   Starting:  Task validation of syntax.
   Completed: Task validation of syntax.
   Starting:  Task validation of required platforms.
   Completed: Task validation of required platforms.
   Starting:  Task validation of semantic.
   Context users@openstack setup()  finished in 0.52 sec
   Context users@openstack cleanup() started
   Context users@openstack cleanup() finished in 0.98 sec
   Completed: Task validation of semantic.
   Completed: Task validation.
   Input Task is valid :)

.. note::

   Removed from the output: ``2018-01-16 20:55:24.621 544 INFO rally.task.engine [-] Task da7b502d-a8ed-4d59-91fd-83043ddd6aaf | ``

.. code-block:: console

   $ rally task start /tests/task.yml --task-args-file /tests/task-arguments.yml
