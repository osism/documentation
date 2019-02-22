=======
Gnocchi
=======

Grafana integration
===================

* https://gnocchi.xyz/grafana.html

.. note::

   When Gnocchi and Grafana are activated, the necessary configuration parameters are
   already set by default. This is only necessary if an external grafana installation is used.

* ``environments/kolla/files/overlays/gnocchi.conf``

.. code-block:: ini

   [cors]
   allowed_origin = {{ public_protocol }}://{{ kolla_external_fqdn }}:{{ grafana_server_port }}

* ``environments/kolla/files/overlays/keystone.conf``

.. code-block:: ini

   [cors]
   allowed_origin = {{ public_protocol }}://{{ kolla_external_fqdn }}:{{ grafana_server_port }}
