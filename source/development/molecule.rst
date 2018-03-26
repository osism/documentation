========
Molecule
========

Manual execution
================

Prepartions
-----------

* Create ``clouds.yml`` file in ``molecule/default``
  * The name of the cloud must be ``molecule``
* Prepare a virtual environment in the root directory of the role
  * ``virtualenv .venv; source venv/bin/activate``
* Install the necessary dependencies
  * ``pip install -r test-requirements.txt
* Install the Ansible version to be tested
  * ``pip install 'ansible>=2.4,<2.5'

Execution
---------

* ``molecule converge``
* ``molecule verify``
* ``molecule destroy``
