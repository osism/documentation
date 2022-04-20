===================
Ansible Style Guide
===================

We implement all the default rules of Ansible Lint. A listing of all these rules
can be found in the Ansible Lint documentation: https://ansible-lint.readthedocs.io/en/latest/default_rules/

Task naming
===========

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
