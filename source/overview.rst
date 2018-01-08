========
Overview
========

.. blockdiag::

   diagram {
     compute [stacked];
     network [stacked];
     controller [stacked];
     storage [stacked];
     seed -> manager;
     monitoring <-> compute;
     monitoring <-> network;
     monitoring <-> storage;
     monitoring <-> controller;
     manager -> compute;
     manager -> network;
     manager -> storage;
     manager -> controller;
     compute <-> network;
     compute <-> controller;
     compute <-> storage;
     controller <-> storage;
   }

Node types
==========

* compute
* controller
* monitoring
* network
* seed
* storage

Network
=======
