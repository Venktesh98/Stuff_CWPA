import winreg
from winreg import*
import os

# def set_reg(name, value):
    
#     registry = ConnectRegistry(None, HKEY_CLASSES_ROOT)
#     try:
#         keyval=r"Directory\background\shell\Encrypting\command"
#         #if not os.path.exists("keyval"):
#         # key = CreateKey(HKEY_CLASSES_ROOT,keyval)
#         key = CreateKey(registry,keyval)
#         # Registrykey= OpenKey(HKEY_CLASSES_ROOT, r"Directory\background\shell\abc\command", 0,KEY_WRITE)
#         Registrykey= OpenKey(registry, r"Directory\background\shell\Encrypting\command", 0,KEY_WRITE)
#         # winreg.DeleteKey(Registrykey,keyval)
#         SetValueEx(Registrykey,name,0,REG_SZ,value)
#         CloseKey(Registrykey)
#         return True
#     except WindowsError:
#         return False   
#set_reg('MouseSensitivity', str(10))

# def setreg_folder(name,value):
#     registry = ConnectRegistry(None, HKEY_CLASSES_ROOT)
#     try:
#         keyval=r"Directory\shell\Encrypting\command"
#         #if not os.path.exists("keyval"):
#         # key = CreateKey(HKEY_CLASSES_ROOT,keyval)
#         key = CreateKey(registry,keyval)
#         # Registrykey= OpenKey(HKEY_CLASSES_ROOT, r"Directory\background\shell\abc\command", 0,KEY_WRITE)
#         Registrykey= OpenKey(registry, r"Directory\shell\Encrypting\command", 0,KEY_WRITE)
#         SetValueEx(Registrykey,name,0,REG_SZ,value)
#         CloseKey(Registrykey)
#         return True
#     except WindowsError:
#         return False


def setreg_anyfile(name,value):
    registry = ConnectRegistry(None, HKEY_CLASSES_ROOT)
    try:
        keyval=r"*\shell\abc\command"
        #key = CreateKey(HKEY_CLASSES_ROOT,keyval)
        key = CreateKey(registry,keyval)
        #Registrykey= OpenKey(HKEY_CLASSES_ROOT, r"*\shell\abc\command", 0,KEY_WRITE)
        Registrykey= OpenKey(registry, r"*\shell\abc\command",0,KEY_WRITE)
        # winreg.DeleteKey(Registrykey,keyval)
        SetValueEx(Registrykey,name,0,REG_SZ,value)
        CloseKey(Registrykey)
        return True
    except WindowsError:
        return False   


#set_reg("","C:\Program Files (x86)\pasteanywhere\pasteanywhere.exe")
#setreg_folder("","C:\Program Files (x86)\pasteanywhere\pasteanywhere.exe")
setreg_anyfile("","C:\Program Files (x86)\pasteanywhere\pasteanywhere.exe")
