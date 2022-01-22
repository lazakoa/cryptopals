#!/bin/env python

from set_1_3 import singleByteXORcipher

"""
4. Detect single-character XOR

One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""

def detectSingleCharacterXOR():
    """ 
    170: Now that the party is jumping
    """
    f = open("resources/cryptopals-set-1-4.txt", "r")
    lines = []
    for line in f:
        lines.append(line.strip())
    f.close()
     
    results = []
    for i in range(len(lines)):
        result = singleByteXORcipher(lines[i])
        results.append(result) 

    return min(results, key=lambda x: x[2])

if __name__ == "__main__":
    print(detectSingleCharacterXOR()[1].decode("ascii"))

