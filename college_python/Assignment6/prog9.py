def custom_caesar_cipher(key, message, decode=False):
    if key < 0:
        return "INVALID INPUT"
    
    if decode:
        key = -key
    
    result = ""
    for char in message:
        if char.isupper():
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif char.isdigit():
            result += chr((ord(char) - ord('0') + key) % 10 + ord('0'))
        else:
            result += char
    
    return result

def main():
    print("=== Custom Caesar Cipher ===")
    choice = input("(1) Encrypt or (2) Decrypt: ")
    
    if choice in ['1', '2']:
        message = input("Enter message: ")
        key = int(input("Enter key: "))
        
        if key < 0:
            print("INVALID INPUT")
        else:
            result = custom_caesar_cipher(key, message, decode=(choice == '2'))
            action = "Decrypted" if choice == '2' else "Encrypted"
            print(f"{action} Text: {result}")
    else:
        print("Invalid choice!")

main()
