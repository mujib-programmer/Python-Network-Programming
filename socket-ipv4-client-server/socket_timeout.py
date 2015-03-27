#!/usr/bin/env python
# This program is optimized for Python 2.7. It may run on any
# other Python version with/without modifications

"""
Sometimes, you need to manipulate the default values of certain properties of a socket
library, for example, the socket timeout.
"""

import socket

"""
You can make an instance of a socket object and call a gettimeout() method to get the
default timeout value and the settimeout() method to set a specific timeout value. This is
very useful in developing custom server applications.

We first create a socket object inside a test_socket_timeout() function. Then, we can
use the getter/setter instance methods to manipulate timeout values.
"""
def test_socket_timeout():

    """
    In this code snippet, we have first created a socket object by passing the socket family and
    socket type as the first and second arguments of the socket constructor. Then, you can
    get the socket timeout value by calling gettimeout() and alter the value by calling the
    settimeout() method. The timeout value passed to the settimeout() method can be in
    seconds (non-negative float) or None . This method is used for manipulating the blocking-socket
    operations. Setting a timeout of None disables timeouts on socket operations.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Default socket timeout: %s" %s.gettimeout()
    s.settimeout(100)
    print "Current socket timeout: %s" %s.gettimeout()

if __name__ == '__main__':
    test_socket_timeout()