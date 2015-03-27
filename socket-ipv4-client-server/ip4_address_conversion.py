#!/usr/bin/env python
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

import socket

from binascii import hexlify

"""
the two IP addresses have been converted from a string to a 32-bit packed
format using a for-in statement. inet_aton() and inet_ntoa() will be used for the IP address conversion.
Additionally, the Python hexlify function is called from
the binascii module. This helps to represent the binary data in a hexadecimal format.
"""
def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)

        print "IP Address: %s => Packed: %s, Unpacked: %s" \
              %(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)

if __name__ == '__main__':
    convert_ip4_address()