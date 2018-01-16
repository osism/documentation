======================================
Move /var/lib/docker to a block device
======================================

.. code-block:: yaml

   ##########################################################                                                          
   # docker                                                  

   docker_configure_storage_block_device: yes                
   docker_storage_block_device: /dev/vdb                     
   docker_storage_filesystem: ext4

.. code-block:: shell

   $ sudo mkfs.ext4 /dev/vdb
   $ echo "/dev/vdb /var/lib/docker ext4 defaults 0 0" | sudo tee -a /etc/fstab

.. code-block:: shell

   $ docker ps -q > running.YYYYMMDD
   $ docker stop $(cat running.YYYYMMDD)
   $ sudo systemctl stop docker

.. code-block:: shell

   $ sudo mv /var/lib/docker /var/lib/docker.YYYYMMDD
   $ sudo mkdir /var/lib/docker
   $ sudo mount /var/lib/docker
   $ sudo rsync -avz /var/lib/docker.YYYYMMDD/ /var/lib/docker/

.. code-block:: shell

   $ sudo systemctl start docker
   $ docker start $(cat running.YYYYMMDD)
   $ rm running.YYYYMMDD
   $ sudo rm -rf /var/lib/docker.YYYYMMDD
