# Elastic Compute Cloud (EC2)

- `virtual machines` known as instances
- private service, configured to run in a `VPC` network
- is launched into a specific subnet, AZ resilient
- different sizes and capabilities available
- on-demand billing per second
  - charged for compute, storage, and external software
- storage can be local on-host or Elastic Block Store (EBS)
  - will be charged for EBS even if instance is stopped
- states : running,  stopped, terminated
- windows rdp port 3389, linux ssh port 22


## Amazon Machine Image (AMI)
- has attached permissions defining who can use it
- used to create an EC2 or from an EC2
- contains the root volume, the drive that boots the operating system
- block device mapping, used to determine which volume is root volume and which is data volume