#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

from tkinter import *
from tkinter import messagebox
from AdWMGUILang.lang import *

def AboutMsgBox():
    aboutLevel = str(input(about_level_title))
    aboutLevel = int(aboutLevel)
    if aboutLevel == 0:
        messagebox.showinfo(about_txt_title, about_zero_level_title)
    elif aboutLevel == 1:
        messagebox.showinfo(about_txt_title, about_one_level_title)
    elif aboutLevel == 2:
        messagebox.showinfo(about_txt_two_title, about_two_level_title)
    elif aboutLevel == 3:
        messagebox.showinfo(about_txt_three_title, about_three_level_title)
    else:
        messagebox.showerror(error_title, error_txt_title)