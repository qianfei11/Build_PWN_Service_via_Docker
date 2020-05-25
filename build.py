#!/usr/bin/env python
import os
import sys

if len(sys.argv) != 3:
    print 'Usage: python', sys.argv[0], '[BIN] [PORT]'
    exit()

binary = sys.argv[1]
port = sys.argv[2]
print '[DEBUG]', binary + ":" + port

os.system("cp ./flag ./env/bin/flag")
os.system("cp {} ./env/bin/vul".format(binary))
os.system("cd env")
os.system('''docker build -t "problem_{}" ./env/'''.format(port))

#cmd = '''nohup docker run -p "0.0.0.0:{}:6999" -h zjgsuctf --name="problem_{}" problem_{} >> problem_{}.log &'''.format(port, port, port, port)
cmd = '''nohup docker run -p "0.0.0.0:{}:9999" -h zjgsuctf --name="problem_{}" problem_{} >> problem_{}.log &'''.format(port, port, port, port)
print '[DEBUG]', cmd
os.system(cmd)
print "======================================"
print "       nc 0.0.0.0 " + port
print "======================================"

