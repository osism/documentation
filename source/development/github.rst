======
GitHub
======

Hints when working with GitHub in the company scope.

Zuul
====

We use Zuul for our CI-CD pipelines. If your task requires secrets,
keep in mind to add a **no_log: true** to every task that handles
secrets (even if it's just scripts that take them).
Other points of possible leakage are the zuul-executor log files as
well as the *job-output.json*. It should also be empty. OTC therefore
forked the swift log upload job and created a fake *job-output.json*
without any content.

