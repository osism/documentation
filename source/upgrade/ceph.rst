====
Ceph
====

Luminous -> Mimic
=================

.. code-block:: console

   $ ceph versions
   {
       "mon": {
           "ceph version 12.2.1 (3e7492b9ada8bdc9a5cd0feafd42fbca27f9c38e) luminous (stable)": 3
       },
       "mgr": {
           "ceph version 12.2.1 (3e7492b9ada8bdc9a5cd0feafd42fbca27f9c38e) luminous (stable)": 3
       },
       "osd": {
           "ceph version 12.2.1 (3e7492b9ada8bdc9a5cd0feafd42fbca27f9c38e) luminous (stable)": 12
       },
       "mds": {},
       "overall": {
           "ceph version 12.2.1 (3e7492b9ada8bdc9a5cd0feafd42fbca27f9c38e) luminous (stable)": 18
       }
   }

.. code-block:: console

   $ ceph mon feature ls
   all features
           supported: [kraken,luminous]
           persistent: [kraken,luminous]
   on current monmap (epoch 2)
           persistent: [kraken,luminous]
           required: [kraken,luminous]
