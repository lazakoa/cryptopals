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

def single_byte_xor(text: bytes, key: int) -> bytes:
    """Given a plain text `text` as bytes and an encryption key `key` as a byte
    in range [0, 256) the function encrypts the text by performing
    XOR of all the bytes and the `key` and returns the resultant.
    """
    return bytes([b ^ key for b in text])

def singleByteXORpossibleDecoded(string):
    solutions = []
    for i in range(128):
        possible = single_byte_xor(bytes.fromhex(string), i)
        possible = possible.decode("ascii")
        solutions.append(possible) 
    
    return solutions

def singleByteXORcipher(string):
    """
    Cooking MC's like a pound of bacon
    """

    import spacy
    from spacy.language import Language
    from spacy_langdetect import LanguageDetector
  
    def get_lang_detector(nlp, name):
        return LanguageDetector()

    nlp = spacy.load("en_core_web_sm")
    Language.factory("language_detector", func=get_lang_detector)
    nlp.add_pipe('language_detector', last=True)

    solutions = singleByteXORpossibleDecoded(string)

    for solution in solutions:
        sentence = nlp(solution)
        lang = sentence._.language
        if lang['language'] == 'en':
            print(sentence)

"""
cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
singleByteXORcipher(cipher) 
"""

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
    
    original = dict()
    for i in range(len(lines)):
        original[i] = lines[i]
        print("BEGIN: ", i)
        try:
            singleByteXORcipher(lines[i])
        except UnicodeDecodeError:
            # just skip everthing that throws this and see if we get the answer
            # yeah it works
            pass
        print("END: ", i)
        
"""
detectSingleCharacterXOR()
"""

"""
5.Implement repeating-key XOR
Here is the opening stanza of an important work of the English language:

{{{
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
}}}

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

It should come out to:

{{{
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
}}}

Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this. 
"""

"""
def zip_with_scalar(l, o):
    return zip(l, itertools.repeat(o))
"""

from itertools import repeat
def repeatingKeyXOR(message, key):

    repeatedKey = (key * len(message))[:len(message)] 

    enciphered = bytes([a ^ b for a, b in zip(message.encode('ascii'), 
        repeatedKey.encode('ascii'))])
    return enciphered

def test_repeatingKeyXOR():
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    s = repeatingKeyXOR(message, key)
    target = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    assert s.hex() == target

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

from collections import OrderedDict
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
    
    print(min(keysDict, key=keysDict.get))
    return min(keysDict, key=keysDict.get)
    #print({k: v for k, v in sorted(keysDict.items(), key=lambda item: item[1])})
    # 5, 3, 2, 13, 11, try 5

import base64
from scorer import singleByteXORcipher
def set1challenge6():
    data = open("resources/cryptopals-set-1-6.txt", "r").read()[:-1]
    message_decoded = base64.b64decode(data)
   
    transposed = transpose(message_decoded, breakingRepeatingKeyXOR(message_decoded))
   
    ans = dict()
    for key in transposed.keys():
        transposed_message = bytes(transposed[key])
        deciphered = singleByteXORcipher(transposed_message.decode("ascii"))
        print(deciphered)
        ans[key] = deciphered[chr(deciphered[0])]

    print(ans)  

def transpose(message, n):
    # takes bytes, it actually doesn't matter if the last chunk is not used, we have enough
    chunky = list(chunks(message, n)) 
    transposed = dict()    

    last = []

    # incase message % len(n) != 0
    if len(chunky[-1]) != n:
        last = chunky.pop()
        
    for chunk in chunky:
        for i in range(len(chunk)):
            if chunk[i] != 0:
                if i in transposed:
                    transposed[i].append(chunk[i])
                else:
                    transposed[i] = [chunk[i]]

    for i in range(len(last)):
        if last[i] != 0:
            if i in transposed:
                transposed[i].append(chunk[i])
            else:
                transposed[i] = [last[i]]

    return transposed

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

set1challenge6()
