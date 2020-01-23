from winreg import*
import winreg

keyVal = r"Directory\background\shell\abc\command"


try:
    key = OpenKey( HKEY_CLASSES_ROOT, keyVal, 0, KEY_ALL_ACCESS)
except:
    key = CreateKey( HKEY_CLASSES_ROOT, keyVal)
SetValueEx(key, "", 0, REG_SZ, "C:\Program Files (x86)\pasteanywhere\pasteanywhere.exe")
CloseKey(key)


