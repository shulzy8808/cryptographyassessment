# Decrypting the Encrypted Symmetric Key with the User's private Key
# Load the Encrypted Fle
import rsa

with open('Encrypted SymmetricKey.key', 'rb') as symKey:
    sym_key = symKey.read()

# Load User 1 Private Key
with open('user1PrivateKey_file.key', 'rb') as priKey:
    pri_key = rsa.PrivateKey.load_pkcs1(priKey.read())

# Decrypt encrypted key backup
dec_symKey = rsa.decrypt(sym_key, pri_key)

# Save decrypted key backup
with open('Decrypted SymmetricKey.key', 'wb') as decsymKey:
    decsymKey.write(dec_symKey)