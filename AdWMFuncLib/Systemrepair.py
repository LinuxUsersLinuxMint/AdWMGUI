#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

import os, time
from tkinter import *
from tkinter import messagebox
from AdWMGUILang.lang import *

def RepairSystem():
    if messagebox.askyesno(adwmgui_txt_title, show_msg_ask_title) == True:
        messagebox.showinfo(repair_sys_title, repair_sys_txt_title)
        time.sleep(2)
        messagebox.showinfo(repair_sys_title, repair_sys_step_one_title)
        os.system("sfc /scannow")
        time.sleep(2)
        messagebox.showinfo(repair_sys_title, repair_sys_step_two_title)
        os.system("dism /Online /Cleanup-Image /CheckHealth")
        time.sleep(2)
        messagebox.showinfo(repair_sys_title, repair_sys_step_three_title)
        os.system("dism /Online /Cleanup-Image /ScanHealth")
        time.sleep(2)
        messagebox.showinfo(repair_sys_title, repair_sys_step_four_title)
        os.system("dism /Online /Cleanup-Image /RestoreHealth")
        time.sleep(2)
        messagebox.showinfo(repair_sys_title, repair_sys_done_title)
    else:
        os.system("sfc /scannow")
        time.sleep(2)
        os.system("dism /Online /Cleanup-Image /CheckHealth")
        time.sleep(2)
        os.system("dism /Online /Cleanup-Image /ScanHealth")
        time.sleep(2)
        os.system("dism /Online /Cleanup-Image /RestoreHealth")