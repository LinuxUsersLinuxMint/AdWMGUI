#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

from tkinter import messagebox
import AdWMFuncLib.Systemclean
import AdWMFuncLib.Systemrepair
import AdWMFuncLib.About.about
import AdWMFuncLib.ShutdownPC.shutdownpc
from tkinter import *
from tkinter import Tk
import platform

if platform.system() == "Windows":
        window = Tk()
        window.title("AdWMGUI (Advanced Windows Manager GUI)")
        window.geometry("700x30")
        window.resizable(FALSE,FALSE)
        systemclean = Button(window, text="SystemClean", command=AdWMFuncLib.Systemclean.OpenCleanmgr)
        systemclean.pack(side=LEFT)
        advancedsystemclean = Button(window, text="DISM WinSxs Folder clean", command=AdWMFuncLib.Systemclean.AdvancedCleanup)
        advancedsystemclean.pack(side=LEFT)
        systemrepair = Button(window, text="SystemRepair", command=AdWMFuncLib.Systemrepair.RepairSystem)
        systemrepair.pack(side=LEFT)
        about = Button(window, text="About", command=AdWMFuncLib.About.about.AboutMsgBox)
        about.pack(side=LEFT)
        shutdownpc = Button(window, text="Shutdown PC (And More)", command=AdWMFuncLib.ShutdownPC.shutdownpc.ShutdownPC)
        shutdownpc.pack(side=LEFT)
        window.mainloop()
else:
    messagebox.showerror("AdWMGUI Platform System", "Sorry! You do not meet the Platform system requirement to use the AdWMGUI application.")