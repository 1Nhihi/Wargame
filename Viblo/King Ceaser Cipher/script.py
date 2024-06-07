# Define the alphabets
alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
alphabet2 = "0123456789"

def decrypt_char(char, key):
    if char in alphabet1:
        idx = alphabet1.index(char)
        new_idx = (idx - key) % len(alphabet1)
        return alphabet1[new_idx]
    elif char in alphabet2:
        idx = alphabet2.index(char)
        new_idx = (idx - key) % len(alphabet2)
        return alphabet2[new_idx]
    else:
        return char  # In case of any non-alphabetic characters

# Decrypt the entire message
encrypted_message = "a22W362Z273a40Z22X56357W5268a411"
key = 48

decrypted_message = ''.join(decrypt_char(c, key) for c in encrypted_message)
print(decrypted_message)

# Flag{e44a584d495e62d44b78579a7480e633}