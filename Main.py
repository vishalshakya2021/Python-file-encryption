from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted_data)


def decrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file, 'wb') as f:
        f.write(decrypted_data)


def main():
    key = generate_key()

    input_file = 'input.txt'
    encrypted_file = 'encrypted.txt'
    decrypted_file = 'decrypted.txt'

    encrypt_file(key, input_file, encrypted_file)
    print("File encrypted successfully.")

    decrypt_file(key, encrypted_file, decrypted_file)
    print("File decrypted successfully.")


if __name__ == "__main__":
    main()
