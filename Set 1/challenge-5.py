#! /usr/bin/python
# Challenge 5 - Implement repeating-key XOR

import binascii
from utils import fixed_xor

from itertools import cycle
def repeating_xor(plaintext, key):
	return fixed_xor(plaintext, cycle(key))

plaintext = b'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
key = b'ICE'

ciphertext  = repeating_xor(plaintext, key)

print(binascii.b2a_hex(ciphertext))
