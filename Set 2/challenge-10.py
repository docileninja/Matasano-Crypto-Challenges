#! /usr/bin/python3
# Challenge 10 - Implement CBC Mode

from utils import decrypt_ecb, fixed_xor
import binascii

def decrypt_cbc(ciphertext, key, iv):
    stream = decrypt_ecb(ciphertext, key)
    return fixed_xor(iv + ciphertext, stream)

with open('10.txt', 'r') as f:
    ciphertext = ''.join(f.read().split('\n'))
    ciphertext = binascii.a2b_base64(ciphertext)

plaintext = decrypt_cbc(ciphertext, b'YELLOW SUBMARINE', b'\x00' * 16)
print(plaintext)
