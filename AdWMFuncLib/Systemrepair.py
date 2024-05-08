#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

import os, time
from tkinter import *
from tkinter import messagebox

def RepairSystem():
    if messagebox.askyesno("AdWMGUI", "Show messages?") == True:
        messagebox.showinfo("RepairSystem", "Repairing System...")
        time.sleep(2)
        messagebox.showinfo("RepairSystem", "Repair System 1/4... (sfc /scannow)")
        os.system("sfc /scannow")
        time.sleep(2)
        messagebox.showinfo("RepairSystem", "Repair System 2/4... (dism /Online /Cleanup-Image /CheckHealth)")
        os.system("dism /Online /Cleanup-Image /CheckHealth")
        time.sleep(2)
        messagebox.showinfo("RepairSystem", "Repair System 3/4... (dism /Online /Cleanup-Image /ScanHealth)")
        os.system("dism /Online /Cleanup-Image /ScanHealth")
        time.sleep(2)
        messagebox.showinfo("RepairSystem", "Repair System 4/4... (dism /Online /Cleanup-Image /RestoreHealth)")
        os.system("dism /Online /Cleanup-Image /RestoreHealth")
        time.sleep(2)
        messagebox.showinfo("RepairSystem", "Reapiring System done!")
    else:
        os.system("sfc /scannow")
        time.sleep(2)
        os.system("dism /Online /Cleanup-Image /CheckHealth")
        time.sleep(2)
        os.system("dism /Online /Cleanup-Image /ScanHealth")
        time.sleep(2)
        os.system("dism /Online /Cleanup-Image /RestoreHealth")