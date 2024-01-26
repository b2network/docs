# Multi Nodes
In this chapter, we will look at how to use [docker](https://docs.docker.com/engine/install/) to launch four nodes.

After entering the [b2-node](https://github.com/b2network/b2-node.git) code repository root directory, execute the following command:

```
$ make localnet-start
```

The above command will first compile the Docker image, then generate the configuration file for starting the image, and finally start 4 nodes using the `networks/local/ethermintnode/docker-compose.yml` file.

The following command can be used to view the running Docker node services:

```
$ docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS         PORTS                                                                                   NAMES
fe3dc26d24b3   ethermintd/node   "/bin/bash -c 'ether…"   8 seconds ago   Up 6 seconds   1317/tcp, 8545-8546/tcp, 9090/tcp, 0.0.0.0:26661->26656/tcp, 0.0.0.0:26662->26657/tcp   b2-node2
75c31a6d52cb   ethermintd/node   "/bin/bash -c 'ether…"   8 seconds ago   Up 6 seconds   1317/tcp, 8545-8546/tcp, 9090/tcp, 0.0.0.0:26659->26656/tcp, 0.0.0.0:26660->26657/tcp   b2-node1
010bc72793b5   ethermintd/node   "/bin/bash -c 'ether…"   8 seconds ago   Up 6 seconds   1317/tcp, 8545-8546/tcp, 9090/tcp, 0.0.0.0:26663->26656/tcp, 0.0.0.0:26664->26657/tcp   b2-node3
0385263ae411   ethermintd/node   "/bin/bash -c 'ether…"   8 seconds ago   Up 6 seconds   1317/tcp, 8545-8546/tcp, 9090/tcp, 0.0.0.0:26656-26657->26656-26657/tcp                 b2-node0
```

You will see the generated node configuration file under the build directory:
```
$ ls build                                            
gentxs     node0      node1      node2      node3
```

Use the following command to stop the services:

```
$ docker-compose -f networks/local/ethermintnode/docker-compose.yml down
```