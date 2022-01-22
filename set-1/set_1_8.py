#!/bin/env python

"""
Detect the ECB being used.
"""

def chunkify(message):
    import math
    chunks = []

    for i in range(10):
        chunks.append(message[i*16:(i+1)*16])
    return chunks


def readFile(path):
    lines = open(path, "r")
    data = [] # length of the data is 160, max is 160
    for line in lines:
        string = bytes.fromhex(line.strip())
        data.append(string)

    return data

# the output of this is the aes ECB cipher text
def analyze_for_ECB():
    data = readFile("resources/cryptopals-set-1-8.txt")
    data = list(map(chunkify, data))
    solutions = list()
    for i in range(len(data)):
        seen = set()
        for chunk in data[i]:
            if chunk not in seen:
                seen.add(chunk)
            else:
                solutions.append((i, data[i]))


    return solutions[0][0]

print(analyze_for_ECB()) # 132
