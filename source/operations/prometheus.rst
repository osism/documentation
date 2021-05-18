==========
Prometheus
==========

.. contents::
   :depth: 2

panic: runtime error: slice bounds out of range
===============================================

frequently restarting prometheus container

.. code-block:: console

   $ docker logs --tail 100 -f prometheus_prometheus_1
   ...
   panic: runtime error: slice bounds out of range

   goroutine 59 [running]:
   github.com/prometheus/prometheus/vendor/github.com/prometheus/tsdb/wal.(*Reader).next(0xc00ed62000, 0xc000fba8a0, 0xc000807bf0)
           /go/src/github.com/prometheus/prometheus/vendor/github.com/prometheus/tsdb/wal/wal.go:739 +0x9a6

delete old data in

.. code-block:: console

   $ ls -la /var/lib/docker/volumes/prometheus_prometheus/_data