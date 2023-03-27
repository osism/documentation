==========
Ceilometer
==========

* https://docs.openstack.org/ceilometer/latest/

Configuration parameters
========================

.. code-block:: yaml

   enable_ceilometer: "yes"

* ``environments/kolla/files/overlays/ceilometer.pipeline.yaml``

.. code-block:: yaml

   ---
   sources:
     - name: meter_source
       meters:
         - "*"
       sinks:
         - meter_sink
         - gnocchi
   sinks:
     - name: meter_sink
       publishers:
         - prometheus://testbed-manager-0.testbed.osism.xyz/metrics/job/openstack-telemetry
     - name: gnocchi
       publishers:
         - gnocchi://

