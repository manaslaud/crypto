import itertools

def create_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))  # Remove duplicates
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = key + "".join(c for c in alphabet if c not in key)
    return [list(matrix[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def format_text(text):
    text = text.upper().replace("J", "I")
    formatted = []
    i = 0
    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i + 1]:
            formatted.append(text[i] + "X")
            i += 1
        else:
            formatted.append(text[i] + text[i + 1])
            i += 2
    return formatted

def playfair_cipher(text, key, mode='encrypt'):
    matrix = create_matrix(key)
    text_pairs = format_text(text)
    result = []

    for a, b in text_pairs:
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:  # Same row
            col_a = (col_a + 1) % 5 if mode == 'encrypt' else (col_a - 1) % 5
            col_b = (col_b + 1) % 5 if mode == 'encrypt' else (col_b - 1) % 5
        elif col_a == col_b:  # Same column
            row_a = (row_a + 1) % 5 if mode == 'encrypt' else (row_a - 1) % 5
            row_b = (row_b + 1) % 5 if mode == 'encrypt' else (row_b - 1) % 5
        else:  # Rectangle swap
            col_a, col_b = col_b, col_a

        result.append(matrix[row_a][col_a] + matrix[row_b][col_b])

    return "".join(result)

if __name__ == "__main__":
    key = input("Enter key: ").upper()
    text = input("Enter text: ").upper().replace(" ", "")
    
    encrypted_text = playfair_cipher(text, key, 'encrypt')
    decrypted_text = playfair_cipher(encrypted_text, key, 'decrypt')
    
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)
