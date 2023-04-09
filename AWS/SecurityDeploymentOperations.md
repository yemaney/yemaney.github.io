# SECURITY, DEPLOYMENT & OPERATIONS


## Secrets Manager

- `designed for secrets`
  - password, API keys
- usable via console, cli, api, sdk
- `supports automatic rotation`
  - using lambda
- directly integrates with some aws products
  - RDS
- `encrypted at rest`  with KMS

## WAF & Shield

### Shield

- `provides aws resources with DDoS protection`
  - layer 3 and layer 4 DDoS protection
    - packets, segments, ips, ports, sessions
    
- `Standard`
  - free with R53 and cloudfront
- `Advanced`
  - $3000p/m
  - EC2, ELB, CloudFront, Global Accelerator, R53
  - DDoS Response team & financial insurance for attacks

### Web Application Firewall (WAF)

- `layer 7 (HTTP/s) firewall`
  - can identify normal and abnormal requests : protocol specific attacks
  - can see unencrypted HTTP plaintext data
  - inspect and block, replace, or tag data at L7
  - identify, block, adjust specific applications
    - facebook
- SQL injections, cross-site scripting, geo blacks, rate awareness
- `Web Access Control Lists (WEBACL)`
  - integrated with ALB, API Gateway, CloudFront
  - default action : allow or blockt
  - `waf rules`
    - added to WEBACL, and are evaluated when traffic arrives
    - Type : how it works
      - Regular : if something occurs
      - Rate-Based
    - Statement : whats matched or count
      - criteria : origin country, IP, headers, cookies, http method, url path, query string, body (first `8192` bytes)
      - single, AND, OR, NOT
    - Action : What it does
      - Allow, Block, Count, Captcha
      - custom response
        - block : custom response/header
        - allow/counts/captcha : custom header only
        - customer-header
          - x-amzn-waf
          - means application itself can react to traffic that has been matched
      - `labels`
        - internal to waf
        - can be referenced later in same WEBACL
        - multi-stage flows
        - used with count/captcha 
          - allow/block stop processing
  - `rule groups`
    - contain rules
    - don't have default actions
    - managed by aws or marketplace, you, service (Shield & Firewall Manager)
    - can be referenced by multiple WEBACLs
  - resource type : cloudfront or regional service
  - WEBACL Capacity Units (WCU) 
    - indication of complexity of rules
    - default max 1500
  - adjusting WEBACL takes less time than associating one
  - resource can have on WEBACL which can be associated with many resources
- can use eventbridge scheduled rules + lambda ip list parser to block bad actors
- `logs`
  - can be directed to S3 (5min), cloudwatch logs, or kinesis firehose
  - lambda event driven processing of logs to get insights to automatically update rules
- `pricing`
  - monthly per WEBACL
  - monthly per rule/rule group on WEBACL
  - monthly per million requests per WEBACL
  - bot control monthly and per requests
  - captcha per 1000s
  - fraud control/account takeover per month and logins attempts
  - marketplace rule groups

## CloudHSM

- similar to KMS
- single tenant hardware security module (HSM)
- provisioned by aws
  - aws has no access to parts where keys are stored
- fully customer managed
- Compliance (FIPS)
  - HSM : FIPS 140-2 Level 3
  - KMS : FIPS 140-2 Level 2
- `Integration`
  - HMS : industry standard apis
    - PKCS#11, JCE, CryptoNG
  - KMS : aws standard apis/iam
  - KMS can use CloudHSM as a custom key stor
- architecture
  - deployed into an aws managed vpc
  - runs in 1 AZ
  - HA : create cluster with an HSM in each AZ being used
  - HSM keep keys and policies in sync when nodes are added or removed
  - ENI for each HSM in cluster is injected to customer VPC
  - CloudHSM client is required to communicate with the HSM

- consideration
  - no native aws integration eg) S3
  - can be used to offload SSL/TLS processing for web servers
  - enable transparent data encryption (TDE) for oracle databases
  - protect private keys for an issuing certificate authority

## Config

- `record configuration changes over time on resources`
- auditing of changes, compliance with standards
- does not prevent changes happening
- regional service
- supports cross-region and cross account aggregation
- changes can generate SNS notifications and near-realtime events via EventBridge and Lambda
- stores data in s3 config bucket
- standard
  - configuration of all supported resources are tracked
  - configuration item is created when a change occurs
  - all configuration items for a resource(known configuration history) are stored in s3
- `config rules`
  - `aws managed or custom`
  - evaluates resources against a defined standard
    - resources are compliant or non-compliant
  - custom rules use lambda for evaluation
- can integrate with ssm to fix configuration of instances

## Macie

- data security and data privacy service
- `discover, monitor, and protect data that is stored in s3 buckets`
- automated discovery of data
  - personally identifiable information (`PII`)
  - personal health information (`PHI`)
  - Finance
- `managed data identifiers`
  - built in
  - find almost all common sensitive data
- `custom data identifiers`
  - proprietary
  - regex
  - `keywords` : optional sequences that need to be in proximity to regex match
  - `maximum match distance`
  - `ignore words` : if regex match contains ignore words, it's ignored
- `integration`
  - pass finding events to EventBridge
- `multi-account`
  - via aws orgs or macie account inviting
- `findings`
  - `policy findings`
    - when policy or settings change for s3 bucket that reduces security 
    - after macie is enabled
  - `sensitive data`
  
- `architecture`
  - 1 or more s3 buckets
  - create `discover job` in macie
    - which buckets to analyze
    - `schedule` : when and how frequently it runs
    - use identifiers to look for matches (`findings`) 

## Inspector

- `scans EC2 instance and the instance OS`
  - also containers
- `checks for vulnerabilities and deviations against best practice`
- provides a report of findings ordered by priority
- `network assessment `
  - agentless
- `network & host assessment`
  - uses agent
- `rules packages`
  - determine what is checked
  - `network reachability`
    - checks end-to-end
      - ec2, alb, dx etc.
    - findings
      - RecognizedPortWithListener
      -  RecognizedPortNoListener
      - RecognizedPortNoAgent
      - UnrecognizedPortWithListener
  - `common vulnerabilities and exposures (CVE)`
  - `center for internet security (CIS) benchmarks`
  - `security best practices for amazon inspector`

## Guardduty

- `continuous` security monitoring service
- identify unexpected and unauthorized activities
- can integrated with eventbridge to notify or start event driven protection/remediation
- support multiple accounts
- supports data sources
  - dns logs, vpc flow logs, cloudtrail event logs, cloudtrail management events, cloudtrail s3 data events
