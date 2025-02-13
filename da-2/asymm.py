from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()
message = b"Manas"
signature = private_key.sign(message, hashes.SHA256())
try:
    public_key.verify(signature, message, hashes.SHA256())
    print("Digital Signature is VALID")
except:
    print("Digital Signature is INVALID")