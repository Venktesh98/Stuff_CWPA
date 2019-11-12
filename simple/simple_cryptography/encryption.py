from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

fhand = open("key.key","wb")
fhand.write(key)
fhand.close()