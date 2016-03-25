#! /usr/bin/python3
# Challenge 11 - An ECB/CBC detection oracle

from utils import encrypt_ecb, fixed_xor, decrypt_cbc, chunks
import binascii

def encrypt_cbc(plaintext, key, iv):
    ciphertext = encrypt_ecb(fixed_xor(plaintext[:16], iv), key)
    for block in chunks(plaintext[16:], 16):
        ciphertext_piece = encrypt_ecb(fixed_xor(ciphertext[-8:], block), key)
        ciphertext += ciphertext_piece
    return ciphertext

from random import randint
import os
def encryption_oracle(plaintext):
    padding = b'\x01' * randint(5,10)
    key = os.urandom(16)
    if randint(0,1) == 0: #cbc
        iv = os.urandom(16)
        encrypted = encrypt_cbc(padding + plaintext + padding, key, iv)
        return encrypted, 'cbc'
    else: #ecb
        encrypted = encrypt_ecb(padding + plaintext + padding, key)
        return encrypted, 'ecb'

ciphertext, mode = encryption_oracle(b'A' * 100)
print(ciphertext)
print(mode)
if len(set(chunks(ciphertext, 16))) < len(ciphertext) / 16:
    print('ecb')
else:
    print('cbc')
