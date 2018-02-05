========
RabbitMQ
========

Emptying the notification queues
================================

If notifications of individual services are activated and these notifications are not consumed,
for example by Panko, over the course of time many unprocessed messages accumulate on the
individual notification queues.

.. code-block:: shell

   $ docker exec -it rabbitmq rabbitmqctl list_queues | grep -v $'\t0'
   Listing queues
   versioned_notifications.info    2983
   versioned_notifications.error   29

   $ docker exec -it rabbitmq rabbitmqctl purge_queue versioned_notifications.info
   Purging queue 'versioned_notifications.info' in vhost '/'

rabbitmqadmin
=============

.. blockqoute:

   The management plugin ships with a command line tool rabbitmqadmin which can perform
   some of the same actions as the Web-based UI, and which may be more convenient for
   automation tasks. Note that rabbitmqadmin is just a specialised HTTP client; if you
   are contemplating invoking rabbitmqadmin from your own program you may want to consider
   using an HTTP API client library instead. [#s1]_

* https://www.rabbitmq.com/management-cli.html

.. [#s1] https://www.rabbitmq.com/management-cli.html
