============================================
Open Source Infrastructure & Service Manager
============================================

The Open Source Infrastructure & Service Manager (OSISM) is an Ansible &
Docker based deployment framework for managing OpenStack, Ceph, and necessary
services.

Further details about OSISM can be found on https://www.osism.de. Do not hesitate
to write an e-mail to info@betacloud-solutions.de if you have questions or doubts.

A testbed of OSISM is available under https://github.com/osism/testbed. This
allows you to deploy a small environment with four nodes on a public cloud like our
`Betacloud <https://www.betacloud.de>`_. Other providers like Citycloud are also
supported.

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
   scaling
   upgrade
   test
   operations
   notes
   development
   appendix

The documentation is maintained on Github: https://github.com/osism/documentation.
There you can open issues for found errors and so on.

.. warning::

   This documentation does not claim to be complete or to be carried out step by step.
   Unless otherwise noted all configurations listed are examples and are not
   recommendations or mandatory specifications. Environmentally specific details such
   as network configuration, system names, partitioning, etc. are always determined
   during the preparatory work depending on the environment to be built.

.. note::

   OSISM is licensed under the Apache License, Version 2.0 (the "License");
   you may not use it except in compliance with the License.
   You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

.. [#] source: https://docs.openstack.org
.. [#] source: http://docs.ceph.com
.. [#] source: http://docs.ansible.com
.. [#] source: https://docs.docker.com
