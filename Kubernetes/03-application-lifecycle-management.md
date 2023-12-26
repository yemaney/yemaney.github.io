## Concepts

| Concept               | Explanation                                                                                                                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rolling Updates       | A strategy in Kubernetes deployments where a new version of a pod is gradually deployed while old pods are gradually terminated. This ensures continuous availability.                       |
| Rollbacks             | Reverting to a previous version of a deployment if issues are detected with the new version, ensuring a quick and reliable rollback to a known-good state.                                   |
| Pod Command           | The command to be executed when the container starts.                                                                                                                                        |
| Pod Args              | Command-line arguments passed to the container command .                                                                                                                                     |
| Environment Variables | Methods in Kubernetes for configuring environment variables: using the `env` field in pod specifications, ConfigMaps, or Secrets.                                                            |
| ConfigMap             | A Kubernetes resource for storing configuration data as key-value pairs, separate from pod specifications.                                                                                   |
| Secrets               | A Kubernetes resource for securely storing sensitive information, such as passwords or API keys, separate from pod specifications. Encoded but not encrypted. Not encrypted at rest in etcd. |
| Multi-Container Pods  | Pods with multiple containers that share the same network namespace, storage, and can communicate with each other.                                                                           |
| Init Containers       | Containers that run and complete before the main containers in a pod, used for setup or preparatory tasks, and share the same network namespace.                                             |
