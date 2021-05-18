====
Ceph
====

.. contents::
   :depth: 2

* https://tracker.ceph.com/projects/ceph/wiki/Benchmark_Ceph_Cluster_Performance

.. note::

   The subsequent commands are executed within the ``cephclient`` container.

   .. code-block:: console

      $ docker exec -it cephclient_cephclient_1 bash
      dragon@e0e0987bd105:/$

RADOS
=====

Preparations
============

.. code-block:: console

   $ ceph osd pool create testing 100 100
   pool 'testing' created

Execution
=========

RADOS
-----

.. code-block:: console

   $ rados bench -p testing 10 write --no-cleanup
   $ rados bench -p testing 10 seq
   $ rados bench -p testing 10 rand
   $ rados -p testing cleanup

RBD
---

.. code-block:: console

   $ rbd create image01 --size 1024 --pool testing
   $ rbd bench-write image01 --pool=testing
   $ rbd remove -p testing image01

fio
---

Create a file ``/tmp/testing.fio`` with this content

.. code-block:: ini

   [global]
   ioengine=rbd
   clientname=admin
   pool=testing
   rbdname=image01
   rw=randwrite
   bs=4k

   [rbd_iodepth32]
   iodepth=32

.. code-block:: console

   $ rbd create image01 --size 1024 --pool testing
   $ fio /tmp/testing.fio
   $ rbd remove -p testing image01

Cleanup
=======

.. code-block:: console

   $ ceph osd pool delete testing testing --yes-i-really-really-mean-it
   pool 'testing' removed
