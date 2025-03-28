class ECC:
    def __init__(self, a, b, p, Gx, Gy, n):
        self.a = a
        self.b = b
        self.p = p
        self.G = (Gx, Gy)
        self.n = n

    def inverse_mod(self, k, p):
        return pow(k, p - 2, p)

    def add(self, P, Q):
        if P is None: return Q
        if Q is None: return P
        if P == Q:
            m = (3 * P[0]**2 + self.a) * self.inverse_mod(2 * P[1], self.p) % self.p
        else:
            m = (Q[1] - P[1]) * self.inverse_mod(Q[0] - P[0], self.p) % self.p
        x_r = (m * m - P[0] - Q[0]) % self.p
        y_r = (m * (P[0] - x_r) - P[1]) % self.p
        return (x_r, y_r)

    def multiply(self, k, P):
        R = None
        for i in bin(k)[2:]:
            R = self.add(R, R)
            if i == '1':
                R = self.add(R, P)
        return R


# Parameters for SECP256k1 curve
ecc = ECC(
    a=0, 
    b=7, 
    p=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,
    Gx=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    Gy=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
    n=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
)

# Generate private key (random number)
private_key = 0x1C3A7D8F9E2B6C7D9A0E4F6B8D5C3A1B2F9D8E7C6B5A4C3D2E1F

# Compute public key
public_key = ecc.multiply(private_key, ecc.G)

print("Private Key:", hex(private_key))
print("Public Key:", public_key)
