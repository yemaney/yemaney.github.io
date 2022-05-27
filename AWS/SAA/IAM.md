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

## IAM Policies
Attached to AWS identities and either ALLOW or DENY access to AWS resources.

Comprised of one or more statements that define what actions to allow and deny a resource.

- `Sid`: (statement id), used to help reader what a statement does
- `Effect` : what happens when the `action` and `resource` match the policy
- `Action` : One or more actions the policy is concerned with
- `Resource` : One or more resources the policy is concerned with

Statements with `DENY` effect are given priority over `ALLOW`.
The default effect is `DENY`.

Inline vs Managed Policy
- inline policies are created by adding a policy to an individual identity or resource
  - used for specific or exceptional allows or denies
- managed policies are created on their own and then attached to one or more entities
  - reusable, low overhead
  - should be used for the normal default operational rights ina business

## IAM Users
An identity used for `long term aws access`
- humans, applications, or service accounts

`Principle` : An entity trying to access an aws account
- person or application, needs to authenticate against an identity within an IAM
- authentication is done with either `username: password` or `access keys`
- once an identity is authenticated, then aws knows which policies apply to it to authorize it

`authentication` : proving identity
`authorization` : checking which statements apply to the identity

Limits
- max `5,000` users per account
- user can be a part of a max `10` groups

## Amazon Resource Name
Used to uniquely identify resources within any aws accounts.
- used in policies to define the resources a statement is about

```
arn:aws:s3:::bucket     # refers to the bucket
arn:aws:s3:::bucket/*   # refers to every object within the bucket, but not the bucket
```

## IAM Groups
Containers for IAM Users. 
- used to organize large sets of IAM Users.
- not real identities, 
  - no credentials 
  - can't be used to log in or in resource policies
  - can't be referenced as a principal in a policy
- can have both inline and managed policies attached
- no nesting of groups
- `300` groups per account
