# Digital Signatures -- using the Private Key
# Load the files
import rsa

with open('Screenshots.zip', 'rb') as zipFile:
    zip_file = zipFile.read()

with open('fileSample.txt', 'rb') as file:
    file_sample = file.read()

# Load user 1 Private key
with open('user1PrivateKey_file.key', 'rb') as priKey:
    pri_key = rsa.PrivateKey.load_pkcs1(priKey.read())

# Signing Files
zip_signature = rsa.sign(zip_file, pri_key, 'SHA-256')
file_signature = rsa.sign(file_sample, pri_key, 'SHA-256')

# Save Digital Signature Files
with open('Screenshots Signature.txt', 'wb') as zipSign:
    zipSign.write(zip_signature)

with open('File Signature.txt', 'wb') as fileSign:
    fileSign.write(file_signature)