def aes_encrypt(plain_text, key):
    return ''.join(chr((ord(char) + key) % 256) for char in plain_text)

def aes_decrypt(cipher_text, key):
    return ''.join(chr((ord(char) - key) % 256) for char in cipher_text)
