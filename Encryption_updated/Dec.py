import os
from Crypto.Cipher import AES
import time
from datetime import datetime


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


# def decryption(key, fileName):

#     #timer start
#     # start_time = datetime.now()

#     #In seconds
#     start_time = time.time()

#     textSize = 64 * 1024
#     outPutFile = fileName[10:]
    
#     with open(fileName, 'rb') as inputFile:
#         fileSize = int(inputFile.read(16))
#         IV = inputFile.read(16)

#         decryptor = AES.new(key, AES.MODE_CBC, IV)

#         with open(outPutFile,'wb') as oFile:
#             while True:
#                 text = inputFile.read(textSize)

#                 if len(text) == 0:
#                     break

#                 oFile.write(decryptor.decrypt(text))
#             oFile.truncate(fileSize)
#     #timer counting 
#     # time_elapsed = datetime.now() - start_time
#     # print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

#     #main()
#     print("--- %s seconds ---" % (time.time() - start_time))