=====
Nexus
=====

Import custom certifications (optional)
=======================================

.. code-block:: yaml
   :caption: environments/infrastructure/configuration.yml

   nexus_api_url: "10.0.3.1:8190"
   nexus_truststore_cert_urls:
     - download.docker.com
     - linux.mellanox.com

Nexus rollout
=============

.. code-block:: console

   osism-infrastructure nexus
