import os
import sys

def Install(menu_name='This is the name that shows up in the context menu'):
    '''Install registry entry for adding to context menu.'''
    import _winreg as wr

    for ext in ['.hex','.mcs']:
        # Check for extension handler override
        try:
            override = wr.QueryValue(wr.HKEY_CLASSES_ROOT, ext)
            if override:
                ext = override
        except WindowsError:
            pass
        keyVal = ext + '\\Shell\\' + menu_name + '\\command'
        try:
            key = wr.OpenKey(wr.HKEY_CLASSES_ROOT, 
                                    keyVal, 
                                    0, 
                                    wr.KEY_ALL_ACCESS)
        except WindowsError:
            key = wr.CreateKey(wr.HKEY_CLASSES_ROOT, keyVal)
        regEntry = (r'"C:\Python27\pythonw.exe" "' + os.getcwd() + 
                    r'\YourPythonScript.py" "%1"')
        wr.SetValueEx(key, '', 0, wr.REG_SZ, regEntry)
        wr.CloseKey(key)

if __name__ == "__main__":    
    if len(sys.argv) == 1:
        Install()
    elif len(sys.argv) == 2:
        inputFilename = sys.argv[1]
        DoStuff(inputFilename)