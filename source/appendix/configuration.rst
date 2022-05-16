===================
Extra Configuration
===================

This chapter is about some options beyond the basic setup.
Some examples are from firm of production environments.

.. contents::
   :depth: 2

Fluentd Authentication
======================

If fluentd is needed to communicate with elasticsearch authenticated or it shall
interact with a company independent elasticsearch, you are able to configure it
with the following configuration parameters:

.. code-block:: yaml
   :caption: /opt/configuration/environments/kolla/configuration.yml
 
   fluentd_elasticsearch_user: "<operator>"
   elasticsearch_address: "<otherhost>"


.. code-block:: yaml
   :caption: /opt/configuration/environments/kolla/secrets.yml

   fluentd_elasticsearch_password: "<SomePassword>"
