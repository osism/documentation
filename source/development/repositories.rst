============
Repositories
============

The repositories are managed via the ``github-manager`` (https://github.com/osism/github-manager).

For each repository there is a file in ``orgs/osism/repositories`` with the name of the repository.

This file contains a dictionary, again with the name of the repository.

This allows new repositories to be added or modified within the ``osism``x organization.

To remove a repository the corresponding file is removed. Afterwards, the repository is removed manually.

.. code-block:: yaml

   ---
   ansible-collection-commons:
     default_branch: main
     description: Ansible collection with common roles
     homepage: https://www.osism.tech
     archived: false
     has_issues: true
     has_projects: false
     has_wiki: false
     private: false
     delete_branch_on_merge: true
     allow_merge_commit: false
     allow_squash_merge: true
     allow_rebase_merge: true
     teams:
       maintain:
         - maintainers
       pull:
       push:
       admin:
         - admins
     collaborators:
       maintain:
       pull:
       push:
       admin:
     topics:
       - ansible
       - ansible-collection
