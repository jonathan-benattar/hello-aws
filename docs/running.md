# Running the server and client

There are two programs. Both use only Python's standard library, so there's nothing to install.

| File | Runs on | What it does |
| --- | --- | --- |
| `server.py` | EC2 instance | Listens on port 8080 and answers every request with `hello world` |
| `client.py` | your PC | Calls the server and prints the answer |

## Try it on your PC first

Do this before deploying to EC2, to check the code works.

1. Open two terminals in the project folder.
2. In terminal 1, start the server:

   ```bash
   python3 server.py
   ```

   It prints `Listening on 0.0.0.0:8080 (Ctrl+C to stop)`.

3. In terminal 2, run the client against your own machine. `127.0.0.1` means "this computer".

   ```bash
   python3 client.py 127.0.0.1
   ```

   It prints `hello world`.

4. Stop the server with **Ctrl+C** in terminal 1.

## Run it on EC2

1. Push your code to GitHub from your PC:

   ```bash
   git add .
   git commit -m "Describe your change"
   git push
   ```

2. Connect to the instance:

   ```bash
   ssh -i ~/.ssh/hello-aws-key.pem ubuntu@<EC2_PUBLIC_IP>
   ```

3. **On the instance**, get the code.

   The first time, clone the repo:

   ```bash
   git clone https://github.com/jonathan-benattar/hello-aws.git
   cd hello-aws
   ```

   Later times, update the copy you already have:

   ```bash
   cd hello-aws
   git pull
   ```

4. **On the instance**, start the server:

   ```bash
   python3 server.py
   ```

5. **On your PC**, in a new terminal, call it:

   ```bash
   python3 client.py <EC2_PUBLIC_IP>
   ```

   It prints `hello world`.

6. Stop the server with **Ctrl+C** in the SSH terminal.

The server stops when you close the SSH session. That's fine for this project.

## If the client fails

The client waits up to 10 seconds. If it can't reach the server, it prints `Could not reach ...`.

- **`Connection refused`**: nothing is listening on port 8080. Is `server.py` running?
- **`timed out`**: the security group is blocking you. See [troubleshooting.md](troubleshooting.md#ssh-or-the-client-hangs).
