=======
Network
=======

.. contents::
   :local:

External connectivity
=====================

speedtest.net
-------------

* https://www.speedtest.net
* https://github.com/sivel/speedtest-cli

.. code-block:: console

   $ sudo apt-get install speedtest-cli

.. code-block:: console

   $ speedtest-cli --no-upload
   Retrieving speedtest.net configuration...
   Testing from TelemaxX Telekommunikation GmbH (a.b.c.d)...
   Retrieving speedtest.net server list...
   Selecting best server based on ping...
   Hosted by TelemaxX Telekommunikation GmbH (Karlsruhe) [1.17 km]: 1.483 ms
   Testing download speed................................................................................
   Download: 935.77 Mbit/s
   Skipping upload test

curl
----

.. code-block:: console

   $ curl ftp://speedtest.tele2.net/1GB.zip -o speedtest.zip
     % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
   100 1024M  100 1024M    0     0  90.0M      0  0:00:11  0:00:11 --:--:--  107M

.. code-block:: console

   $ curl https://speed.hetzner.de/10GB.bin -o /dev/null
     % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
   100  9.7G  100  9.7G    0     0   109M      0  0:01:31  0:01:31 --:--:--  111M

.. code-block:: console

   $ curl -T speedtest.zip ftp://speedtest.tele2.net/upload/
     % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
   100 1024M    0     0  100 1024M      0  95.7M  0:00:10  0:00:10 --:--:--  103M

Internal connectivity
=====================

iPerf
-----

* https://iperf.fr
* https://aws.amazon.com/premiumsupport/knowledge-center/network-throughput-benchmark-linux-ec2/

.. note::

   iperf3 is single threaded - therefore it might be limited by CPU and not actual network speed.
   If you expect more than approx. 20 GBit/s either start multiple iperf3 instances on different
   ports or you might consider using the older but multi-threaded iperf 2

.. code-block:: console

   $ sudo apt install iperf3

On the server side:

.. code-block:: console

   $ iperf3 -s
   -----------------------------------------------------------
   Server listening on 5201
   -----------------------------------------------------------
   [...]

On the client side:

