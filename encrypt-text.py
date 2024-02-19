#Tool to encrypt text file
from Crypto.PublicKey import RSA
import emoji

secret_code = "Secret_to_all"
key = RSA.generate(2048)
#encrypted_key is the private key
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                              protection="scryptAndAES128-CBC",
                              prot_params={'iteration_count':131072})

with open("rsa_key.bin", "wb") as f:
    f.write(encrypted_key)    

print("****Public certificate and details****")
print(key.publickey().export_key())
print(key.publickey().__doc__)
#print(encrypted_key)

#print encripted file 
fread = open("rsa_key.bin", "r")
pkey = fread.read()
if len(pkey) > 0:
    emoji_text = emoji.emojize('Certificate is in the file :thumbs_up: ')
else :
    emoji_text = emoji.emojize('Certificate is not in the file :thumbs_down: ')
  
print(emoji_text)

