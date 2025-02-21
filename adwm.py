#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

from tkinter import messagebox
import AdWMFuncLib.Systemclean
import AdWMFuncLib.Systemrepair
import AdWMFuncLib.About.about
import AdWMFuncLib.ShutdownPC.shutdownpc
from tkinter import *
from tkinter import Tk
from AdWMGUILang.lang import *
import platform

if platform.system() == "Windows":
    window = Tk()
    window.title(windows_title)
    icon = PhotoImage(file="Icon/adwmgui_icon.png")
    window.iconphoto(False, icon)
    window.geometry("830x30")
    window.resizable(FALSE,FALSE)
    systemclean = Button(window, text=system_clean_title , command=AdWMFuncLib.Systemclean.OpenCleanmgr)
    systemclean.pack(side=LEFT)
    advancedsystemclean = Button(window, text=advanced_system_clean_title, command=AdWMFuncLib.Systemclean.AdvancedCleanup)
    advancedsystemclean.pack(side=LEFT)
    systemrepair = Button(window, text=system_repair_title, command=AdWMFuncLib.Systemrepair.RepairSystem)
    systemrepair.pack(side=LEFT)
    about = Button(window, text=about_title, command=AdWMFuncLib.About.about.AboutMsgBox)
    about.pack(side=LEFT)
    shutdownpc = Button(window, text=shutdownpc_title, command=AdWMFuncLib.ShutdownPC.shutdownpc.ShutdownPC)
    shutdownpc.pack(side=LEFT)
    all_operations_shutdownpc = Button(window, text=all_operations_shutdownpc_title, command=AdWMFuncLib.ShutdownPC.shutdownpc.all_operations_ShutdownPC)
    all_operations_shutdownpc.pack(side=LEFT)
    window.mainloop()
else:
    messagebox.showerror(adwmgui_platform_error_title_txt, adwmgui_platform_error_txt)