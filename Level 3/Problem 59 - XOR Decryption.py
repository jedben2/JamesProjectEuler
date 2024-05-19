# Problem 59 - XOR Decryption

# This one was pain. The message is encoded by a 3 letter key so that every ith letter is encoded by the i % 3th letter of the key.
# We can find the correct key by making sure that all the chars decoded are not gibberish characters (see the GOOD var. for the acceptable chars)

import string
from itertools import cycle

good = string.ascii_letters + string.digits + " .,:;+?!/[]()'\""
print(good)

with open("0059_cipher.txt", "r") as f:
    text = [int(i) for i in f.read().split(",")]

def keys(chunk):
    keys = []
    for c in string.ascii_lowercase:
        decoded = set([chr(char ^ ord(c)) for char in chunk])
        if all(c in good for c in decoded):
            keys.append(c)
    return keys[0]
key = [keys(text[i::3]) for i in range(3)]
textdecoded = [text[i] ^ ord(key[i % 3]) for i in range(len(text))]
print(''.join([chr(c) for c in textdecoded]))
print(sum(textdecoded))