==========
Deployment
==========

The deployment of OSISM is carried out in several successive phases.
The phases are documented in this chapter.

1. Preparation of a seed node
2. Bootstrap and deployment of a manager node
3. Provisioning of the bare-metal systems

.. blockdiag::

    blockdiag {
      node_width = 200;
      node_height = 100;

      seed [numbered = 1];
      manager [numbered = 2];
      bare-metal [numbered = 3];

      seed -> manager -> bare-metal;
    }

4. Bootstrap of all remaining nodes
5. Deployment of the individual services

.. blockdiag::

   blockdiag {
     node_width = 200;
     node_height = 100;

     manager;
     bootstrap [numbered = 4];
     services [numbered = 5];

     manager -> bootstrap -> services;
   }

.. toctree::
   :maxdepth: 2

   deployment/seed
   deployment/provisioning
   deployment/manager
   deployment/bootstrap
   deployment/services
