============
Issue labels
============

Labels management
=================

The labels are managed via the github-manager (https://github.com/osism/github-manager).

The config.yaml file lists all available labels. There they can be added accordingly and so on.

All defined labels are available in all repositories of the ``osism`` organization.

.. code-block:: yaml

   labels:
     - name: needs rework
       description: "Needs rework"
       color: "b60205"
     - name: bug
       description: "Something isn't working"
       color: "d73a4a"
