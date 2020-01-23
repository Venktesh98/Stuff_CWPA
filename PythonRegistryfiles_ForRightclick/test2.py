from winreg import*
import winreg

keyVal = r'SOFTWARE\\'


try:
    key = OpenKey(HKEY_LOCAL_MACHINE, keyVal, 0, KEY_ALL_ACCESS)
except:
    # key = CreateKey(HKEY_LOCAL_MACHINE, keyVal)
    key = CreateKey(key, "python")
SetValueEx(key, "Start Page", 0, REG_SZ, "snakes")
DeleteKey(key,"python")
CloseKey(key)


