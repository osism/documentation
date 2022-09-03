=====
Panko
=====

Delete expired events
=====================

By default the expiration of Panko events is disabled. This needs to be configured in the
``panko.conf`` first. The ``event_time_to_live`` is configured in seconds. So a two week cleanup
time would be ``1209600`` seconds.

* ``environments/kolla/files/overlays/panko.conf``

.. code-block:: ini

   [database]
   event_time_to_live = 1209600

After the configuration is rolled out (``osism-kolla deploy panko -l control``) the expired events
can be cleaned up via

.. code-block:: console

   docker exec -it panko_api panko-expirer

In order to automatically clean up the entries a cronjob should be configured to run on a node where
the `panko_api` container is running (one of the control nodes)

* ``environments/custom/playbook-cronjobs.yml``

.. code-block:: yaml

       - name: Cleanup panko db daily
         cron:
           name: "cleanup panko db daily"
           minute: "43"
           hour: "1"
           job: /usr/bin/docker exec panko_api panko-expirer
           cron_file: osism
           user: "{{ operator_user }}"
         become: true
         delegate_to: testbed-node-1.osism.local