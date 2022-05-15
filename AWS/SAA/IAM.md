## AWS Accounts
An AWS Account container for identities (users) and resources

The `ROOT USER` is created when the account is created.
- has full control over the account and any resources within it
- can't be restricted or deleted

AWS `Multi-Factor Authentication (MFA)` is a simple best practice that adds an extra layer of protection on top of your user name and password.

## Tips when making a new account
- use gmail, `+` to create multiple accounts with different emails all pointing to the same email address.
- enable MFA for root user
- create a budget
- enable iam user and role access to billing

## Identity and Access Management (IAM)
- globally resilient service
- can create other identities
  - `users` : humans or apps that need access to the account
    - a certain number of entities
  - `groups` : collections of related users
  - `roles` : used by `aws services`, or `external access` to  your account
    - for an uncertain number of entities
- `policies` : allow or deny access to aws services when attached to a user, group, or rol
  
Three main jobs...
1. `Manages identities` : an ID provider (`IDP`)
2. `Authenticate` : prove you are who you claim to be
3. `Authorize` : allow or deny access to resources

- No cost
- Global service
- no direct control on external accounts or users
- identity federation

## IAM Access Keys
Long term credentials... -> don't change regularly
- can have two at a time
- can be created, deleted, made inactive or active

Has two parts : `Access Key ID + Secret Access Key`