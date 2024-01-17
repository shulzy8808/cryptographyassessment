# Encryption of Symmetric key using the user's public key
# Import RSA library
import rsa

# Load the main user (User 1) public key
with open('user1PublicKey_file.key', 'rb') as user1_pubKey:
    user1Pubkey = rsa.PublicKey.load_pkcs1(user1_pubKey.read())

# Load Symmetric Key
with open('symKey.key', 'rb') as symKey:
    sym_key = symKey.read()

# Encrypting Key
enc_symKey = rsa.encrypt(sym_key, user1Pubkey)

# Store Encrypted Key Backup
with open('Encrypted SymmetricKey.key', 'wb') as enc_symKeyfile:
    enc_symKeyfile.write(enc_symKey)