.. code-block:: console

   $ iperf3 -c 10.30.50.11
   Connecting to host 10.30.50.11, port 5201
   [  4] local 10.30.50.10 port 42328 connected to 10.30.50.11 port 5201
   [ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
   [  4]   0.00-1.00   sec  1.15 GBytes  9.91 Gbits/sec    0    935 KBytes       
   [  4]   1.00-2.00   sec  1.15 GBytes  9.90 Gbits/sec    0    935 KBytes       
   [  4]   2.00-3.00   sec  1.15 GBytes  9.89 Gbits/sec    0   1.03 MBytes       
   [  4]   3.00-4.00   sec  1.15 GBytes  9.90 Gbits/sec    0   1.13 MBytes       
   [  4]   4.00-5.00   sec  1.15 GBytes  9.90 Gbits/sec    0   1.20 MBytes       
   [  4]   5.00-6.00   sec  1.15 GBytes  9.90 Gbits/sec    0   1.26 MBytes       
   [  4]   6.00-7.00   sec  1.15 GBytes  9.90 Gbits/sec    0   1.26 MBytes       
   [  4]   7.00-8.00   sec  1.15 GBytes  9.90 Gbits/sec    0   1.26 MBytes       
   [  4]   8.00-9.00   sec  1.15 GBytes  9.90 Gbits/sec    0   1.26 MBytes       
   [  4]   9.00-10.00  sec  1.15 GBytes  9.90 Gbits/sec    0   1.26 MBytes       
   - - - - - - - - - - - - - - - - - - - - - - - - -
   [ ID] Interval           Transfer     Bandwidth       Retr
   [  4]   0.00-10.00  sec  11.5 GBytes  9.90 Gbits/sec    0             sender
   [  4]   0.00-10.00  sec  11.5 GBytes  9.90 Gbits/sec                  receiver

   iperf Done.

.. code-block:: console

   $ iperf3 -c 192.168.200.100 -t 10 -V -u -b 10g
   iperf 3.1.3
   Linux 20-02 4.15.0-50-generic #54-Ubuntu SMP Mon May 6 18:46:08 UTC 2019 x86_64
   Time: Sun, 02 Jun 2019 11:22:53 GMT
   Connecting to host 192.168.200.100, port 5201
	 Cookie: 20-02.1559474573.408056.2c6c8bdb62d9
   [  4] local 192.168.200.200 port 33296 connected to 192.168.200.100 port 5201
   Starting Test: protocol: UDP, 1 streams, 8192 byte blocks, omitting 0 seconds, 10 second test
   [ ID] Interval           Transfer     Bandwidth       Total Datagrams
   [  4]   0.00-1.00   sec  1.03 GBytes  8.87 Gbits/sec  135329  
   [  4]   1.00-2.00   sec  1.15 GBytes  9.88 Gbits/sec  150793  
   [  4]   2.00-3.00   sec  1.15 GBytes  9.88 Gbits/sec  150777  
   [  4]   3.00-4.00   sec  1.15 GBytes  9.89 Gbits/sec  150929  
   [  4]   4.00-5.00   sec  1.15 GBytes  9.89 Gbits/sec  150948  
   [  4]   5.00-6.00   sec  1.15 GBytes  9.89 Gbits/sec  150940  
   [  4]   6.00-7.00   sec  1.15 GBytes  9.87 Gbits/sec  150574  
   [  4]   7.00-8.00   sec  1.15 GBytes  9.89 Gbits/sec  150843  
   [  4]   8.00-9.00   sec  1.15 GBytes  9.88 Gbits/sec  150800  
   [  4]   9.00-10.00  sec  1.15 GBytes  9.89 Gbits/sec  150971  
   - - - - - - - - - - - - - - - - - - - - - - - - -
   Test Complete. Summary Results:
   [ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
   [  4]   0.00-10.00  sec  11.4 GBytes  9.78 Gbits/sec  0.005 ms  1039856/1492835 (70%)  
   [  4] Sent 1492835 datagrams
   CPU Utilization: local/sender 75.1% (6.3%u/68.7%s), remote/receiver 0.5% (0.0%u/0.4%s)

   iperf Done.

.. code-block:: console

   $ iperf3 -c 192.168.200.100 -t 10 -V --parallel 10
   [...]
   Test Complete. Summary Results:
   [ ID] Interval           Transfer     Bandwidth       Retr
   [  4]   0.00-10.00  sec   986 MBytes   827 Mbits/sec    0             sender
   [  4]   0.00-10.00  sec   985 MBytes   826 Mbits/sec                  receiver
   [  6]   0.00-10.00  sec   739 MBytes   620 Mbits/sec    0             sender
   [  6]   0.00-10.00  sec   738 MBytes   619 Mbits/sec                  receiver
   [  8]   0.00-10.00  sec  2.88 GBytes  2.47 Gbits/sec    0             sender
   [  8]   0.00-10.00  sec  2.88 GBytes  2.47 Gbits/sec                  receiver
   [ 10]   0.00-10.00  sec  1.44 GBytes  1.24 Gbits/sec    0             sender
   [ 10]   0.00-10.00  sec  1.44 GBytes  1.24 Gbits/sec                  receiver
   [ 12]   0.00-10.00  sec   987 MBytes   828 Mbits/sec    0             sender
   [ 12]   0.00-10.00  sec   985 MBytes   826 Mbits/sec                  receiver
   [ 14]   0.00-10.00  sec   739 MBytes   620 Mbits/sec    0             sender
   [ 14]   0.00-10.00  sec   738 MBytes   619 Mbits/sec                  receiver
   [ 16]   0.00-10.00  sec   988 MBytes   829 Mbits/sec    0             sender
   [ 16]   0.00-10.00  sec   987 MBytes   828 Mbits/sec                  receiver
   [ 18]   0.00-10.00  sec  1.44 GBytes  1.24 Gbits/sec    0             sender
   [ 18]   0.00-10.00  sec  1.44 GBytes  1.24 Gbits/sec                  receiver
   [ 20]   0.00-10.00  sec   738 MBytes   619 Mbits/sec    0             sender
   [ 20]   0.00-10.00  sec   737 MBytes   618 Mbits/sec                  receiver
   [ 22]   0.00-10.00  sec   739 MBytes   620 Mbits/sec    0             sender
   [ 22]   0.00-10.00  sec   737 MBytes   618 Mbits/sec                  receiver
   [SUM]   0.00-10.00  sec  11.5 GBytes  9.91 Gbits/sec    0             sender
   [SUM]   0.00-10.00  sec  11.5 GBytes  9.90 Gbits/sec                  receiver
   CPU Utilization: local/sender 32.5% (1.1%u/31.4%s), remote/receiver 80.9% (2.7%u/78.2%s)

   iperf Done.
