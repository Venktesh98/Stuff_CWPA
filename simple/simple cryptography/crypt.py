from cryptography.fernet import Fernet

fhand = open("key.key","rb")
key = fhand.read()
fhand.close()

with open("test.txt","rb") as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open("test.txt.encrypted","wb") as f:
    f.write(encrypted)

