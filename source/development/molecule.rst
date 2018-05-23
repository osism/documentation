========
Molecule
========

Manual execution
================

Prepartions
-----------

* Create ``clouds.yml`` file in ``molecule/default`` (the name of the cloud must be ``molecule``)
* Prepare a virtual environment in the root directory of the role: ``virtualenv .venv; source venv/bin/activate``
* Install the necessary dependencies: ``pip install -r test-requirements.txt``
* Install the Ansible version to be tested: ``pip install 'ansible>=2.5.0.0,<2.6'``
* Execute ``molecule create`` followed by ``molecule dependency`` to prepare the required infrastructure.
* Execute ``molecule login`` to log in.
* Execute ``molecule destroy`` to destroy the infrastructure.

Execution
---------

* Execute ``molecule converge`` to run the playbook. If not already executed, ``create`` and ``dependency`` are also executed.
* Execute ``molecule verify`` to run the verification.

Configuration
=============

Testinfra
=========

* https://testinfra.readthedocs.io

Place all tests in the ``molecule/default/tests`` directory in the ``test_default.py`` file.
