===================
Ansible Style Guide
===================

We implement all the default rules of Ansible Lint. A listing of all these rules
can be found in the Ansible Lint documentation: https://ansible-lint.readthedocs.io/en/latest/default_rules/

Task naming
===========

* Tasks must always have names. The only exception allowed is for forked playbooks.
* A name never starts with a small letter
* Names are written in present tense
* No punctuation is used in names

Positioning and use of the become directive
===========================================

The become directive is only set when needed and is always set explicitly
for each task that needs it.

Blocks, roles, or playbooks are never executed in a privileged mode.

We always insert the become directive between the name of a task
and the task itself. This also applies to related directives like become_user
or become_flags. This is for better visibility if a task is privileged or not.

.. code-block:: yaml

   - name: Copy hddtemp configuration file
     become: true
     ansible.builtin.copy:
       src: "{{ ansible_os_family }}/hddtemp"
       dest: "{{ hddtemp_conf_file }}"
       owner: root
       group: root
       mode: 0644
     notify: Restart hddtemp service

Usage of collections
====================
Collections are always defined as in the following example.

``netbox.netbox`` is here the collection that is used. 

.. code-block:: yaml

   - name: Configure netbox manufacturers
     netbox.netbox.netbox_manufacturer:
       netbox_url: "{{ netbox_url }}"
       netbox_token: "{{ netbox_token }}"
       data:
         name: "{{ item.value.name }}"
         slug: "{{ item.value.slug }}"
         description: "{{ item.value.description | default('') }}"
       state: present
     with_dict: "{{ netbox_data_manufacturers }}"

Please don´t declare it in this way!:

.. code-block:: yaml

   collections:
       - netbox.netbox

     tasks:
       - name: Manage Discworld site
         netbox_site:
           netbox_url: "{{ netbox_url }}"
           netbox_token: "{{ netbox_token }}"
           validate_certs: false
           data:
             name: Discworld
             slug: discworld
           state: present

The reason for that is, that the code is than more readable and easier to understand.


Parameters that offer lists
===========================

Parameters that provide a list are always defined as in the following example.

``docker_hosts_defaults`` sets the defaults in the role. Overriding is only possible
with the ``ansible-defaults`` repository.

In the configuration repository, docker_hosts_extra is then used to add additional
items to the list.

``docker_hosts`` itself is never modified from the outside.

.. code-block:: yaml

   docker_hosts_defaults:
     - "unix:///var/run/docker.sock"
   docker_hosts_extra: []
   docker_hosts: "{{ docker_hosts_defaults + docker_hosts_extra }}"
