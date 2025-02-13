def xor_encrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def xor_decrypt(cipher_text, key):
    return xor_encrypt(cipher_text, key)  # XORing again reverses encryption

key = "8bytekey"  # 8-byte key
text = input("Enter the text to encrypt: ")

cipher_text = xor_encrypt(text, key)

print("\nText    : ", text)

decrypted_text = xor_decrypt(cipher_text, key)
print("Decrypted: ", decrypted_text)
