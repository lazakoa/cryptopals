#!/bin/env python

def fixedXOR(hexValue, XORtarget):
   return hex(int(hexValue, 16) ^ int(XORtarget, 16))

def test_fixedXOR():
    input1 = '1c0111001f010100061a024b53535009181c'
    input2 = '686974207468652062756c6c277320657965'
    print("fixedXor: ",  fixedXOR(input1, input2) == hex(int('746865206b696420646f6e277420706c6179',16)))


