========
Operator
========

.. list-table::
   :widths: 10 90
   :align: left

   * - **Name**
     - ``osism.operator``
   * - **Repository**
     - https://github.com/osism/ansible-operator
   * - **Documentation**
     - ---

Add SSH public key
==================

Role ``osism.operator`` supports the configuration of arbitrary SSH public keys for the operator account.

Set the ``operator_authorized_keys`` list parameter in the ``environments/configuration.yml`` file.

.. code-block:: yaml

   operator_authorized_keys:
     - "ssh-rsa [...]"
     - "ssh-rsa [...]"
     [...]

The SSH private key of the operator user, which is used by the Ansible playbooks, is defined in the ``environments/secrets.yml``
file via the ``operator_private_key`` parameter. The associated SSH public key must also be added to the
``operator_authorized_keys`` list parameter.

Newly added SSH public keys could be transferred to the systems via ``osism-generic operator``.
