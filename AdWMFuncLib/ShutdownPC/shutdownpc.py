#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

from tkinter import *
from tkinter import messagebox
import os

def ShutdownPC():
    if messagebox.askyesno("AdWMGUI", "Are you sure you want to shutdown your computer?") == True:
        userTime = input("Enter time in seconds: ")
        os.system("shutdown /s /t {0}", format(userTime))
    else:
        print("Shutdown cancelled.")