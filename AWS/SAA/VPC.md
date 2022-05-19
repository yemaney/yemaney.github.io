# AWS Virtual Private Cloud {VPC}

- a virtual private network inside of AWS
- regionally resilient
  - `divided into subnets`, each located in an AZ
- private and isolated by default

### Default
- one default VPC per region
- comes with  internet gateway (IGW), Security Group (SG) & NACL
- subnets assign public IPv4 addresses

*best practice not to use default VPC*

## AWS Public vs Private Services

1. `AWS Public Zone:`
    - network that is connected to the public internet
    - where aws services with public endpoints operate from, ie S3
    - internet is used as transit in with communication
2. `AWS Private Zone: Virtual Private Clouds (VPC)`
   - isolated unless configured to otherwise, can't be reached by public internet unless explicitly allowed
   - services can be hosted in these private networks
   - can communicate with aws public zone without touching the internet
   - can access the internet via `IGW`
   - can be access by on-prem using `VPN` or `Direct Connect`
