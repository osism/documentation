=================
Deployment models
=================

A deployment consists of 3 largely independent areas:

* Provisioning & deployment
* Controller
* Resources

Provisioning & deployment
=========================

The deployment and administration of all services is centrally managed on a
separate administaion node. In smaller environments, the manager node can be
virtualized. The use of a bare-metal system is recommended.

Optional infrastructure services (registry, installation, repository) are
provided here as well.


Controller
==========

The controller is modular and usually consists of 3 nodes. Individual modules of the controller, such as monitoring & logging, can be operated on independent nodes.

Network services are usually part of the controller, but can also be operated on the compute nodes. They are often operated on dedicated network nodes.

Resources
=========

Non-hyper-converged
-------------------

Compute services and storage services run on independent nodes.

Hyper-converged
---------------

Compute services and storage services reside on the same node.
