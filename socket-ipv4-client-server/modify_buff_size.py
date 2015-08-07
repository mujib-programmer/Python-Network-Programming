#!/usr/bin/env python
# Python Network Programming Cookbook Chapter 1
# This program is optimized for Python 2.7. It may run on any
# other Python version with/without modifications

import socket

"""
First, define two constants: SEND_BUF_SIZE / RECV_BUF_SIZE and then wrap a socket
instance's call to the setsockopt() method in a function. It is also a good idea to check the
value of the buffer size before modifying it. Note that we need to set up the send and receive
buffer size separately.
"""
SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    
    # Get the size of the socket's send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [Before]:%d" %bufsize

    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_BUF_SIZE)
    
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_BUF_SIZE)
    
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [After]:%d" %bufsize

"""
If you run the preceding script, it will show the changes in the socket's buffer size. The following
output may be different on your machine depending on your operating system's local settings:
$ python modify_buff_size.py
Buffer size [Before]:16384
Buffer size [After]:8192
"""
if __name__ == '__main__':
    modify_buff_size()