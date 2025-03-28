import random
import hashlib

class RSA:
    def __init__(self, key_size=512):
        self.p = self.generate_large_prime()
        self.q = self.generate_large_prime()
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)

        self.e = 65537  # Common public exponent
        self.d = pow(self.e, -1, self.phi)  # Compute private key (modular inverse)

    def generate_large_prime(self):
        """Generates a random large prime number."""
        while True:
            num = random.getrandbits(256) | (1 << 255) | 1  # Ensure it's odd and 256-bit
            if self.is_prime(num):
                return num

    def is_prime(self, num, tests=5):
        """Checks if a number is prime using Miller-Rabin."""
        if num < 2:
            return False
        for _ in range(tests):
            a = random.randint(2, num - 2)
            if pow(a, num - 1, num) != 1:
                return False
        return True

    def hash_message(self, message):
        """Hashes the message using SHA-256 and returns an integer."""
        h = hashlib.sha256(message.encode()).hexdigest()
        return int(h, 16)

    def sign(self, message):
        """Generates a digital signature using RSA."""
        hashed_msg = self.hash_message(message)
        signature = pow(hashed_msg, self.d, self.n)  # Signature = H(m)^d mod n
        return signature

    def verify(self, message, signature):
        """Verifies the digital signature."""
        hashed_msg = self.hash_message(message)
        decrypted_hash = pow(signature, self.e, self.n)  # V = S^e mod n
        return hashed_msg == decrypted_hash


# Example Usage
rsa = RSA()

message = "Secure Blockchain Transactions"
signature = rsa.sign(message)
print("Signature:", signature)

# Verify the signature
is_valid = rsa.verify(message, signature)
print("Signature Valid:", is_valid)
