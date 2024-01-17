# Decrypting the files using the Decrypted Key
# Import Fernet
from cryptography.fernet import Fernet
# Load the Encrypted Backups
with open('Encrypted Screenshots.zip', 'rb') as encZip:
    enc_zip = encZip.read()

with open('Encrypted fileSample.txt', 'rb') as encFile:
    enc_file = encFile.read()

# Load the Decrypted Symemetric Key
with open('Decrypted SymmetricKey.key', 'rb') as decSymkey:
    symKey = decSymkey.read()

# Read the Decrypted key with Fernet
dec_symKey = Fernet(symKey)

# Decrypt the Files using the Decrypted Key
dec_zip = dec_symKey.decrypt(enc_zip)
dec_file = dec_symKey.decrypt(enc_file)

# Save the Decrypted Back up files
with open('Decrypted Screenshots.zip', 'wb') as decZip:
    decZip.write(dec_zip)

with open('Decrypted fileSample.txt', 'wb') as decFile:
    decFile.write(dec_file)