#!/usr/bin/env python3

import sys
import zlib


if len(sys.argv) < 2:
    print("Error: You must provide the secret key")
    sys.exit()

key = ''.join(sys.argv[1:]).encode()
crc32 = zlib.crc32(key)

key = b'asdf;klasdjf;kakjsdf;akjf;aksdljf;asldjfqewradsfafaw4efaefawefzdxffasdfw4ffawefawe4fawasdffadsfef'

if crc32 != zlib.crc32 (key):
    print("Error: You didn't paste the correct input string")
    sys.exit()

import getpass
user = getpass.getuser()
other = ''
for letter in user:
    number = ord (letter)
    if 65 <= number <= 77 or 97 <= number <= 109:
        number += 13
    elif 78 <= number <= 90 or 110 <= number <= 122:
        number -= 13
    other += chr (number)
print(f"success: {user} {other}")
