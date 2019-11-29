# Build PWN Service via Docker

> A docker repository for deploying CTF PWN challenges.

## Configuration

Put files to current floder. They'll be copied to /home/ctf. **Update the flag** at the same time.

You can edit `ctf.xinetd, Dockerfile, ctf.xinetd, start.sh` to custom your environment.

## Build & Run

```bash
python build.py [BIN] [PORT]
# python build.py backdoor 10002
```

DO NOT use *bin* as challenge's name

## Capture traffic

If you want to capture challenge traffic, just run `tcpdump` on the host. Here is an example.

```bash
tcpdump -w helloworld.pcap -i eth0 port pub_port
```

`pub_port` is the port you want to expose to the public network.

