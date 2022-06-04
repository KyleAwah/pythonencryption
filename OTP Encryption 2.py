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
#  Program 2 (Bob's Program)
#
#  - Receive encrypted message from Alice
#  - Decrypt message using OTP Key
#  - Display Decrypted message
#
# -------------------------------------------------------- #




# ------------------ IMPORT LIBRARIES ------------------- #
import socket
# ------------------------------------------------------- #




# ------------------ FUNCTION DECLARATIONS ------------------ #
# function to convert each binary digit to a letter in a string
def binary_from_convert (binary = None):
    return ''.join([chr(int(bin_digit,2)) for bin_digit in binary])  # goes through the binary digits or items in the list and joins them and loops through them to convert them back into characters

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

# function to decrypt with an OTP
def Decrypt_OTP(encrypted_message, key):
    decrypted_message = []
    current_key_bit = 0
    final_decrypted_message = []
    # loop through each bit in the encrypted message
    for each_encrypted_bit in encrypted_message:
        encrypted_int_bit = int(each_encrypted_bit)                     # convert every bit into an int
        key_int_bit = int(key[current_key_bit])                         # convert every bit into an int
        decrypted_bit = XOR_Logic_Gate(encrypted_int_bit, key_int_bit)  # compares the encrypted bit to the key to find the decrypted bit
        decrypted_message.append(decrypted_bit)                         # add decrypted bit to the list
        current_key_bit += 1
    final_decrypted_message = convert_to_format(decrypted_message)
    return final_decrypted_message
# ------------------------------------------------------- #




# -------- RECIEVE ENCRYPTED MESSAGE FROM ALICE -------- #
print("Waiting to recieve encrypted message from Alice...")
recieved_file = open('protocoloneoutput.dat','wb')
s = socket.socket()
host = socket.gethostname()
port = 8080
s = socket.socket()
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print(host, "Has connected")
print("Transferring Data...")
while True:
    data = conn.recv(1024)
    recieved_file.write(data)
    if not data:
        break
    conn.sendall(data)
conn.close()
recieved_file.close()
print("Encrypted Message Received")
# ------------------------------------------------------- #




# ----- DECRYPT MESSAGE FROM FILE & SAVE ITS BINARY ----- #
with open('protocoloneoutput.dat', 'r') as recieved_file_contents:   # open file and store the encrypted binary form of message from Alice
    for line in recieved_file_contents:
        file_data_string = line

with open('OTPGeneratedKey.dat', 'r') as key_file_contents:   # open file and store the OTP Key
    for line in key_file_contents:
        key_data_string = line

file_data = []
for char in file_data_string:                                 # convert the message from Alice into the binary structure to be decrypted
    current_bit = int(char)
    file_data.append(current_bit)

key_data = []
for char in key_data_string:                                  # convert the OTP Key into the binary structure to be used in the decryption of Alice's Message
    current_key_bit = int(char)
    key_data.append(current_key_bit)

decrypted_binary = Decrypt_OTP(file_data, key_data)           # Decrypt the binary message from Alice

with open('LetterBinary.dat', 'w') as decrypted_binary_write: # Save the decrypted binary to the file
    for line in decrypted_binary:
        decrypted_binary_write.write(line)
# ------------------------------------------------------- #




# ----------- CONVERT BINARY & SAVE TO FILE ------------ #
with open('LetterBinary.dat', 'r') as decrypted_binary:              # get the decrypted data from the file
    for line in decrypted_binary:
        decrypted_from_file = line

decrypted_data = []
for char in decrypted_from_file:                                      # convert the decrypted message into the binary structure to be converted into characters
    current_key_bit = int(char)
    decrypted_data.append(current_key_bit)

final_binary_format = convert_to_format(decrypted_data)
decrypted_message = binary_from_convert(final_binary_format)

with open('ASCII_character_file.txt', 'w') as saving_actual_message:  # saving the final ascii text
    saving_actual_message.write(decrypted_message)
# ------------------------------------------------------- #




# -------- DISPLAY DECRYPTED MESSAGE FROM ALICE --------- #
print("\n")
print("Message From Alice: ")
with open('ASCII_character_file.txt', 'r') as actual_message:  # getting the decrypted message from the file
    for line in actual_message:
        print(line)
print("\n")
# ------------------------------------------------------- #