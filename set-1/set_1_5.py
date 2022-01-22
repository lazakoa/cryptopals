#!/bin/env python

from itertools import repeat
def repeatingKeyXOR(message, key):

    repeatedKey = (key * len(message))[:len(message)]

    enciphered = bytes([a ^ b for a, b in zip(message.encode('ascii'),
        repeatedKey.encode('ascii'))])
    return enciphered

def test_repeatingKeyXOR():
    # used for pytest, might remove later.
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    s = repeatingKeyXOR(message, key)
    target = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    test = s.hex() == target
    assert test
    return test

if __name__ == "__main__":
    print("repeatingKeyXOR: ", test_repeatingKeyXOR())
    
