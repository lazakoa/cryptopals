#!/bin/env python 

from Crypto.Cipher import AES # pip install pycryptodome
import base64

def readBytes(path):
    data = open(path, 'r').read() # possibly needs a [::-1] to remove the trailing newline
    return base64.b64decode(data)

key = "YELLOW SUBMARINE"

cipher = AES.new(key.encode("ascii"), AES.MODE_ECB)
plaintext64 = cipher.decrypt(readBytes("resources/cryptopals-set-1-7.txt"))
plaintext = plaintext64.decode("ascii")
print(plaintext)
