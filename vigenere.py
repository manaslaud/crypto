def vigenere_cipher(text, key, mode):
    result = ""
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    for t, k in zip(text, key):
        shift = ord(k) - ord('A')
        if mode == 'encrypt':
            result += chr((ord(t) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += chr((ord(t) - ord('A') - shift) % 26 + ord('A'))
    return result

text = input("Enter text: ").upper()
key = input("Enter key: ").upper()
cipher_text = vigenere_cipher(text, key, 'encrypt')
decrypted_text = vigenere_cipher(cipher_text, key, 'decrypt')

print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypted_text)
