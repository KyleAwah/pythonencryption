from Crypto.Cipher import AES

key = 'This is a key123'.encode("utf-8")
mode = AES.MODE_CBC
IV = 'This is an IV456'.encode("utf-8")

def pad(message):
    while len(message)%16 != 0:
        message = message + " "
    return message

e_cipher = AES.new(key, AES.MODE_CBC, IV)
d_cipher = AES.new(key, AES.MODE_CBC, IV)

message = 'encrypt this secret message'
padded_message = pad(message)
encrypted_msg = e_cipher.encrypt(padded_message.encode("utf-8"))

print(padded_message)
print(encrypted_msg)

decrypted_msg = d_cipher.decrypt(encrypted_msg)

print(decrypted_msg.rstrip().decode("utf-8"))