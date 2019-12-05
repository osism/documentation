============================================
Open Source Infrastructure & Service Manager
============================================

The Open Source Infrastructure & Service Manager (OSISM) is an Ansible &
Docker based deployment framework for managing OpenStack, Ceph, and necessary
services.

Further details about OSISM can be found on https://osism.io. Do not hesitate
to write an e-mail to info@betacloud-solutions.de if you have questions or doubts.

* **OpenStack** is a cloud operating system that controls large pools of
  compute, storage, and networking resources throughout a datacenter, all managed
  through a dashboard that gives administrators control while empowering their users
  to provision resources through a web interface. [#]_

* **Ceph** uniquely delivers object, block, and file storage in one unified system. [#]_

* **Ansible** is a simple, agentless and powerful open source IT automation. [#]_

* **Docker** provides a way to run applications securely isolated in a container,
  packaged with all its dependencies and libraries. [#]_

.. toctree::
   :maxdepth: 2

   overview
   configuration
   deployment
   upgrade
   test
   operations
   notes
   appendix

The documentation is maintained on Github: https://github.com/osism/documentation.
There you can open issues for found errors and so on.

.. warning::

   This documentation does not claim to be complete or to be carried out step by step.
   Unless otherwise noted all configurations listed are examples and are not
   recommendations or mandatory specifications. Environmentally specific details such
   as network configuration, system names, partitioning, etc. are always determined
   during the preparatory work depending on the environment to be built.

.. [#] source: https://docs.openstack.org
.. [#] source: http://docs.ceph.com
.. [#] source: http://docs.ansible.com
.. [#] source: https://docs.docker.com
