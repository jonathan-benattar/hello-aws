# Troubleshooting

## SSH or the client hangs

When `ssh` or `python3 client.py` sits there with no output and eventually times out, the security group is almost always blocking you. Check these in order.

### 1. Your home IP changed

Internet providers change home IP addresses from time to time.

1. Get your current IPv4 address:

   ```bash
   curl -4 ifconfig.me
   ```

2. In the EC2 console, go to **Security Groups** and open the instance's group.
3. Compare the source of both inbound rules (port 22 and port 8080) with that address.
4. If they don't match, update **both** rules to `<your-ip>/32`.

### 2. A rule has an IPv6 address

- Your browser reaches AWS over IPv6. So the console's **"My IP"** option fills in an IPv6 address, something like `2a0d:...`.
- The instance only has IPv4, so a rule with an IPv6 source never matches. Nothing shows an error; SSH just hangs.

To fix it:

1. Delete the IPv6 rule. AWS rejects changing it in place.
2. Add a new rule with the same type and port, and source `<your-ip>/32` from `curl -4 ifconfig.me`.

### 3. The public IP changed

If you stopped and started the instance, it has a new public IP. Get it from the EC2 console (see [ec2-instance.md](ec2-instance.md#public-ip-address)).

## `Permissions 0644 for '...pem' are too open`

SSH refuses keys that other users can read. Fix it with:

```bash
chmod 400 ~/.ssh/hello-aws-key.pem
```

## IAM user can't get a console password

This is expected. See [aws-account.md](aws-account.md#iam-user).
