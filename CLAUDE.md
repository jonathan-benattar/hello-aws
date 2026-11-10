hello-aws

A learning project: a minimal "hello world" client/server. The server runs on an AWS EC2 instance; the client runs on my Linux PC and calls it over HTTP. Code lives in a GitHub repo.

The developer is new to git, GitHub and AWS. Explain steps clearly, give exact commands, and avoid anything that could cost money.

Code
server.py — runs on EC2. Python standard library only (http.server). Listens on 0.0.0.0:8080, answers GET with hello world.
client.py — runs on the PC. Python standard library only (urllib). Usage: python3 client.py <EC2_PUBLIC_IP>.
.gitignore — must exclude *.pem and __pycache__/. Never commit keys or credentials.

Keep dependencies at zero unless there's a clear reason; the EC2 machine is a fresh Ubuntu install.

Docs
docs/ holds the developer's guides: README.md (index), aws-account.md, ec2-instance.md, running.md, troubleshooting.md.
Keep docs/ up to date without being asked. In the same change, update the matching doc whenever:
- code, usage, ports or dependencies change (running.md)
- AWS account, IAM, budget or CLI setup changes (aws-account.md)
- instance settings, security group rules or SSH setup change (ec2-instance.md)
- a new problem is solved, or a fix is found (troubleshooting.md)
Add a new doc (and list it in docs/README.md) when a topic doesn't fit an existing one. Write for a beginner, with exact commands. The repo is public: never put IPs, account IDs, keys or credentials in docs/; use placeholders like <EC2_PUBLIC_IP>. Tell the developer which docs were updated.

Local environment
Linux PC, VS Code with the Python and Claude Code extensions.
SSH key: ~/.ssh/hello-aws-key.pem (ED25519, chmod 400).
Connect: ssh -i ~/.ssh/hello-aws-key.pem ubuntu@<EC2_PUBLIC_IP>
Git and GitHub: installed and set up with gh auth login (HTTPS). Repo is public so EC2 can clone without credentials.
AWS setup
Account is on the Free plan ($100 credits). It cannot be charged, but using up the credits or reaching 6 months closes the account. Protect the credits.
Do not enable AWS Organizations or IAM Identity Center: that upgrades the account to Paid and voids the Free Tier credits.
The account sits under an AWS-managed organization whose service control policy blocks console passwords for IAM users (iam:CreateLoginProfile is denied). Console work is done with the account's normal sign-in (a full-access role), protected by MFA.
An IAM user exists with a custom policy, intended for future CLI access keys:
EC2 only, region eu-north-1 only
Instance types limited to t3.micro / t4g.micro
EBS volumes limited to 30 GiB
A budget alert is set up in AWS Budgets.
EC2 instance
Region: eu-north-1 (Stockholm)
Name: hello-aws, type t3.micro, Ubuntu Server LTS (x86), 8 GiB gp3
Public IP: changes whenever the instance is stopped and started; ask the developer or check the EC2 console. Don't record it in the repo (it's public).
Security group inbound rules (IPv4 only):
SSH, port 22, from my home IP /32
Custom TCP, port 8080, from my home IP /32
Known gotcha: "My IP" picks IPv6

The browser reaches AWS over IPv6, so the console's "My IP" option fills in an IPv6 address. The instance only has IPv4, so SSH then silently hangs. Always get the IP from the PC's terminal instead:

bash
curl -4 ifconfig.me

Then use it as <ip>/32. To change an IPv6 rule to IPv4, delete the rule and add a new one (editing it in place is rejected).

If SSH or the client hangs, first suspect a changed home IP and update both rules.

Status
 AWS account, budget, MFA, IAM user with custom policy
 EC2 instance launched and SSH working