#! /usr/bin/python3
# Challenge 9 - Implement PKCS#7 padding

def pkcs7(plaintext, block_size):
    remaining = block_size - (len(plaintext) % block_size)
    return plaintext + bytes([remaining] * remaining)

print(pkcs7(b"YELLOW SUBMARINE", 20))


