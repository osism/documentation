=======
Network
=======

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
