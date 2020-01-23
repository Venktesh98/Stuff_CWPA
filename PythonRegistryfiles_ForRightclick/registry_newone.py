import winreg
from winreg import*
import os

class Registry:

    # Global declaretions
    # connect_registry = ConnectRegistry(None,HKEY_CLASSES_ROOT)
    # keyval="Directory\\background\\shell\\Encrypting\\command"
    # key = CreateKey(connect_registry,keyval)
    # opening_key = OpenKey(connect_registry,"Directory\\background\\shell")

    def setRegister(self,name,value):
        connect_registry = ConnectRegistry(None,HKEY_CLASSES_ROOT)
        keyval=r"Directory\background\shell\Encrypting\command"
        try:
            key = CreateKey(connect_registry,keyval)
            # self.key = CreateKey(connect_registry,keyval)
            # Registrykey= OpenKey(connect_registry, "Directory\\background\\shell\\Encrypting\\command", 0,KEY_ALL_ACCESS)
            Registrykey= OpenKey(connect_registry, keyval, 0,KEY_ALL_ACCESS)
            SetValueEx(Registrykey,name,1,REG_SZ,value)
            CloseKey(Registrykey)
            return True
        except WindowsError:
            return False  

    # def deleteRegistry(self):
    #     keyval=r"Directory\background\shell"
    #     connect_registry =  ConnectRegistry(None,HKEY_CLASSES_ROOT)
    #     opening_key = OpenKey(connect_registry,keyval)
    #     DeleteKey(opening_key,"Encrypting\\command")
    #     DeleteKey(opening_key,"Encrypting")

    #     #Use it if defined in Global
    #     # DeleteKey(self.opening_key,"Encrypting\\command")
    #     # DeleteKey(self.opening_key,"Encrypting")

ob = Registry()
ob.setRegister("","C:\Program Files (x86)\pasteanywhere\pasteanywhere.exe")
# ob.deleteRegistry()