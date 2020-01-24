import os
filehome = os.path.expanduser('~')
filepath = os.path.join(filehome,'file.txt')
print(filepath)
with open(filepath,"w") as f:
    f.write("Heloo world")


# path = os.path.join(os.path.expanduser('~'),'Documents','file.txt')
# print (path)
# with open(path,'w') as f:
#     f.write("Heloo world")
