def gcd(a, b):
 while b:
     a, b = b, a % b
 return a
def mod_inverse(e, phi):
 for x in range(1, phi):
     if (e * x) % phi == 1:
         return x
 return None
def rsa_encrypt(plain_text, e, n):
     return ''.join(chr((ord(char) ** e) % n) for char in plain_text)
def rsa_decrypt(cipher_text, d, n):
 return ''.join(chr((ord(char) ** d) % n) for char in cipher_text)
p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = mod_inverse(e, phi)
text = "Manas Laud"
cipher_text = rsa_encrypt(text, e, n)
print("Text : " + text)
print("Cipher: " + cipher_text)
decrypted_text = rsa_decrypt(cipher_text, d, n)
print("Decrypted: " + decrypted_text)
