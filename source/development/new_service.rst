=============================
Adding a new service to OSISM
=============================

If you want to add a service to osism, this is done via an Ansible role.
An example workflow how to do so might look like this:

- Add the Ansible Playbook Code: https://github.com/osism/ansible-playbooks/pull/215
- Add the Ansible Playbook to python-osism: https://github.com/osism/python-osism/pull/2
- Create a new Ansible inventory group for this: https://github.com/osism/cfg-generics/pull/225
- Add the image to the release repositoriy: https://github.com/osism/release/pull/278
- Add the image to osism-ansible container: https://github.com/osism/container-image-osism-ansible/pull/215
- Image registry and host need to be added in ansible-defaults: https://github.com/osism/ansible-defaults/pull/54
- Add the deployment to the testbed: https://github.com/osism/testbed/pull/1043
- Add the service netzwerk and port to the documentation: https://github.com/osism/documentation/pull/330
- If required, add the container image in the container-images repository (the example here is from another service, yet it is good for understanding): https://github.com/osism/container-images/pull/34
- Add the role in the respective ansible collection: https://github.com/osism/ansible-collection-services/pull/578
- Add a release note: https://github.com/osism/release/pull/279

