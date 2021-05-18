=======
Manager
=======

Preparations
------------

Before starting the upgrade, the configuration repository on the manager node
need to be prepared and updated.

.. contents::
   :local:

The *OSISM* version need to be set to the new version:

* configure version in ``environments/manager/configuration.yml``

.. code-block:: yaml

   ##########################
   # versions

   ceph_manager_version: 2019.4.0
   kolla_manager_version: 2019.4.0
   osism_manager_version: 2919.4.0

Make sure, the file ``requirements.txt`` in the root directory of the
configuration repository contains the following python modules:

* check ``requirements.txt``

.. code-block:: none

   Jinja2
   PyYAML
   python-gilt
   requests
   ruamel.yaml

Create temporary Python virtual environment for executing ``gilt``:

.. code-block:: console

   sudo apt-get install python3-venv
   python3 -m venv --prompt osism-upgrade .venv
   source .venv/bin/activate
   pip3 install wheel
   pip3 install python-gilt

Update the Python modules:

.. code-block:: console

   pip3 install -r requirements.txt

Next the configuration repository need to be synchronized with the master
configuration repository. Run the following command from the root directory
of the configuration repository at ``/opt/configuration/``:

.. code-block:: console

   MANAGER_VERSION=2019.4.0 gilt overlay

Review the changes made to the configuration repository and commit the changes:

.. code-block:: console

   git diff
   git add .
   git commit -m "Upgrade MANAGER_VERSION=2019.4.0"
   git push

The directories ``environments/manager/roles`` and
``environments/manager/.venv`` need to be deleted on the manager node.
They will be recreated and populated automatically.

.. code-block:: console

   rm -rf /opt/configuration/environments/manager/roles
   rm -rf /opt/configuration/environments/manager/.venv

Upgrading to Manager version 2019.4.0
-------------------------------------

ARA Ansible log server
~~~~~~~~~~~~~~~~~~~~~~

The ARA 1.x introduced in 2019.4.0 is unfortunately not downward compatible to
ARA 0.x. Hence, when upgrading to 2019.4.0, the ARA database must be reset.

The ara backend database need to be deleted:

.. code-block:: console

   docker rm -f manager_database_1
   docker volume rm manager_mariadb

The following ARA configuration block has become obsolete and need to be removed
from ``environments/ansible.cfg``.

.. code-block:: ini

   [ara]
   database = mysql+pymysql://ara:password@database/ara

The new variable ``ara_password`` need to be added to the file
``environments/secrets.yml``:

.. code-block:: console

   pwgen -1 32
   iMeebi0cofu3eiChoothahdoshi7Ohm7
   ansible-vault edit environments/secrets.yml

.. code-block:: yaml

   # manager
   ara_password: iMeebi0cofu3eiChoothahdoshi7Ohm7

Ceph
~~~~

When using Ceph, the following groups must be added to the inventory. Insert after the ``ceph-osd`` group.

.. code-block:: ini

   # NOTES: Subsequent groups necessary for compatibility to ceph-ansible. Don't change it.

   [mdss:children]
   ceph-mds

   [mgrs:children]
   ceph-mgr

   [mons:children]
   ceph-mon

   # [rgws:children]
   # ceph-rgw

   [osds:children]
   ceph-osd

.. warning::

   The environment ``monitoring`` is deprecated. The associated Ansible roles and Docker images
   (Prometheus and Prometheus exporters) will be removed in a future release.

Running the upgrade
===================

.. code-block:: console

   osism-generic configuration
   osism-manager

.. note::
   If encountering the following error message, while running ``osism-manager``

   ``ERROR! Attempting to decrypt but no vault secrets found``

   Place the vault password of the configuration repository into file in
   the users home folder and export the following environment variable:

.. code-block:: console

   export ANSIBLE_VAULT_PASSWORD_FILE=$HOME/vaultpass
