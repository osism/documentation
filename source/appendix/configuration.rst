=============
Configuration
=============

The chapter configuration is about some option beyond the basic setup.
Some examples are from firm of production environments.

.. contents::
   :depth: 2

Fluentd Authentication
============

If fluentd is needed to communicate with elasticsearch authenticated or it shall
to interact with a company independent elasticsearch, you are able to configure it
with following configuration parameters:

.. code-block:: console

   /opt/configuration/environments/kolla/configuration.yml
 
   fluentd_elasticsearch_user: "<operator>"
   fluentd_elasticsearch_password: "<SomePassword>"
   elasticsearch_address:"<otherhost>"

    /opt/configuration/environments/kolla/secrets.yml

    fluentd_elasticsearch_password: "<SomePassword>"