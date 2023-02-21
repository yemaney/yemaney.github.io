## CloudFormation Physical & Logical Resources

- cloudformation template : YAML or JSON
  - used to create stacks
  - logical resource : what to create
    - can be reference / queried once create is in complete status
- Stack
  - create physical resources from the logical
  - if stacks template changes, then physical resources are also changed

## Template and Pseudo Parameters

- `template parameters`
  - accept input via console/cli/api
  - can be referenced from within logical resources
    - influence the physical resources
  - Options
    - Defaults, AllowedValues, Min/Max length, AllowedPatterns, NoEcho, Type
  
```yaml
Parameters:
  InstanceType:
  Type: String
  Default: t3.micro
  AllowedValues:
    - t3.micro
    - t3.medium
    - t3.large
  Description: Pick a supported instance type
```

- `psuedo parameter`
  - made available by aws, can be referenced without being defined

## Intrinsic Functions

- `Ref`
  - reference parameter value or logical resource physical ID 
- `Fn::GetAtt`
  - get attribute associated with a resource
    - like publicIP
- `Fn::Join` & `Fn::Split`
  - join and split strings
- `Fn::GetAzs`
  - get list of Azs where default vpc has subnets in
- `Fn::Select`
  - select one element from a list
- `Conditions (F::)`
  - IF, AND, EQUALS, NOT, OR
- `Fn::Base64`
  - accepts non encoded text, and outputs encoded text
- `Fn::Sub`
  - substitute things with text base on runtime information
- `Fn::Cidr`
  - generate a list of smaller cidr ranges for subnets from a larger vpc
- Fn::ImportValue, Fn::Transform

## Mappings

- optional
- contain mappings of keys to values
- allow lookups
- can have a key, or Top & Second Level
- Fn::FindInMap intrinsic function to retrieve values in a map.

## Outputs

- optional
- values can be declared in this section
- accessible from parent stack when using nesting
- can be exported, allowing cross stack references

## Conditions

- created in optional Conditions section of template
- evaluated to true or false
  - before resources are created
- use intrinsic functions AND, EQUALS, IF, NOT, OR
- associated with logical resources to control if they are created or nota
- can be nested

## DependsOn

- establish formal dependencies between resources
- cloudformation tries to automatically understand dependencies using references or functions used in the template
- can specify list of resources to define multiple dependencies
- example : make elastic ip depend on internet gateway, since an igw is needed to create an eip

## Wait Conditions, Creation Policy & cfn-signal

- `cnf-signal`
  - utility running on the instance that sends message back to cloudformation

- configure cloudformation to wait for certain number of success signals
- timeout H:M:S for those signals (12hr max)
- failure : failure signal or timeout before getting all signals 
- `creation policy`
  - generally used for ec2 instances or autoscaling groups
  - create endpoint that can be signaled to indicate when instance is really in created state 


- `wait condition`
  - for general progress gate
  - its own logical resource, not defined in an existing one
  - can depend on other resources, and vice versa
- `WaitHandle`
  - `generate presigned url` for resource signals
  - `can get response`
    - response can be accessed elsewhere in the template

## Nested Stacks

- `root / parent` stack
  - has nested stacks 
- can have a `cloudformation as a resource`
  - require a url to the template
  - must pass parameters
- root stack `can reference outputs of nested stacks`
  - STACKNAME.Outputs.xxx
- break up stack into modular templates allows you to `reuse templates`
- `lifecycle linked`
- `overcome 500 resource limit of one stack`

## Cross-Stack References

- cloudformation stack are designed to be isolated and self-contained
- outputs can be exported, making them visible to other stacks
- exports must have a unique name in the region
- Fn::ImportValue used to reference export values
- when you want to reuse resources
- different life-cycles

## StackSets

- deploy cfn stacks across many accounts & regions
- StackSets
  - containers in an admin account
  - contain stack instances which reference a stack
- Stack instances and stacks
  - in target accounts
  - each stack = 1 region 1 account
- workflow
  - permission granted via self-managed or service-managed roles  AWS ORG
  - StackSets gain access to target accounts and create stack instances followed by the stacks themselves
- Concurrent Accounts
  - how many accounts can be deployed into
  - more concurrent accounts the faster resources are deployed
- Failure Tolerance
  - amount of individual deployments can fail, before the stack set is considered a fail
- Retain Stacks
  - remove stack instances but retain the stacks
- Scenario:
  - Enable AWS Config across many accounts
  - Create AWS Config Rules : MFA, EIPS, EBS Encryption
  - Create IAM Roles for cross-account access at scale

## Deletion Policy

- if you delete a logical resource from a template
  - by default the physical resource is deleted
  - this can cause data loss
- deletion policy can be defined on each resource
- Delete : Default
- Retain : physical resource will not be deleted if logical resource is
- Snapshots : snapshot of resource before it is deleted
  - supports : EBS Volume, ElastiCache, Neptune, RDS, Redshift
  - snapshot live past stack lifetime
- Only apply to delete, not replace

## Stack Roles

- by default cfn uses the permissions of the logged in identity
  - mean you need the permissions for aws
- cfn can assume a role to gain the permissions
  - allows for role separation
  - identity creating the stack doesn't need resource permissions, only needs PassRole to cfn
  - identity also needs the permissions to create, update, delete stacks

## CFN-INIT

- simple configuration management system
- runs during bootstrapping
- configuration directives stored in template
- AWS::CloudFormation::Init part of logical resource
- config key : containers of configuration directives
- configSets
  - group of config keys
  - define which config keys to use and in what order
- user data vs cfn-init
  - User data : HOW: procedural
  - cfn-init : WHAT : desired state
    - `idempotent`
- cfn-init helper script
  - installed on ec2 os
- workflow:
  - template has ec2 resource with cloudformation init in metadata
  - cfn-init helper tool works in userdata
    - gets data from stack

## CFN-HUP

- cfn-init only runs once
- cfn-hup helper is a daemon that is installed an runs on the instance
- chfn-hup detects changes in resource metadata
- run configurable actions when a change is detected
  - re-runs cfn-init

## ChangeSets

- usual flows:
  - template -> stack -> create physical resources
  - delete stack -> delete physical resources
  - update template -> update stack -> resources change
    - no interruption, some interruption, replacement
- Change Sets let you preview changes

## Custom Resources

- cloudformation doesn't support everything
- custom resources let cfn integrate with anything it doesn't yet
- passes data to something, gets data back to something
