#! /usr/bin/python3
# Challenge 7 - AES in ECB mode

from Crypto.Cipher import AES
import binascii

with open('7.txt', 'r') as f:
    base64 = ''.join(f.read().split('\n'))
    ciphertext = binascii.a2b_base64(base64)

key = 'YELLOW SUBMARINE'
cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
