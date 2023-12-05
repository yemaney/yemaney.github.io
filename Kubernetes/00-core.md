# Core

## Main K8s Cluster Architecture
- Main Node:
  - `etcd`: A distributed key-value store that stores the cluster's configuration data and provides a reliable source of truth.
  - `kube-scheduler`: Assigns Pods to nodes based on resource availability and other constraints.
  - `kube-controller-manager`: runs controller processes that loop to regulate the state of the system to achieve the desired state.
  - `kube-api server`: Exposes the Kubernetes API and acts as the front end for the Kubernetes control plane.

- Worker Nodes:
  - `kubelet`: An agent that runs on each worker node and ensures that containers are running in a Pod.
  - `kube-proxy`: Maintains network rules on nodes, enabling communication between Pods and external traffic.

```mermaid
graph TD
  subgraph Main_Node
    kube_api_server -->|Exposes API| controllers
    kube_api_server -->|Exposes API| kube_scheduler
    kube_api_server -->|Exposes API| etcd
  end

  subgraph Worker_Node_1
    kube_api_server -->|Exposes API| kubelet1
    kube_api_server -->|Exposes API| kube_proxy1
    kubelet1 -->|Manages| Pod1.1

    kube_proxy1 -->|Manages| Pod1.1 
  end

  subgraph Worker_Node_2
    kube_api_server -->|Exposes API| kubelet2
    kube_api_server -->|Exposes API| kube_proxy2
    kubelet2 -->|Manages| Pod2.1
    kubelet2 -->|Manages| Pod2.2

    kube_proxy2 -->|Manages| Pod2.1
    kube_proxy2 -->|Manages| Pod2.2
  end
```

---

### Main K8s Resources
- **Pods:** The smallest deployable units in Kubernetes, consisting of one or more containers and shared resources, enabling the deployment of applications.
- **ReplicaSets:** Kubernetes controllers that ensure a specified number of pod replicas are running, providing scalability, fault tolerance, and the ability to manage multiple identical instances.
- **Deployment:** A higher-level abstraction managing ReplicaSets, enabling declarative updates, rollbacks, and the definition of desired application states in Kubernetes.



```mermaid
graph TD
  subgraph Cluster
    subgraph Node1
      pod1.1
      pod1.2
      pod1.3
    end

    subgraph Node2
      pod2.1
      pod2.2
      pod3.3
    end
  
    subgraph ReplicaSet
      replicaset1 -->|Creates| Node1
      replicaset1 -->|Creates| Node2
    end
  
    subgraph Deployment
      deployment -->|Manages| ReplicaSet
    end
  end
```


- **Services:** Abstractions that define logical sets of pods and policies for accessing them, facilitating communication within the cluster or from external sources, with types such as NodePort, ClusterIP, and LoadBalancer.
  - **NodePort:** Exposes a service on a static port on each cluster node, enabling external access to the service.
  - **ClusterIP:** Exposes a service on a cluster-internal IP address, allowing communication only within the cluster.
  - **LoadBalancer:** Exposes a service externally using a cloud provider's load balancer, distributing incoming traffic across multiple pods for scalability and availability.

```mermaid
graph TD
  NodePort1 --> Node1
  NodePort2 --> Node2
  subgraph Cluster

    subgraph ClusterIP_Services
      db_svc <----> Node1
      api_svc <----> Node2
      db_svc <----> api_svc
    end
    subgraph Node1
      dbpod1.1
      dbpod1.2
      dbpod1.3
    end
    subgraph Node2
      apipod2.1
      apipod2.2
      apipod3.3
    end
  end
  subgraph LoadBalancerService
    LoadBalancer --> Node1
    LoadBalancer --> Node2
  end
```


- **Namespaces:** Virtual clusters within a Kubernetes cluster, providing a way to partition and isolate resources, enabling multiple teams or projects to share the same cluster without interference.

```mermaid
graph TD
  subgraph Cluster
    subgraph Namespace1
      pod1
      pod2
      service1 -->|In Namespace1| pod1
    end

    subgraph Namespace2
      pod3
      pod4
      service2 -->|In Namespace2| pod3
    end

    subgraph Namespace3
      pod5
      pod6
      service3 -->|In Namespace3| pod5
    end
  end
```
