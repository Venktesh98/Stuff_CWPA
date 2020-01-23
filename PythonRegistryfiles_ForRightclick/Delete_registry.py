import winreg
from winreg import *
import os

class deleting:
    def deleteRegistry(self):
        keyval=r"Directory\background\shell"
        connect_registry =  ConnectRegistry(None,HKEY_CLASSES_ROOT)
        opening_key = OpenKey(connect_registry,keyval)
        DeleteKey(opening_key,"Encrypting\\command")
        DeleteKey(opening_key,"Encrypting")

ob = deleting()
ob.deleteRegistry()