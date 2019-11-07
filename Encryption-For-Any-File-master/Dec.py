import os
from Crypto.Cipher import AES
import time
from datetime import datetime

def decryption(key, fileName):

    #timer start
    # start_time = datetime.now()

    #In seconds
    start_time = time.time()

    textSize = 64 * 1024
    outPutFile = fileName[10:]
    
    with open(fileName, 'rb') as inputFile:
        fileSize = int(inputFile.read(16))
        IV = inputFile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outPutFile,'wb') as oFile:
            while True:
                text = inputFile.read(textSize)

                if len(text) == 0:
                    break

                oFile.write(decryptor.decrypt(text))
            oFile.truncate(fileSize)
    #timer counting 
    # time_elapsed = datetime.now() - start_time
    # print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

    #main()
    print("--- %s seconds ---" % (time.time() - start_time))
            
