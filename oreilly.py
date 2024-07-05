import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = os.urandom(32)
iv = os.urandom(16)

message = b"a secret message"

algorithm = algorithms.AES(key)
cipher = Cipher(algorithm, mode=modes.ECB())

encryptor = cipher.encryptor()
ct = encryptor.update(message) + encryptor.finalize()
decryptor = cipher.decryptor()
pt = decryptor.update(ct) + decryptor.finalize()
print(pt)

message = "a secret message"
bits = len(message.encode()) * 8
print(bits)

message = "a secret message"
encoded_message = message.encode('utf-8')
print(encoded_message)

