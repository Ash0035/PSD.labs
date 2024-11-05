def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            
            offset = 65 if char.isupper() else 97
          
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    
    return caesar_cipher_encrypt(text, -shift)  

substitution_key = {
    'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y', 'G': 'U', 'H': 'I', 'I': 'O',
    'J': 'P', 'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F', 'O': 'G', 'P': 'H', 'Q': 'J', 'R': 'K',
    'S': 'L', 'T': 'Z', 'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N', 'Z': 'M'
}

reverse_substitution_key = {v: k for k, v in substitution_key.items()}

def substitution_cipher_encrypt(text, key):
    
    encrypted_text = ""
    for char in text.upper():  
        encrypted_text += key.get(char, char)  
    return encrypted_text

def substitution_cipher_decrypt(text, key):
   
    decrypted_text = ""
    for char in text.upper():
        decrypted_text += key.get(char, char)  
    return decrypted_text

def full_encryption(text, caesar_shift):
  
    caesar_encrypted = caesar_cipher_encrypt(text, caesar_shift)
    print(f"Caesar Encrypted: {caesar_encrypted}")  
    
    fully_encrypted = substitution_cipher_encrypt(caesar_encrypted, substitution_key)
    print(f"Fully Encrypted (after Substitution Cipher): {fully_encrypted}")  
    return fully_encrypted

def full_decryption(encrypted_text, caesar_shift):
   
    substitution_decrypted = substitution_cipher_decrypt(encrypted_text, reverse_substitution_key)
    print(f"Substitution Decrypted: {substitution_decrypted}") 
   
    original_text = caesar_cipher_decrypt(substitution_decrypted, caesar_shift)
    print(f"Original Decrypted Text: {original_text}")  
    return original_text

input_text = input("Input text: ")
caesar_shift = int(input("input the shift size: "))

print("Encryption Process:")
encrypted_text = full_encryption(input_text, caesar_shift)

print("\nDecryption Process:")
decrypted_text = full_decryption(encrypted_text, caesar_shift)

print(f"\nFinal Encrypted Text: {encrypted_text}")
print(f"Final Decrypted Text: {decrypted_text}")
