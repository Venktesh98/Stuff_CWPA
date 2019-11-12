#Does the encryption-decryption by using AES and SHA256 bit and generates the key itself not custom one

import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from Enc import encryption
from Dec import decryption
from Generate_Key import getKey

def Enc(fileName):
    passWord = "abcd"
    print(fileName)
    encryption(getKey(passWord),fileName)
    print("Finished.")

def Dec(fileName):
    passWord = "abcd"
    decryption(getKey(passWord),fileName)
    print("Finished.")
