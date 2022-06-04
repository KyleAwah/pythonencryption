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
# -------------------------------------------------------- #


# User Input
print("\n")
print("\t\t   Caesar’s Cipher Encryption ")
print("\n")
message = input("Enter The Message to be Encrypted: ")
print("Choose an Encryption Key:")
print("(How many characters between the current letter and the encrypted letter) \n")
key = int(input("Your Key: "))  # User Inputs key and converts it into an int


# Variables & Arrays/Lists For The Program
user_key = key  # stores the original value for the key used by the user
encrypted_message_list = []
encrypted_message = ""
current_number = 0
encrypted_number = 0
count = 0
space_finder = False
encrypted_letter = ""
ASCII =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","~","!","@","#","$","%","^","&","*","(",")","_","+","{","}","|",":",'"',"<",">","?","`","-","=","[","]","\\",";","'",",",".","/"," "]

# If the user enters a key thats bigger than the array then do this
if key > len(ASCII):
    key = key % len(ASCII)

    if key == 0: # if we mod and get the intended key for encryption as 0 then this means no shift
                 # and the message will not be encrypted and so since the intention by the user was for a safer encryption
                 # by using a large number we can make a safe assumption to assign this as the new key
        key = 7
# Loop through the entire message one letter at a time
for letter_in_message in message:
    # If the letter is a space then we just leave it as a space
    if letter_in_message == " ":
        encrypted_letter = " "
        space_finder = True
    # Else if its not a space then we look for the character
    else:
        # Search the ASCII List and match the letter in the message to a character from the ascii table and store its array subscript
        for ASCII_Charater in ASCII:
            count = count + 1  # Counts the current array subscript
            if letter_in_message == ASCII_Charater:
                current_number = count       # Stores the subscript we're at
                break   # Break out of the for loop once the character is matched
    # Only encrypt the ascii charaters if its a charater and not a space
    if space_finder == False:
        # Add the key to encrypt the current letter
        encrypted_number = current_number + key
        # If we reached a number bigger than the size of the array then start from the top
        if encrypted_number > len(ASCII):
            encrypted_number = encrypted_number - len(ASCII)
        encrypted_letter = ASCII[encrypted_number] # The encrypted character is found by taking its position in the array


    encrypted_message_list.append(encrypted_letter) # Adding the new letter unto the end of the list

    # Reseting all valuse for the next letter
    space_finder = False
    count = 0
    encrypted_number = 0
    current_number = 0
    encrypted_letter = " "

    # For Loop ends here and moves unto the next letter in the message the user entered

# Output of Encrypted Message
encrypted_message = "".join(encrypted_message_list)  # joining the list of letters together into a single string

print("\n\n\n")
print("\t\t   Encryption Output \n")
print("The Original Message   : " + message)
print("The Encrypted Message  : " + encrypted_message)
print("Key (Char Offset) Used : " + str(user_key))
print("\n")