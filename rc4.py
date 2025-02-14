def rc4_ksa(key):
    """Key Scheduling Algorithm (KSA)"""
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def rc4_prga(S, data_length):
    """Pseudo-Random Generation Algorithm (PRGA)"""
    i = j = 0
    key_stream = bytearray()
    for _ in range(data_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key_stream.append(S[(S[i] + S[j]) % 256])
    return key_stream

def rc4_encrypt_decrypt(key, data):
    """Encrypt or decrypt using RC4 (same function for both)."""
    key = bytearray(key, 'utf-8') if isinstance(key, str) else bytearray(key)
    data = bytearray(data, 'utf-8') if isinstance(data, str) else bytearray(data)
    S = rc4_ksa(key)
    key_stream = rc4_prga(S, len(data))
    return bytes([data[i] ^ key_stream[i] for i in range(len(data))])

# Example usage:
key = "secret"
data = "Hello, RC4!"

# Encrypt
cipher_text = rc4_encrypt_decrypt(key, data)
print("Cipher:", cipher_text)

# Decrypt (same function)
decrypted_text = rc4_encrypt_decrypt(key, cipher_text)
print("Decrypted:", decrypted_text.decode('utf-8'))
