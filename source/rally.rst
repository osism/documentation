=====
Rally
=====

Configuration
=============

Set ``configure_rally: yes`` in ``environments/infrastructure/configuration.yml`` and deploy Rally with
``osism-infrastructure helper --tags rally``.

Initialisation
==============

At the moment it is required to manually initialise the Rally database. On the manager node run the
``rally db create`` command to bootstrap the database. After an upgrade run ``rally db upgrade``.

.. code-block:: console

   $ rally db create

Create the ``/opt/rally/tests/rally.json`` file with the required cloud details.

.. code-block:: json

   {
       "openstack": {
           "auth_url": "http://192.168.90.200:5000/v3",
           "region_name": "osism",
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

Create a Rally deployment with ``rally deployment create``.

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
   | __unknown__ | placement      | Available |
   | __unknown__ | volumev2       | Available |
   | __unknown__ | volumev3       | Available |
   | cinder      | volume         | Available |
   | cloud       | cloudformation | Available |
   | glance      | image          | Available |
   | heat        | orchestration  | Available |
   | keystone    | identity       | Available |
   | neutron     | network        | Available |
   | nova        | compute        | Available |
   +-------------+----------------+-----------+

Run a test
==========

A lot of sample tests can be found in the Rally repository: https://github.com/openstack/rally/tree/master/samples/tasks.

Create the ``/opt/rally/tests/create-user.yaml`` file with the following content.

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

A Nginx server serving the ``results`` directory is running on the manager node on port ``8090``.

.. image:: /images/rally-result-html.png
