#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

from tkinter import messagebox
import AdWMFuncLib.Systemclean
import AdWMFuncLib.Systemrepair 
import  AdWMFuncLib.About.about 
import AdWMFuncLib.ShutdownPC.shutdownpc
import platform
from AdWMGUILang.lang import *
from Settings.settings import *
from SystemReq.system_req import *
from Theme.theme import *
from AgreementCheck.agreement_check import *
import pystray, threading
from PIL import Image, ImageDraw

def hide_window():
    window.withdraw()

def tray():
    image = Image.open("Icon/adwmgui_icon.png")
    d = ImageDraw.Draw(image)
    d.text((10, 25), "A", fill=(255,255,255))

    def on_exit(icon, item):
        icon.stop()
        window.quit()

    def on_show(icon, item):
        window.deiconify()
    
    sysclean = pystray.Menu(
        pystray.MenuItem(sysclean_tray_title, AdWMFuncLib.Systemclean.Cleanmgr),
        pystray.MenuItem(sysclean_advanced_clean_title, AdWMFuncLib.Systemclean.AdvancedCleanup)
    )

    sysrepair = pystray.Menu(
        pystray.MenuItem(system_repair_title, lambda: AdWMFuncLib.Systemrepair.RepairSystem(mode="auto"))
    )
    
    shutdown_pc = pystray.Menu(
        pystray.MenuItem(all_operations_shutdownpc_title, AdWMFuncLib.ShutdownPC.shutdownpc.all_operations_ShutdownPC),
        pystray.MenuItem("0", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(0)),
        pystray.MenuItem("5", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(5)),
        pystray.MenuItem("10", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(10)),
        pystray.MenuItem("15", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(15)),
        pystray.MenuItem("20", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(20)),
        pystray.MenuItem("25", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(25)),
        pystray.MenuItem("30", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(30)),
        pystray.MenuItem("35", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(35)),
        pystray.MenuItem("40", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(40)),
        pystray.MenuItem("45", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(45)),
        pystray.MenuItem("50", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(50)),
        pystray.MenuItem("55", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(55)),
        pystray.MenuItem("60", lambda: AdWMFuncLib.ShutdownPC.shutdownpc.shutdownpc(60))
    )

    menu = pystray.Menu(
        pystray.MenuItem(open_title, on_show),
        pystray.MenuItem(system_clean_title, sysclean),
        pystray.MenuItem(system_repair_title, sysrepair),
        pystray.MenuItem(shutdownpc_title, shutdown_pc),
        pystray.MenuItem(exit_title, on_exit)
    )

    icon = pystray.Icon("AdWMGUI", image, "AdWMGUI", menu)
    icon.run()

resx = config['MainMenu']['xsupportforresizability']
resy = config['MainMenu']['ysupportforresizability']

def close(event=None):
    window.destroy()

if check_agreement_file("adwmgui_software_acceptance_agreement.lsf") and platform.system() == "Windows":
    window = Tk()
    window.title(windows_title)
    icon = PhotoImage(file="Icon/adwmgui_icon.png")
    window.iconphoto(False, icon)
    window.geometry("550x30")
    window.configure(bg=window_bg)
    window.resizable(resx,resy) 
    systemclean = Button(window, text=system_clean_title , command=AdWMFuncLib.Systemclean.SystemClean, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
    systemclean.pack(side=LEFT)
    systemrepair = Button(window, text=system_repair_title, command=AdWMFuncLib.Systemrepair.SystemRepair, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
    systemrepair.pack(side=LEFT)
    about = Button(window, text=about_title, command=AdWMFuncLib.About.about.About, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
    about.pack(side=LEFT)
    shutdownpc = Button(window, text=shutdownpc_title, command=AdWMFuncLib.ShutdownPC.shutdownpc.ShutdownPC, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
    shutdownpc.pack(side=LEFT)
    settings = Button(window, text=settings_title, command=Settings, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
    settings.pack(side=LEFT)
    sysreq = Button(window, text=sys_req_title, command=sys_req, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
    sysreq.pack(side=LEFT)
    window.bind('<Control-w>', close)
    window.protocol("WM_DELETE_WINDOW", hide_window)
    threading.Thread(target=tray, daemon=True).start()
    window.mainloop()
elif not platform.system() == "Windows":
    messagebox.showerror(adwmgui_platform_error_title_txt, adwmgui_platform_error_txt)
elif not check_agreement_file("adwmgui_software_acceptance_agreement.lsf"):
    messagebox.showerror(adwmgui_agreement_error_title_txt, adwmgui_agreement_error_txt)