#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

import os, time
from tkinter import *
from _tkinter import TclError
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import Tk

def OpenCleanmgr():
    os.system("cleanmgr.exe")

def AdvancedCleanup():
    messagebox.showinfo("AdvancedCleanup", "Advanced Cleanup...")
    time.sleep(2)
    messagebox.showinfo("AdvancedCleanup", "Advanced Cleanup 1/2... (DISM.exe /Online /Cleanup-Image /AnalyzeComponentStore)")
    os.system("DISM.exe /Online /Cleanup-Image /AnalyzeComponentStore")
    time.sleep(2)
    messagebox.showinfo("AdvancedCleanup", "Advanced Cleanup 2/2... (DISM.exe /Online /Cleanup-Image /StartComponentCleanup)")
    os.system("DISM.exe /Online /Cleanup-Image /StartComponentCleanup")
    time.sleep(2)
    messagebox.showinfo("AdvancedCleanup", "Advanced Cleanup done!")