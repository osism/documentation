======
GitHub
======

Hints when working with GitHub in the company scope.

Issues
======

Using the Github search, it is possible to view the issues for a specific organization.

https://github.com/search?q=user%3Aosism+state%3Aopen&type=Issues&ref=advsearch&l=&l=

Pull requests
=============

All code changes are introduced via pull requests, this allows code to be reviewed
and tested before it gets merged.

When changes to a pull request are to be made, the preferred option is to amend the
existing commit(s) as needed instead of adding additional commits that modify the
previous commits in your PR. This requires you to use the ``--force`` option on
your next ``git push``, but it helps to keep the git history clean and it also
mirrors the workflow for upstream projects using Gerrit instead of GitHub.

Zuul
====

We use Zuul for our CI-CD pipelines. If your task requires secrets,
keep in mind to add a **no_log: true** to every task that handles
secrets (even if it's just scripts that take them).
Other points of possible leakage are the zuul-executor log files as
well as the *job-output.json*. It should also be empty. OTC therefore
forked the swift log upload job and created a fake *job-output.json*
without any content.

