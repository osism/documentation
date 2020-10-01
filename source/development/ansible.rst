=======
Ansible
=======

Test of roles on local systems
==============================

.. code-block:: console

   $ git clone https://github.com/osism/ansible-repository
   $ ansible-playbook -i localhost, -c local ansible-repository/molecule/default/converge.yml
