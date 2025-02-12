def xor_encrypt(text, key):
    """ Encrypt text using XOR encryption with a repeating key """
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def xor_decrypt(cipher_text, key):
    """ Decrypt text (XOR encryption is symmetric, so decryption is the same) """
    return xor_encrypt(cipher_text, key)  # XORing again reverses encryption

# Example usage
key = "8bytekey"  # 8-byte key
text = input("Enter the text to encrypt: ")

cipher_text = xor_encrypt(text, key)

print("\nText    : ", text)

decrypted_text = xor_decrypt(cipher_text, key)
# print("Decrypted: ", decrypted_text)
