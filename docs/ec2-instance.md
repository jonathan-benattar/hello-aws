# EC2 instance

## Settings

| Setting | Value |
| --- | --- |
| Region | eu-north-1 (Stockholm) |
| Name | hello-aws |
| Instance type | t3.micro |
| Operating system | Ubuntu Server LTS (x86) |
| Disk | 8 GiB gp3 |

## Public IP address

The instance's public IP **changes every time you stop and start it**.

To find the current one, open the EC2 console, go to **Instances**, select `hello-aws`, and read **Public IPv4 address**.

## Security group (firewall) rules

Inbound rules, IPv4 only:

| Type | Port | Source |
| --- | --- | --- |
| SSH | 22 | your home IP `/32` |
| Custom TCP | 8080 | your home IP `/32` |

- `/32` means "this one address only".
- Port 8080 is where `server.py` listens.

**Don't use the console's "My IP" button.** It often fills in an IPv6 address, which doesn't work here. See [troubleshooting.md](troubleshooting.md#ssh-or-the-client-hangs).

Get your home IPv4 address from your PC's terminal instead:

```bash
curl -4 ifconfig.me
```

## SSH key

- The private key is at `~/.ssh/hello-aws-key.pem` (ED25519).
- Its permissions must be read-only for you, or SSH refuses to use it:

  ```bash
  chmod 400 ~/.ssh/hello-aws-key.pem
  ```

- Never commit `.pem` files. `.gitignore` excludes `*.pem`.

## Connecting

Replace `<EC2_PUBLIC_IP>` with the address from the console:

```bash
ssh -i ~/.ssh/hello-aws-key.pem ubuntu@<EC2_PUBLIC_IP>
```

## Saving credits

A running t3.micro uses credits. When you're not working on the project, stop the instance: EC2 console → select it → **Instance state → Stop instance**.

- The disk keeps your files while the instance is stopped.
- The public IP will be different when you start it again.
