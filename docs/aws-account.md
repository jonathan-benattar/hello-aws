# AWS account

## Plan

The account is on the **Free plan** with $100 in credits.

- It can't be charged money.
- The account closes when the credits run out or after 6 months, whichever comes first.
- So protect the credits: stop or terminate anything you're not using.

## Things you must NOT enable

Turning on either of these upgrades the account to the Paid plan and you lose the Free Tier credits:

- **AWS Organizations**
- **IAM Identity Center**

## Budget

A budget alert is set up in **AWS Budgets** (console → Billing and Cost Management → Budgets). It emails you when spending approaches the limit.

## Signing in to the console

- Use the account's normal sign-in. It gives you a full-access role.
- MFA (multi-factor authentication) is turned on for it.

## IAM user

An IAM user exists for future command-line (CLI) access with access keys.

**It can't sign in to the console.** The account belongs to an AWS-managed organization. That organization's service control policy denies `iam:CreateLoginProfile`, which is the permission that gives an IAM user a console password. This is expected, not a mistake.

Its custom policy allows only:

- **EC2**, nothing else
- Region **eu-north-1** (Stockholm) only
- Instance types **t3.micro** and **t4g.micro** only
- EBS volumes up to **30 GiB**

These limits mean that even if the user's keys leaked, nobody could launch expensive machines with them.

## AWS CLI on the PC

- The AWS CLI v2 is installed in `~/.local/bin`.
- `~/.aws/config` has a profile called `hello-aws` with region `eu-north-1`.
- No credentials are set up yet.

When you're ready to use the IAM user from the command line:

1. Create an access key for the user in the console: IAM → Users → the user → Security credentials → Create access key.
2. Enter the key on your PC:

   ```bash
   aws configure --profile hello-aws
   ```

3. Check that it works:

   ```bash
   aws ec2 describe-instances --profile hello-aws
   ```

Never commit access keys to git.

## Not set up: AWS Agent Toolkit

The AWS Agent Toolkit lets AI coding assistants act on the AWS account directly. It was skipped for now:

- It needs a console sign-in, which the IAM user can't have.
- It runs in us-east-1, which the IAM user's policy blocks.
- This project doesn't need it.
