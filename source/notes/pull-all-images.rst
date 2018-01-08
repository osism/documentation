===============
Pull all images
===============

.. code-block:: console

   $ osism-kolla pull common,elasticsearch,haproxy,memcached,mariadb,rabbitmq,kibana,grafana,gnocchi
   [...]
   TASK [common : Pulling kolla-toolbox image] ************************************
   ok: [20-10.betacloud.xyz]
   ok: [50-11.betacloud.xyz]
   ok: [50-10.betacloud.xyz]
   ok: [50-12.betacloud.xyz]
   ok: [20-11.betacloud.xyz]
   ok: [20-12.betacloud.xyz]
   ok: [30-10.betacloud.xyz]
   ok: [30-11.betacloud.xyz]
   ok: [10-11.betacloud.xyz]
   [...]

   $ osism-kolla pull keystone,glance,heat,horizon,cinder,neutron,nova,ceilometer
   [...]
   TASK [common : Pulling keystone image] *****************************************
   ok: [20-10.betacloud.xyz]
   ok: [50-11.betacloud.xyz]
   ok: [50-10.betacloud.xyz]
   ok: [50-12.betacloud.xyz]
   ok: [20-11.betacloud.xyz]
   ok: [20-12.betacloud.xyz]
   ok: [30-10.betacloud.xyz]
   ok: [30-11.betacloud.xyz]
   ok: [10-11.betacloud.xyz]
   [...]
