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

def scoreTest(text):
    "This isn't a very good metric to go by."

    letters = dict()

    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    
    maxvals = sorted(letters.keys(), key=lambda k: letters[k], reverse=True)
    if maxvals[1] == 'e' or maxvals[1] == 'E':
        return True
    if maxvals[1] == 'a' or maxvals[1] == 'A':
        return True
    if maxvals[1] == 'r' or maxvals[1] == 'R':
        return True
    if maxvals[1] == 'i' or maxvals[1] == 'I':
        return True
    if maxvals[1] == 'o' or maxvals[1] == 'O':
        return True

    return False

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
