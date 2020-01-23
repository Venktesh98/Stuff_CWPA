from winreg import *

registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
def openRegistryA():

    rawKeyA = OpenKey(registry, "SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System")

    try:
        i = 0
        while 1:
            name, value, type = EnumValue(rawKeyA, i)
            print(name, value, i)
            i += 1

    except WindowsError:
        print("END")

    CloseKey(rawKeyA)

def openRegistryB():
    rawKeyB = OpenKey(registry, "SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters")

    try:
        i = 0
        while 1:
            name, value, type = EnumValue(rawKeyB, i)
            print(name, value, i)
            i += 1

    except WindowsError:
        print("END")

    CloseKey(rawKeyB)

openRegistryA()
openRegistryB()
