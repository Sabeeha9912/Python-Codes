from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)
cipher = Fernet(key)    #Load the key
with open("input.txt", "rb") as file:   # Read the original text file
    data = file.read()
encrypted_data = cipher.encrypt(data)   #Encrypt the data
with open("decrypt.txt", "wb") as file :# Write the encrypted data to 'decrypt.txt'
    file.write(encrypted_data)

print("File encrypted successfully! Saved as 'decrypt.txt'")
