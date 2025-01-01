#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

from tkinter import *
from tkinter import messagebox
from AdWMGUILang.lang import *
from AdWMFuncLib.Systemrepair import *
from AdWMFuncLib.Systemclean import *
import os

def ShutdownPC():
    if messagebox.askyesno(adwmgui_txt_title, shutdownpc_askyesno_txt_title) == True:
        userTime = str(input(usertm_title))
        os.system("cmd.exe /c shutdown -s -t {0}". format(userTime))
    else:
        print(shutdownpc_askyesno_cancel_txt_title)

def all_operations_ShutdownPC():
    if messagebox.askyesno(adwmgui_txt_title, shutdownpc_askyesno_txt_title) == True:
        time.sleep(0.5)
        OpenCleanmgr()
        time.sleep(0.5)
        AdvancedCleanup()
        time.sleep(0.5)
        RepairSystem()
        time.sleep(0.5)
        ShutdownPC()
    else:
        print(shutdownpc_askyesno_cancel_txt_title)