import gzip
import shutil

def compress(path):

    with open(path,'rb') as f_in:
        # print(path)
        outputpath= path+'.gz'   
        # print((outputpath))
        with gzip.open(outputpath,'wb') as f_out:
            content = f_in.read()
            f_out.write(content)
   
    print("compressed")
    print(outputpath)

    return outputpath

def decompress(path):

    with gzip.open(path,'rb') as f:
        outputfle=path[:-3]
        with open(outputfle, 'wb') as f2:
            file_content = f.read()
            f2.write(file_content)
    
    print("decompressed")
    print(outputfle)