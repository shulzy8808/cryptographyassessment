# Verification of Digital Signatures --- using the Public Key
# Load the files
import rsa

with open('Screenshots.zip','rb') as zipFile:
    zip_file = zipFile.read()

with open('fileSample.txt', 'rb') as file:
    file_sample = file.read()

with open('Screenshots Signature.txt', 'rb') as zipSign:
   zip_sign = zipSign.read()

with open('File Signature.txt', 'rb') as fileSign:
    file_sign = fileSign.read()

# Loading the Private Key
with open('user1PrivateKey_file.key', 'rb') as priKey:
    pri_key = rsa.PrivateKey.load_pkcs1(priKey.read())

# Digital Signature Verification
zip_verify = rsa.verify(zip_file,zip_sign, pri_key)
file_verify = rsa.verify(file_sample,file_sign,pri_key)

print(f'Zip Verification: {zip_verify} \nFile Verification: {file_verify}'  )