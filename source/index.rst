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
  to provision resources through a web interface. [#s1]_

* **Ceph** uniquely delivers object, block, and file storage in one unified system. [#s2]_

* **Ansible** is a simple, agentless and powerful open source IT automation. [#s3]_

* **Docker** provides a way to run applications securely isolated in a container,
  packaged with all its dependencies and libraries. [#s4]_

.. toctree::
   :maxdepth: 2

   overview
   configuration
   deployment
   test
   operations
   notes
   development
   appendix

The documentation is maintained on Github: https://github.com/osism/documentation.
There you can open issues for found errors and so on.

.. [#s1] source: https://docs.openstack.org
.. [#s2] source: http://docs.ceph.com
.. [#s3] source: http://docs.ansible.com
.. [#s4] source: https://docs.docker.com
