#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

from tkinter import *
from tkinter import messagebox

def AboutMsgBox():
    aboutLevel = str(input('Enter About Level (0, 1, 2, 3): '))
    aboutLevel = int(aboutLevel)
    if aboutLevel == 0:
        messagebox.showinfo("About", "AdWMGUI (Advanced Windows Manager GUI) version: 1.2")
    elif aboutLevel == 1:
        messagebox.showinfo("About", "AdWMGUI (Advanced Windows Manager GUI) version: 1.2, version_type: Stable Version (for GUI and Program), licence: GPL2")
    elif aboutLevel == 2:
        messagebox.showinfo("About Licence", "AdWMGUI (Advanced Windows Manager GUI), Licence type: GPL, Licence Version: 2, Licence Name: GPL2")
    elif aboutLevel == 3:
        messagebox.showinfo("Manufacturer Information", "Program Manufacturer: LinuxUsersLinuxMint, Organization: LinuxUsersLinuxMint, Organization Website: https://linuxuserslinuxmint.github.io/")
    else:
        messagebox.showerror("Error", "Error: Unknown About Level")