import hashlib

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift

    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()


def main():
    while True:
        print("\n===== CryptoLab =====")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Generate SHA-256 Hash")
        print("4. Verify SHA-256 Hash")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            text = input("Enter text: ")
            shift = int(input("Enter shift number: "))
            print("Encrypted:", caesar_cipher(text, shift))

        elif choice == "2":
            text = input("Enter encrypted text: ")
            shift = int(input("Enter shift number: "))
            print("Decrypted:", caesar_cipher(text, shift, True))

        elif choice == "3":
            text = input("Enter text: ")
            print("SHA-256:", sha256_hash(text))

        elif choice == "4":
            text = input("Enter original text: ")
            old_hash = input("Enter previous hash: ")
            new_hash = sha256_hash(text)

            if old_hash == new_hash:
                print("Verification successful!")
            else:
                print("Hash does not match!")

        elif choice == "5":
            print("Exiting CryptoLab...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
