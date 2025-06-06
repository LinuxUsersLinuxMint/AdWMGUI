#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

import os
from tkinter import *
from tkinter import messagebox
from AdWMGUILang.lang import *
from PyAppDevKit.pyappdevkit import *

def RepairSystem():
    if messagebox.askyesno(adwmgui_txt_title, show_msg_ask_title) == True:
        messagebox.showinfo(repair_sys_title, repair_sys_txt_title)
        time(2)
        messagebox.showinfo(repair_sys_title, repair_sys_step_one_title)
        os.system("sfc /scannow")
        time(2)
        messagebox.showinfo(repair_sys_title, repair_sys_step_two_title)
        os.system("dism /Online /Cleanup-Image /CheckHealth")
        time(2)
        messagebox.showinfo(repair_sys_title, repair_sys_step_three_title)
        os.system("dism /Online /Cleanup-Image /ScanHealth")
        time(2)
        messagebox.showinfo(repair_sys_title, repair_sys_step_four_title)
        os.system("dism /Online /Cleanup-Image /RestoreHealth")
        time(2)
        messagebox.showinfo(repair_sys_title, repair_sys_done_title)
    else:
        os.system("sfc /scannow")
        time(2)
        os.system("dism /Online /Cleanup-Image /CheckHealth")
        time(2)
        os.system("dism /Online /Cleanup-Image /ScanHealth")
        time(2)
        os.system("dism /Online /Cleanup-Image /RestoreHealth")