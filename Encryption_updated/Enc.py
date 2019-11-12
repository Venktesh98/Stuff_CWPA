import os
from Crypto.Cipher import AES
from Crypto import Random
import time
from datetime import datetime

# def encryption(key,fileName):

#    #In seconds
#     start_time = time.time()
    
#     # #timer start
#     # start_time = datetime.now()

#     textSize = 64 * 1024
#     #outPutFile = "(encrypted)" + fileName
#     #outPutFile = "(encrypted)"+fileName
#     outPutFile = "encrypted."+fileName
#     filesize = str(os.path.getsize(fileName)).zfill(16)
#     IV = Random.new().read(16)

#     encryptor = AES.new(key, AES.MODE_CBC, IV)

#     with open(fileName, 'rb') as inputFile:
#         with open(outPutFile, 'wb') as oFile:
#             oFile.write(filesize.encode('utf-8'))
#             oFile.write(IV)

#             while True:
#                 text = inputFile.read(textSize)

#                 if len(text) == 0:
#                     break
#                 elif len(text) % 16 != 0:
#                     text += b' ' * (16 - (len(text) % 16))
#                 oFile.write(encryptor.encrypt(text))
#     # #timer counting 
#     # time_elapsed = datetime.now() - start_time
#     # print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

#     #main()
#     print("--- %s seconds ---" % (time.time() - start_time))
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
            # return outfile.write(encryptor.encrypt(chunk))
