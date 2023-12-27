## Concepts

| Concept                                 | Explanation                                                                                                                                     |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Drain                                   | Draining a node in Kubernetes involves gracefully evicting pods from the node, preparing it for maintenance or decommissioning.                 |
| Cordon                                  | Cordoning a node in Kubernetes prevents new pods from being scheduled onto the node. Existing pods continue to run.                             |
| Uncordon                                | Uncordoning a node in Kubernetes allows new pods to be scheduled onto the node after it was previously cordoned.                                |
| Backup and Restore                      | Backup and restore in Kubernetes can be performed from configuration files or directly from etcd, the key-value store.                          |
| Export ETCDCTL_API=3                    | Sets the environment variable to specify the etcdctl API version (version 3 in this case).                                                      |
| etcdctl snapshot save                   | etcdctl command to create a snapshot of the etcd key-value store, capturing the current state for backup or migration.                          |
| etcdctl snapshot restore                | etcdctl command to restore the etcd key-value store from a previously created snapshot.                                                         |
| etcd needs cacert, cert, endpoints, key | etcd requires certain parameters for secure communication: CA certificate (--cacert), client certificate (--cert), --endpoints, and client key (--key). |

## Extra

- restoring from etcd server
  - create a snapshot
  - restore a snapshot to a folder
  - update etcd service `data-dir` to use new folder

