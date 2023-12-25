## Concepts

| Concept             | Explanation                                                                                | Example                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| Labels              | Key-value pairs for object categorization in Kubernetes.                                   | Labeling a pod as "app=web" for later grouping or selection.                                              |
| Selectors           | Criteria to filter and match objects based on labels.                                      | Selecting pods with the label "environment=production" using a selector.                                  |
| Taints              | Properties applied to nodes to influence pod scheduling.                                   | Tainting a node as "NoSchedule" to prevent certain pod types from being scheduled on it.                  |
| Tolerations         | Declarations allowing pods to tolerate specific taints.                                    | Specifying toleration in a pod to be scheduled on nodes with specific taints.                             |
| Node Selectors      | Specifications in pod definitions constraining scheduling based on node labels.            | Assigning a pod to nodes with the label "type=worker" using node selectors.                               |
| Node Affinity       | Rules in pod specifications influencing pod scheduling based on node labels. `More Expressive than node selectors`              | Specifying node affinity to schedule pods on nodes with specific labels, like "zone=us-west" OR "zone=ca-central-1".             |
| Resource Requests   | Initial resource claims by a container upon scheduling.                                    | Requesting 0.5 CPU cores and 256 MiB of memory for a pod.                                                 |
| Resource Limits     | Maximum resource usage allowed for a container.                                            | Setting limits of 1 CPU core and 512 MiB of memory for a container.                                       |
| Limit Range         | Constraints on resource requests and limits for pods in a namespace.                       | Specifying that all pods in a namespace must have a minimum CPU request of 0.1 cores using a Limit Range. |
| Resource Quota      | Limits on aggregate resource usage within a namespace.                                     | Setting a Resource Quota to limit the total CPU cores and memory usage in a namespace.                    |
| DaemonSets          | Controllers ensuring a copy of a pod runs on all or selected nodes in a cluster.           | Using a DaemonSet to deploy a log collector on each node.                                                 |
| Static Pods         | Pods with configurations managed directly by the kubelet on a node.                        | Configuring a kubelet to start and manage pods based on static pod manifest files.                        |
| Multiple Schedulers | Kubernetes feature supporting the use of different schedulers for pod placement decisions. | Employing a specialized scheduler for certain nodes or pods based on custom requirements.                 |

This table provides a concise overview of each concept in Kubernetes, along with an example illustrating its usage.

## Comparisons

- scheduling:
  - taints and tolerations: deny pods from being scheduled in nodes
  - node selector & node affinity: select nodes a pod can be sceheduled in.
