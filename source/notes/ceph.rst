====
Ceph
====

Deep scrub distribution
=======================

* https://ceph.com/geen-categorie/deep-scrub-distribution/

Distribution per weekday:

.. code-block:: console

   $ for date in $(ceph pg dump | grep active | awk '{ print $20 })'; do date +%A -d $date; done | sort | uniq -c

Distribution per hours:

.. code-block:: console

   $ for date in $(ceph pg dump | grep active | awk '{ print $21 }'); do date +%H -d $date; done | sort | uniq -c
