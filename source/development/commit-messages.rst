===============
Commit messages
===============

* Avoid duplications and redundancies

  * When you commit to the ``testbed`` repository it is not necessary to use a prefix ``testbed:`` (e.g.
    ``Remove all easter eggs`` instead of ``testbed: remove all easter eggs``

  * When you commit to the ``testbed`` repository, it is not necessary to say that you are committing
    to the testbed repository (e.g. ``Remove all easter eggs`` instead of ``Remove all easter eggs in
    the testbed repository``)

Squash merge
============

When using squash merge, the commit message must always be revised manually.

The following commit message from a squash merge of a PR with 3 commits makes no sense.

.. code-block:: none

   Reposistory for  meeting minutes

   * Reposistory for  meeting mintues

   Signed-off-by: Mathias Fechner <fechner@osism.tech>

   * insert new line at the end

   Signed-off-by: Mathias Fechner <fechner@osism.tech>

   * yaml-linting

   Signed-off-by: Mathias Fechner <fechner@osism.tech>

This commit message should look like the following after the squash merge.
Commits that were added in a PR just to make the CI happy do not need to be
mentioned in the final commit message.

Multiple lines with a signed-off-by from the same author don't make sense either.

.. code-block:: none

   Reposistory for  meeting minutes

   Signed-off-by: Mathias Fechner <fechner@osism.tech>
