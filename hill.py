import numpy as np

def hill_cipher_encrypt(text, key):
    key_matrix = np.array(key)
    text_vector = [ord(c) - ord('A') for c in text]
    text_vector = np.array(text_vector).reshape(-1, len(key))
    cipher_vector = (np.dot(text_vector, key_matrix) % 26).flatten()
    return ''.join(chr(c + ord('A')) for c in cipher_vector)

def hill_cipher_decrypt(cipher, key):
    key_matrix = np.array(key)
    inverse_key = np.linalg.inv(key_matrix) % 26
    inverse_key = np.round(inverse_key).astype(int)
    cipher_vector = [ord(c) - ord('A') for c in cipher]
    cipher_vector = np.array(cipher_vector).reshape(-1, len(key))
    text_vector = (np.dot(cipher_vector, inverse_key) % 26).flatten()
    return ''.join(chr(c + ord('A')) for c in text_vector)

key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
text = input("Enter text: ").upper()
if len(text) % 3 != 0:
    text += 'X' * (3 - len(text) % 3)

encrypted_text = hill_cipher_encrypt(text, key)
decrypted_text = hill_cipher_decrypt(encrypted_text, key)

print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
