import random
import hashlib

class ElGamalDSA:
    def __init__(self, p, g):
        self.p = p  # Large prime number
        self.g = g  # Primitive root modulo p
        self.x = random.randint(2, p - 2)  # Private key
        self.y = pow(g, self.x, p)  # Public key y = g^x mod p

    def hash_message(self, message):
        """Hashes the message using SHA-256 and returns an integer."""
        h = hashlib.sha256(message.encode()).hexdigest()
        return int(h, 16) % (self.p - 1)

    def sign(self, message):
        """Generates a digital signature (r, s) for a given message."""
        h_m = self.hash_message(message)

        while True:
            k = random.randint(2, self.p - 2)
            if self.gcd(k, self.p - 1) == 1:  # Ensure k has an inverse
                break

        r = pow(self.g, k, self.p)  # r = g^k mod p
        k_inv = pow(k, -1, self.p - 1)  # Compute modular inverse of k
        s = ((h_m - self.x * r) * k_inv) % (self.p - 1)

        return (r, s)

    def verify(self, message, r, s):
        """Verifies the digital signature (r, s) for a given message."""
        if not (1 < r < self.p):
            return False

        h_m = self.hash_message(message)
        v1 = pow(self.g, h_m, self.p)  # g^H(m) mod p
        v2 = (pow(self.y, r, self.p) * pow(r, s, self.p)) % self.p  # y^r * r^s mod p

        return v1 == v2

    def gcd(self, a, b):
        """Computes the greatest common divisor (GCD) using Euclidean algorithm."""
        while b:
            a, b = b, a % b
        return a


# Example usage
p = 7919  # Large prime number
g = 2     # Primitive root modulo p

elgamal_dsa = ElGamalDSA(p, g)

# Sign a message
message = "Blockchain Security"
signature = elgamal_dsa.sign(message)
print("Signature:", signature)

# Verify the signature
is_valid = elgamal_dsa.verify(message, *signature)
print("Signature Valid:", is_valid)
