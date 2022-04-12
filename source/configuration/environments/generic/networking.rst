==========
Networking
==========

Interfaces
==========

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.network-interfaces``
   * - **Repository**
     - https://github.com/osism/ansible-network-interfaces
   * - **Documentation**
     - ---

Proxy
=====

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.proxy``
   * - **Repository**
     - https://github.com/osism/ansible-proxy
   * - **Documentation**
     - ---

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

Resolvconf
==========

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.resolvconf``
   * - **Repository**
     - https://github.com/osism/ansible-resolvconf
   * - **Documentation**
     - ---

If available, the company's internal DNS servers should be used. If no own DNS servers
are available, we recommend using the DNS servers from `Quad9 <https://www.quad9.net>`_.

* ``environments/configuration.yml``

.. code-block:: yaml

   ##########################
   # resolvconf

   resolvconf_nameserver:
     - 9.9.9.9
     - 149.112.112.112
   resolvconf_search: osism.io


Network Interface Card Offloading
=================================

If vxlan or geneve tunnel's for overlay networks enabled. For performance issues
it will be need to enable hardware offloading.

This can verify with ethtool and the following paramameter:

.. code-block:: console
   
   ethtool -k enoX 

This can set with ethtool and following parameters:

.. code-block:: console
    
    ethtool -K enoX rx on tx on sg on tso on lro on

If jumboframes are enabled it make sense to increase the tx and rx buffer to 
the hardware possible maximum size. 

This can verify with ethtool and the following paramameter:

.. code-block:: console
    
    ethtool -g enoX 

This can set with ethtool and following parameters:

.. code-block:: console
   
   ethtool -G enoX rx <Size> tx <Size> 
