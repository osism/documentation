===============
Commit messages
===============

* Use present tense in the commit message header

  * The commit message header should be suited to be read in a sentence like: The effect of this
    commit when merged is to ...
  * ``Remove all easter eggs`` is good, ``Removed all easter eggs`` is bad.

* Avoid duplications and redundancies

  * When you commit to the ``testbed`` repository it is not necessary to use a prefix ``testbed:`` (e.g.
    ``Remove all easter eggs`` instead of ``testbed: remove all easter eggs``

  * When you commit to the ``testbed`` repository, it is not necessary to say that you are committing
    to the testbed repository (e.g. ``Remove all easter eggs`` instead of ``Remove all easter eggs in
    the testbed repository``)

* Add a ``Signed-off-by:`` footer to the commit message.

  * You can do this by adding the ``-s`` option to the ``git commit`` command.

Squash merge
============

When using squash merge, the commit message must always be revised manually.

The following commit message from a squash merge of a PR with 3 commits makes no sense.

.. code-block:: none

   Reposistory for  meeting minutes

   * Reposistory for  meeting mintues

   Signed-off-by: Max Mustermann <mustermann@osism.tech>

   * insert new line at the end

   Signed-off-by: Max Mustermann <mustermann@osism.tech>

   * yaml-linting

   Signed-off-by: Max Mustermann <mustermann@osism.tech>

This commit message should look like the following after the squash merge.
Commits that were added in a PR just to make the CI happy do not need to be
mentioned in the final commit message.

Multiple lines with a signed-off-by from the same author don't make sense either.

.. code-block:: none

   Reposistory for  meeting minutes

   Signed-off-by: Max Mustermann <mustermann@osism.tech>

References to issues
====================

We work with the issues from GitHub. The issues can be referenced in commit messages.
For this we always use the full path to the issue.
See https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue.

To close an issue via a commit, ``Closes osism/NAME_OF_THE_REPOSITORY#NUMBER_OF_THE_ISSUE`` is used as the last
line above the ``Signed-off-by`` line.

If a commit belongs to an issue, but does not close it directly, ``Related to osism/NAME_OF_THE_REPOSITORY#NUMBER_OF_THE_ISSUE``
or ``Part of osism/NAME_OF_THE_REPOSITORY#NUMBER_OF_THE_ISSUE`` is used.

The reference to an issue is never placed directly in the title of the commit message.
