============
Update facts
============

.. note:: Run this command on the manager node.            

.. code-block:: console                                    

   $ osism-generic facts                                   

   PLAY [Gather facts for all hosts] **********************************************                                   

   TASK [setup] *******************************************************************                                   
   ok: [20-11.betacloud.xyz]                               
   ok: [20-10.betacloud.xyz]                               
   ok: [50-10.betacloud.xyz]                               
   ok: [50-11.betacloud.xyz]                               
   ok: [50-12.betacloud.xyz]                               
   ok: [10-11.betacloud.xyz]                               
   ok: [30-10.betacloud.xyz]                               
   ok: [20-12.betacloud.xyz]                               
   ok: [30-11.betacloud.xyz]                               

   PLAY [Gather facts for all hosts (if using --limit)] ***************************                                   

   TASK [setup] *******************************************************************
   skipping: [30-11.betacloud.xyz] => (item=20-11.betacloud.xyz)
   skipping: [30-11.betacloud.xyz] => (item=20-10.betacloud.xyz)
   [...]

   PLAY RECAP *********************************************************************
   10-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   20-10.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   20-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   20-12.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   30-10.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   30-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   50-10.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   50-11.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
   50-12.betacloud.xyz        : ok=1    changed=0    unreachable=0    failed=0
