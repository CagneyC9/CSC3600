import hashlib

Shift = 4
Plaintext = "Hello"
print(Plaintext)
for x in Plaintext:
    print("Encrypted: ", chr((ord(x) - 65 + Shift) % 26 + 65))
for x in Plaintext:
    print("Decrypted: ", chr((ord(x) - 65 - Shift) % 26 + 65))

