import winreg
from winreg import*
# import os

# def set_reg(name, value):

#     keyval=r"SOFTWARE\my path to\Registry"
#     try:
#         # keyval=r"SOFTWARE\my path to\Registry"
#             # if not os.path.exists("keyval"):
#         # key = CreateKey(HKEY_CURRENT_USER,keyval)
#         Registrykey= OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\my path to\Registry", 0, KEY_WRITE)
#             # Registrykey= OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\my path to\Registry")
#         # SetValueEx(Registrykey,name,0,REG_SZ,value)
#         # DeleteValue(Registrykey,name)
#         DeleteKeyEx(Registrykey,keyval)
#         # winreg.DeleteKey(Registrykey,keyval)
#             #print(dele1)
#         CloseKey(Registrykey)
#         return True
#     except WindowsError:
#         return False
#         # print('done')   
# #set_reg('MouseSensitivity', str(10))
# set_reg('Demo.exe',"C:\Program Files (x86)\Dailog\Dailog.exe" )

keyval=r"SOFTWARE\my path to"
try:
    Registrykey= OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\my path to", 0, KEY_ALL_ACCESS)
except:
    DeleteKeyEx(Registrykey,keyval)


    
