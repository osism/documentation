====
Ceph
====

Luminous -> Luminous
====================

* ``environments/configuration.yml``

.. code-block:: yaml

   ceph_manager_version: 20180807-0

* ``environments/manager/configuration.yml``

.. code-block:: yaml

   ceph_manager_version: 20180807-0

* update the manager with ``osism-manager manager``

* check versions

.. code-block:: console

   $ ceph versions
   {
       "mon": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 3
       },
       "mgr": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 3
       },
       "osd": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 12
       },
       "mds": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 3
       },
       "overall": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 21
       }
   }

* start the update

.. code-block:: console

   $ osism-ceph rolling_update
   Are you sure you want to upgrade the cluster? [no]: yes
   [...]

* check versions during the update

.. code-block:: console

   $ ceph versions
   {
       "mon": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 2,
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 1
       },
       "mgr": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 3
       },
       "osd": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 12
       },
       "mds": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 3
       },
       "overall": {
           "ceph version 12.2.4 (52085d5249a80c5f5121a76d6288429f35e4e77b) luminous (stable)": 20,
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 1
       }
   }

* check versions after the update

.. code-block:: console

   $ ceph versions

   {
       "mon": {
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 3
       },
       "mgr": {
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 3
       },
       "osd": {
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 12
       },
       "mds": {
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 3
       },
       "overall": {
           "ceph version 12.2.7 (3ec878d1e53e1aeb47a9f619c49d9e7c0aa384d5) luminous (stable)": 21
       }
   }
