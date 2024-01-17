# Install and Import Cryptography Library -- using pip install cryptography
from cryptography.fernet import Fernet

# Install rsa library -- using pip install rsa
import rsa

# Generate symmetric key for File Encryption
sym_key = Fernet.generate_key()

# Store the Symmetric Key in a key text
with open('symKey.key', 'wb') as symKey_file:
    symKey_file.write(sym_key)

# Generate Public and Private key for the two users
user1_publicKey,user1_priKey = rsa.newkeys(2048)
user2_publicKey,user2_priKey = rsa.newkeys(2048)

# Store the Public Key and Private Key in a key text
with open('user1PublicKey_file.key', 'wb') as user1pubKey_file:
    user1pubKey_file.write(user1_publicKey.save_pkcs1('PEM'))

with open('user2PublicKey_file.key', 'wb') as user2pubKey_file:
    user2pubKey_file.write(user2_publicKey.save_pkcs1('PEM'))

with open('user1PrivateKey_file.key', 'wb') as user1priKey_file:
    user1priKey_file.write(user1_priKey.save_pkcs1('PEM'))

with open('user2PrivateKey_file.key', 'wb') as user2priKey_file:
    user2priKey_file.write(user2_priKey.save_pkcs1('PEM'))