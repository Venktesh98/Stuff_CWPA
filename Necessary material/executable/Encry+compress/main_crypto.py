#Does the encryption-decryption by using AES and SHA256 bit and generates the key itself not custom one

import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from Generate_Key import getKey
 
def Enc(fileName):
    passWord = "abcd"
    # print(fileName)
    outputfile=encryption(getKey(passWord),fileName)
    print("Finished.")
    return outputfile

def Dec(fileName):
    passWord = "abcd"
    outputfile=decryption(getKey(passWord),fileName)
    return outputfile

def encryption(key , filename):
    chunksize = 64 * 1024
    outputFile = filename+".enc"
    #outputFile = "/media/akshar/D/Copy/new"+".enc"

    filesize = str(os.path.getsize(filename)).zfill(16)
    # print(filesize)
    # IV = ''
    # os.chdir("/media/akshar/D/Copy")
    IV = Random.new().read(16)
    # for i in range(16):
    #     IV += chr(random.randint(0, 0xFF))


    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))
            print("Encrypted") 
            print(outputFile)
            return outputFile
            # return outfile.write(encryptor.encrypt(chunk))

def decryption(key, filename):
    chunksize = 64 * 1024
    outputFile = filename[:-4]

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

            print("Decrypted")
            print(outputFile)
            return outputFile