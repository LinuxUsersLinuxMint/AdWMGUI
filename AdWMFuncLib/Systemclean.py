#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

import os, time
from tkinter import *
from tkinter import messagebox
from AdWMGUILang.lang import *

def OpenCleanmgr():
    os.system("cleanmgr.exe")

def AdvancedCleanup():
    if messagebox.askyesno(adwmgui_txt_title, show_msg_ask_title) == True:
        messagebox.showinfo(adv_cleanup_title, adv_clnp_txt_title)
        time.sleep(2)
        messagebox.showinfo(adv_cleanup_title, adv_cleanup_step_one_txt_title)
        os.system("DISM.exe /Online /Cleanup-Image /AnalyzeComponentStore")
        time.sleep(2)
        messagebox.showinfo(adv_cleanup_title, adv_cleanup_step_two_txt_title)
        os.system("DISM.exe /Online /Cleanup-Image /StartComponentCleanup")
        time.sleep(2)
        messagebox.showinfo(adv_cleanup_title, adv_clnp_done_title)
    else:
        os.system("DISM.exe /Online /Cleanup-Image /AnalyzeComponentStore")
        time.sleep(2)
        os.system("DISM.exe /Online /Cleanup-Image /StartComponentCleanup")