#########################################################
#  Kyle Awah
#  816012635
#
#  INFO 2604 - Information Systems Security
#  Final Assignment
#  10th June - 15th June (5 Days)
#
#  PYTHON VERSION - 3
#  DEPENDENCIES (Additional Installs above base python):
#  pycrypto, pycryptodome, pycryptodomex
#
#
#  Question #1
#  Part 1 - Program A1 (Alice's Program)
#
#########################################################


# import Libraries
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
import hashlib
import socket

# open file streams
output_file_PrivateKey = open('private.dat', 'wb')
output_file_PublicKey = open('public.dat', 'wb')

# generate Public & Private Keys
key = RSA.generate(2048)
private_key_seed = key.export_key()
public_key_seed = key.publickey().export_key()

# write the keys to the files
output_file_PrivateKey.write(private_key_seed)
output_file_PublicKey.write(public_key_seed)

# close the file streams
output_file_PublicKey.close()
output_file_PrivateKey.close()

# make keys from seeds
public_key_seed_from_file = RSA.import_key(open("public.dat").read())
public_key = Cipher_PKCS1_v1_5.new(public_key_seed_from_file)

private_key_seed_from_file = RSA.import_key(open("private.dat").read())
private_key = Cipher_PKCS1_v1_5.new(private_key_seed_from_file)

# messages to encrypt
original_message = "testing"
encrypted_message = ""
decrypted_message = ""
original_message = original_message.rstrip("\n")

# actual encrypt/decrypt
encrypted_message = public_key.encrypt(original_message.encode())
decrypted_message = private_key.decrypt(encrypted_message, None).decode()

# output
print("\n")
print("Original Message: ")
print(original_message)
print("\n")
print("Encrypted Message: ")
print(encrypted_message)
print("\n")
print("Decrypted Message: ")
print(decrypted_message)