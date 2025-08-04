def caesar_cipher_encode(key, message):
    result = ""
    for char in message:
        if char.isupper():
            shifted = (ord(char) - ord('A') + key) % 26 + ord('A')
            result += chr(shifted)
        elif char.islower():
            shifted = (ord(char) - ord('a') + key) % 26 + ord('a')
            result += chr(shifted)
        elif char.isdigit():
            shifted = (ord(char) - ord('0') + key) % 10 + ord('0')
            result += chr(shifted)
        else:
            result += char
    return result

def caesar_cipher_decode(key, message):
    return caesar_cipher_encode(-key, message)  # decoding uses reverse shift

# Menu like switch-case
def main():
    print("Caesar Cipher Program")
    print("1. Encode")
    print("2. Decode")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        plaintext = input("Enter your PlainText: ")
        key = int(input("Enter the Key: "))
        if key <= 0:
            print("INVALID INPUT")
        else:
            print("Encrypted Text:", caesar_cipher_encode(key, plaintext))

    elif choice == '2':
        ciphertext = input("Enter your CipherText: ")
        key = int(input("Enter the Key used for encryption: "))
        print("Decrypted Text:", caesar_cipher_decode(key, ciphertext))

    else:
        print("Invalid Choice")

# Run the main function
main()
