#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

import AdWMFuncLib.Systemclean
import AdWMFuncLib.Systemrepair
import AdWMFuncLib.about_help.about
import AdWMFuncLib.about_help.help
from tkinter import *
from _tkinter import TclError
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import Tk

window = Tk()
window.title("AdWMGUI (Advanced Windows Manager GUI)")
window.geometry("385x30")
window.resizable(FALSE,FALSE)
systemclean = Button(window, text="SystemClean", command=AdWMFuncLib.Systemclean.OpenCleanmgr)
systemclean.pack(side=LEFT)
advancedsystemclean = Button(window, text="DISM WinSxs Folder clean", command=AdWMFuncLib.Systemclean.AdvancedCleanup)
advancedsystemclean.pack(side=LEFT)
systemrepair = Button(window, text="SystemRepair", command=AdWMFuncLib.Systemrepair.RepairSystem)
systemrepair.pack(side=LEFT)
about = Button(window, text="About", command=AdWMFuncLib.about_help.about.AboutMsgBox)
about.pack(side=LEFT)
help = Button(window, text="Help", command=AdWMFuncLib.about_help.help.HelpMsgBox)
help.pack(side=LEFT)
window.mainloop()