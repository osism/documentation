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
