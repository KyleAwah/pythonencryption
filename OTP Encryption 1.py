# ------------------ DEVELOPER INFORMATION ------------------ #
#
#  Name:           Kyle Awah
#
#
# ---------------- ENVIRONMENT INFORMATION ---------------- #
#
#  PYTHON VERSION - 3.8
#  DEPENDENCIES   - NONE
#
# ----------------- PROGRAM INFORMATION ------------------ #
#
#  Program 1 (Alice's Program)
#
#  - Import Letter.dat and convert it to binary
#  - Create an OTP KEY
#  - Encrypt with OTP
#  - Send Encrypted Message to bob
#
# -------------------------------------------------------- #




# ------------------ IMPORT LIBRARIES ------------------- #
import socket
import random
# ------------------------------------------------------- #




# ------------------ FUNCTION DECLARATIONS ------------------ #
# function to convert each letter in a string to binary
def binary_to_convert (string = ""):
    return [bin(ord(letter)) [2:].zfill(8) for letter in string]    # goes through each letter of the string and uses .zfill to pad the binary conversion with extra 0's if it does not make up 8 digits

# function to simulate an XOR Logic Gate
def XOR_Logic_Gate (num_a, num_b):
    if num_a == 0 and num_b == 0:
        return int(0)
    elif num_a == 1 and num_b == 0:
        return int(1)
    elif num_a == 0 and num_b == 1:
        return int(1)
    elif num_a == 1 and num_b == 1:
        return int(0)

# function to convert finished encrypted messages or decrypted messages into 8 bit sections for binary conversion into characters
def convert_to_format (message):
    final_message = []
    count_to_8 = 0
    letter = []
    for bit in message:
        if count_to_8 == 8:
            count_to_8 = 0                                              # reset the counter to find each 8 bit pairing
            string_letter_in_bits = ''.join(letter)                     # join the list into a single string
            letter = []                                                 # reset letter list
            final_message.append(string_letter_in_bits)                 # add the letter into the decrypted string
        current_bit = str(bit)                                          # converting back into string from int for each bit
        letter.append(current_bit)                                      # adding on this bit to a letter
        count_to_8 += 1                                                 # increase the counter so we will know when we have reached 8 bits
    # add on the last letter which is only delivered after the loop is finished executing
    string_letter_in_bits = ''.join(letter)                             # join the list into a single string
    final_message.append(string_letter_in_bits)                         # add the letter into the decrypted string
    return final_message

# function to encrypt with an OTP
def Encrypt_OTP(plaintext, key):
    encrypted_message = []
    current_key_bit = 0
    final_encrypted_message = []
    # loop through each bit in the plain text
    for each_plaintext_bit in plaintext[0]:
        plaintext_int_bit = int(each_plaintext_bit)                     # convert every bit into an int
        key_int_bit = int(key[0][current_key_bit])                      # convert every bit into an int
        encrypted_bit = XOR_Logic_Gate(plaintext_int_bit, key_int_bit)  # compares the plain text bit to the key bit find the new encrypted bit
        encrypted_message.append(encrypted_bit)                         # add encrypted bit to the list
        current_key_bit += 1
    final_encrypted_message = convert_to_format(encrypted_message)
    return final_encrypted_message
# ------------------------------------------------------- #




# ------------------ GENERATE OTP KEY ------------------ #
OTP_Key = []
for loop_a_bunch_of_times in range (0, 1000):                      # Generate 1000 random bits as the OTP Key
    value = random.randint(0, 1)
    value_string = str(value)
    OTP_Key.append(value_string)

with open('OTPGeneratedKey.dat', 'w') as writing_OTP_key_to_file:  # open new OTPGeneratedKey.dat file and store the newly generated OTP Key
    for line in OTP_Key:
        writing_OTP_key_to_file.write(line)
# ------------------------------------------------------- #




# --------------- CONVERT FILE TO BINARY ----------------- #
with open('Letter.dat', 'r') as reading_letter:              # open Letter.dat file and convert it into binary and store it in a variable
    for line in reading_letter:
        file_in_binary = binary_to_convert(line)

with open('LetterBinary.dat', 'w') as writing_binary_to_file: # open new LetterBinary.dat file and store the converted binary
    for line in file_in_binary:
        writing_binary_to_file.write(line)
# ------------------------------------------------------- #




# ----------- ENCRYPT WITH OTP & SAVE TO FILE ----------- #
letter_in_binary = []
with open('LetterBinary.dat', 'r') as read_binary:                   # read binary from file and store it
    for line in read_binary:
        letter_in_binary.append(line)

OTP_Key_imported = []
with open('OTPGeneratedKey.dat', 'r') as OTP_Key_from_file:          # read OTP key from file and store it
    for line in OTP_Key_from_file:
        OTP_Key_imported.append(line)

encrypted_message = Encrypt_OTP(letter_in_binary, OTP_Key_imported)  # calls function to encrypt message

with open('protocoloneoutput.dat', 'w') as encrypted_message_for_bob: # saves encrypted message to file
    for line in encrypted_message:
        encrypted_message_for_bob.write(line)
# ------------------------------------------------------- #




# ------------ SEND ENCRYPTED MESSAGE TO BOB ------------ #
print("\n")
print("Transferring Encrypted Message...")
send_file = open('protocoloneoutput.dat','rb')
file_data_to_send = send_file.read()
host = socket.gethostname()
conn = socket.socket()
port = 8080
conn.connect((host, port))
conn.sendall(file_data_to_send)
data = conn.recv(1024)
conn.close()
send_file.close()
print("Message sent to Bob safely & successfully using One Time Pass (OTP) Encryption!")
print("\n")
# ------------------------------------------------------- #