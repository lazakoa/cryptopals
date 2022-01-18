#!/bin/env python

frequencies = {
    "a": 0.07743208627550165,
    "b": 0.01402241586697527,
    "c": 0.02665670667329359,
    "d": 0.04920785702311875,
    "e": 0.13464518994079883,
    "f": 0.025036247121552113,
    "g": 0.017007472935972733,
    "h": 0.05719839895067157,
    "i": 0.06294794236928244,
    "j": 0.001267546400727001,
    "k": 0.005084890317533608,
    "l": 0.03706176274237046,
    "m": 0.030277007414117114,
    "n": 0.07125316518982316,
    "o": 0.07380002176297765,
    "p": 0.017513315119093483,
    "q": 0.0009499245648139707,
    "r": 0.06107162078305546,
    "s": 0.061262782073188304,
    "t": 0.08760480785349399,
    "u": 0.030426995503298266,
    "v": 0.01113735085743191,
    "w": 0.02168063124398945,
    "x": 0.0019880774173815607,
    "y": 0.022836421813561863,
    "z": 0.0006293617859758195,
}

def single_byte_xor(text: bytes, key: int) -> bytes:
    """Given a plain text `text` as bytes and an encryption key `key` as a byte
    in range [0, 256) the function encrypts the text by performing
    XOR of all the bytes and the `key` and returns the resultant.
    """
    return bytes([b ^ key for b in text])


def score_text(text: bytes) -> float:
    # lower scores are better
    score = 0.0
    l = len(text)

    for letter, frequency_expected in frequencies.items():
        frequency_actual = text.count(ord(letter)) / l
        err = abs(frequency_expected - frequency_actual)
        score += err

    return score

def singleByteXORpossibleDecoded(string: bytes):
    solutions = []
    for i in range(128):
        possible = (i, single_byte_xor(string, i).decode("ascii"))
        solutions.append(possible) 
    
    return solutions

def singleByteXORcipher(string):
    """
    Cooking MC's like a pound of bacon
    """

    solutions = singleByteXORpossibleDecoded(string)
    solutions = [(x[0], x[1] , score_text(x[1].encode("ascii"))) for x in solutions]
    result = min(solutions, key = lambda x: x[2])
    return result

"""
message = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
print(singleByteXORcipher(message))
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


        try:
            result = singleByteXORcipher(lines[i])
            results.append(result)
        except UnicodeDecodeError:
            pass

    return min(results, key = lambda x: x[2])[1]
