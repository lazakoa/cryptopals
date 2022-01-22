#!/bin/env python
from set_1_5 import repeatingKeyXOR

def hammingDistance(str1, str2):
    # we can always default to from scipy.spatial.distance import hamming 
    # https://stackoverflow.com/questions/26122368/inaccurate-hamming-distance-of-two-strings-in-binary
    bytes1 = str1.encode("ascii")
    bytes2 = str2.encode("ascii")
    return sum(bin(i^j).count("1") for i,j in zip(bytes1, bytes2))

def hammingDistance2(str1, str2):
    num1 = int(str1.encode("ascii").hex(), 16)
    num2 = int(str2.encode("ascii").hex(), 16)
    xor = num1 ^ num2
    return bin(xor).count("1")


def test_hammingDistance():
    # sanity check for our hamming distance function
    message1 = "this is a test"
    message2 = "wokka wokka!!!"
    assert hammingDistance(message1, message2) == 37

def test_hammingDistance2():
    # sanity check for our hamming distance function
    message1 = "this is a test"
    message2 = "wokka wokka!!!"
    assert hammingDistance2(message1, message2) == 37

def breakingRepeatingKeyXOR(message_bytes):
    import itertools
    keysDict = dict()
    for KEYSIZE in range(2,41):
        array1 = message_bytes[:KEYSIZE]
        array2 = message_bytes[2*KEYSIZE:3*KEYSIZE]
        array3 = message_bytes[4*KEYSIZE:5*KEYSIZE]
        array4 = message_bytes[10*KEYSIZE:11*KEYSIZE]
    
        array_of_snippets = [array1, array2, array3, array4]
        to_average = []
        combinations = list(itertools.combinations(array_of_snippets, 2))

        for combination in combinations:
            distance = hammingDistance2(
                    combination[0].decode("ascii"), 
                    combination[1].decode("ascii"))

            to_average.append(distance / KEYSIZE)

        keysDict[KEYSIZE] = sum(to_average)/len(to_average)
    
    return min(keysDict, key=keysDict.get) # 29
    #print({k: v for k, v in sorted(keysDict.items(), key=lambda item: item[1])})

def set1challenge6():
    from scorer import singleByteXORcipher
    import base64

    data = open("resources/cryptopals-set-1-6.txt", "r").read()[:-1]
    message_decoded = base64.b64decode(data)
    transposed = transpose(message_decoded, breakingRepeatingKeyXOR(message_decoded))
   
    ans = dict()
    for i in range(len(transposed)):
        transposed_message = bytes(transposed[i])
        deciphered = singleByteXORcipher(transposed_message)
        ans[i] = chr(deciphered[0])
    
    from collections import OrderedDict
    cipher_key = ""
    ordered = OrderedDict(ans)
    for key in OrderedDict(ans):
        cipher_key += ordered[key]


    return repeatingKeyXOR(message_decoded.decode("ascii"), cipher_key).decode("ascii")

def transpose(message: bytes, n: int):
    # takes bytes, it actually doesn't matter if the last chunk is not used, we have enough
    chunks = []
    for i in range(n):
        chunks.append(message[i::n])

    return chunks

if __name__ == "__main__":
    print(set1challenge6())
