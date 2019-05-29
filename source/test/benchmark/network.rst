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
