===============
External access
===============

All systems must be able to access the following external systems.
Access via HTTP proxy is also possible.

======================== ======= ====================================
Description              Port    URL
======================== ======= ====================================
Container images             443 https://registry.airgap.services.osism.tech
OpenStack machine images     443 https://minio.services.osism.tech
Ubuntu packages               80 http://archive.ubuntu.com
Ubuntu packages              443 https://download.docker.com
Ubuntu packages              443 https://packagecloud.io
======================== ======= ====================================

The following accesses are additionally required for the manager.
Only required for the initial deployment of the manager node when not
being able to use Docker there.

======================== ======= ====================================
Description              Port    URL
======================== ======= ====================================
Ansible collections          443 https://github.com
Ansible collections          443 https://galaxy.ansible.com
Python packages              443 https://pypi.org
======================== ======= ====================================

The following accesses are additionally required for the manager.
Only required when using Bifrost.

======================== ======= ====================================
Description              Port    URL
======================== ======= ====================================
OpenDev services         443     https://\*.opendev.org
======================== ======= ====================================
