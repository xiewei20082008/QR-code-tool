import win32com.client
from ctypes import *
import win32com
from time import sleep



def reg():
    dm = win32com.client.Dispatch('dm.dmsoft')
    hMod = windll.kernel32.GetModuleHandleA('dm.dll')
    memarray = (c_char*1).from_address(hMod+0x1063D0)
    memarray[0] = '1'
    return dm

dm = reg()
