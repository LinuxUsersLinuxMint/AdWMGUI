#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

from tkinter import *
from _tkinter import TclError
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import Tk

def AboutMsgBox():
    messagebox.showinfo("About", "AdWMGUI (Advanced Windows Manager GUI) version: 1.0, version_type: GUI Beta (For GUI), licence: GPL2")