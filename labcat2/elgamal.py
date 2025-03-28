import random

class ElGamal:
    def __init__(self, p, g):
        self.p = p  # Large prime number
        self.g = g  # Primitive root modulo p
        self.x = random.randint(2, p - 2)  # Private key (random number)
        self.y = pow(g, self.x, p)  # Public key y = g^x mod p

    def encrypt(self, M):
        """Encrypts the message M"""
        k = random.randint(2, self.p - 2)  # Random number for encryption
        c1 = pow(self.g, k, self.p)  # c1 = g^k mod p
        c2 = (M * pow(self.y, k, self.p)) % self.p  # c2 = M * y^k mod p
        return (c1, c2)

    def decrypt(self, c1, c2):
        """Decrypts the ciphertext (c1, c2)"""
        s = pow(c1, self.x, self.p)  # Compute shared secret s = c1^x mod p
        s_inv = pow(s, -1, self.p)  # Modular inverse of s mod p
        M = (c2 * s_inv) % self.p  # Recover M
        return M


# Example usage
p = 7919  # Large prime number
g = 2     # Primitive root modulo p

elgamal = ElGamal(p, g)

# Encrypt a message
message = 1234  # Must be < p
ciphertext = elgamal.encrypt(message)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_message = elgamal.decrypt(*ciphertext)
print("Decrypted Message:", decrypted_message)
