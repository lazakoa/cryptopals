#!/bin/env python
from base64 import b64encode, b64decode

"""
1. Convert hex to base64
"""

def hexToBase64(hexString):
    # return the bytes, don't convert to a string
    return b64encode(bytes.fromhex(hexString))

if __name__ == "__main__":
    value1 = hexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") 
    print("hexToBase64: ", value1 == b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


