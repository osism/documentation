==============
Proxy Settings
==============

There are three proxy configuration

* proxy for manager bootstrap

.. code-block:: yaml
   :caption: environments/manager/configuration.yml

   ##########################
   # proxy

   proxy_url_custom: "http://proxy_user:proxy_pwd@proxy_url:proxy_port"
   proxy_proxies:
     http: "{{ proxy_url_custom }}"
     https: "{{ proxy_url_custom }}"
   proxy_package_manager: no

* proxy for operating system in ``/etc/environment`` and for ``apt``.

.. code-block:: yaml
   :caption: environments/configuration.yml

   # system proxy
   proxy_url_custom: "http://proxy_user:proxy_pwd@proxy_url:proxy_port"
   proxy_proxies:
     http: "{{ proxy_url_custom }}"
     https: "{{ proxy_url_custom }}"
   proxy_package_manager: no
   proxy_no_proxy_extra:
     - 127.0.0.1
     - 10.0.3.10
     - 10.0.3.11
     - 10.0.3.12
     - localhost
     - api-int.osism.xyz
     - api.osism.xyz

* proxy for docker to pull images.

.. code-block:: yaml
   :caption: environments/configuration.yml

   # docker proxy
   proxy_url_custom: "http://proxy_user:proxy_pwd@proxy_url:proxy_port"
   docker_configure_proxy: true
   docker_proxy_http: "{{ proxy_url_custom }}"
   docker_proxy_https: "{{ proxy_url_custom }}"
   docker_proxy_no_proxy:
     - 127.0.0.1
     - 10.0.3.10
     - 10.0.3.11
     - 10.0.3.12
     - localhost
     - api-int.osism.xyz
     - api.osism.xyz
