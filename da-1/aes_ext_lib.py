from Crypto.Cipher import AES
import secrets

k = secrets.token_bytes(16)

# encryption
key =k #16bit cipher key
data=b'Message to be encrypted'
cipher=AES.new(key,AES.MODE_EAX)

nonce=cipher.nonce
ciphertext,tag = cipher.encrypt_and_digest(data)

#decryption
key =k #16bit cipher key
cipher=AES.new(key,AES.MODE_EAX,nonce=nonce)
plaintext=cipher.decrypt(ciphertext)
try:
    cipher.verify(tag)
    print('Message is authentic: ',plaintext)
except ValueError:
    print('Message is not authentic')