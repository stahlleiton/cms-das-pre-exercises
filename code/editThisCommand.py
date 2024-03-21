#!/usr/bin/env python3

import sys
import zlib

# Please comment the line below out by adding a '#' to the front of
# the line.
raise RuntimeError("You need to comment out this line with a #")

import getpass
user = getpass.getuser()
crc32 = zlib.crc32(user.encode())

print(f"success:  {user} 0x{crc32:X}")
