#!/bin/env python

"""
Set 1: Basics
"""

"""
1. Convert hex to base64
"""
from base64 import b64encode, b64decode

def hexToBase64(hexString):
    # return the bytes, don't convert to a string
    return b64encode(bytes.fromhex(hexString))

def test_hexToBase64():
    value1 = hexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") 

    assert value1 == b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

"""
2. Fixed XOR
"""

def fixedXOR(hexValue, XORtarget):
   return hex(int(hexValue, 16) ^ int(XORtarget, 16))

def test_fixedXOR():
    input1 = '1c0111001f010100061a024b53535009181c'
    input2 = '686974207468652062756c6c277320657965'
    assert fixedXOR(input1, input2) == hex(int('746865206b696420646f6e277420706c6179',16))

"""
3. Single-byte XOR cipher

Single-byte XOR cipher
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
"""
