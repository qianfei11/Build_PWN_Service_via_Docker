# ctf_xinetd

> A docker repository for deploying CTF challenges

## Configuration

Put files to floder `bin`. They'll be copied to /home/ctf. **Update the flag** at the same time.

Edit `ctf.xinetd`. replace `./helloworld` to your command.

You can also edit `Dockerfile, ctf.xinetd, start.sh` to custom your environment.

## Build

```bash
docker build -t "helloworld" .
```

DO NOT use *bin* as challenge's name

## Run

```bash
docker run -d -p "0.0.0.0:pub_port:9999" -h "helloworld" --name="helloworld" helloworld
```

`pub_port` is the port you want to expose to the public network.

## Capture traffic

If you want to capture challenge traffic, just run `tcpdump` on the host. Here is an example.

```bash
tcpdump -w helloworld.pcap -i eth0 port pub_port
```

## PS

In Ubuntu 20.04, `/lib*` are soft link files to `/usr/lib*` (Specific Dockerfile see `Dockerfile.U20`):

```bash
$ ls -l /
total 48
lrwxrwxrwx   1 root root    7 Apr 23 19:06 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15 19:09 boot
drwxr-xr-x  10 root root 2920 May 16 09:29 dev
drwxr-xr-x   1 root root 4096 May 16 09:29 etc
drwxr-xr-x   1 root root 4096 May 16 09:30 home
lrwxrwxrwx   1 root root    7 Apr 23 19:06 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Apr 23 19:06 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Apr 23 19:06 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Apr 23 19:06 libx32 -> usr/libx32
...
```
