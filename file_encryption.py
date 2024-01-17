# Import Fernet Library

from cryptography.fernet import Fernet

# Load the Symmetric key Stored in Tab 'key_generation'
with open('symKey.key', 'rb') as sym_key:
    symKey = sym_key.read()

# Encryption with Symmetric Key
# Read File to be encrypted, Zipping the folder as one first before encryption
with open('Screenshots.zip', 'rb') as screenshots:
    folder = screenshots.read()

with open('fileSample.txt', 'rb') as fileText:
    file_text = fileText.read()

# Reading the Symmetric Key with Fernet Library
enc_key = Fernet(symKey)

# File Encryption
enc_folder = enc_key.encrypt(folder)
enc_file = enc_key.encrypt(file_text)

# Saving Encrypted Backups using the Symmetric Key
with open('Encrypted Screenshots.zip', 'wb') as enc_screenshots:
    enc_screenshots.write(enc_folder)

with open('Encrypted fileSample.txt', 'wb') as enc_filetext:
    enc_filetext.write(enc_file)
