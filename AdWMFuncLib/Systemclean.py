#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

import subprocess, threading, os
from tkinter import *
from tkinter import messagebox
from AdWMGUILang.lang import *
from PyAppDevKit.pyappdevkit import *
from Theme.theme import *

def Cleanmgr():
    try:
        threading.Thread(target=lambda: subprocess.run(["cleanmgr.exe","/autoclean"])).start()
        messagebox.showinfo("AdWMGUI", cleanmgr_success_title)
    except subprocess.CalledProcessError:
        messagebox.showerror("AdWMGUI", cleanmgr_fail_title)

def DISMClean(mode):
    if mode == "auto":
        threading.Thread(target=lambda: subprocess.run("DISM.exe /Online /Cleanup-Image /AnalyzeComponentStore", shell=True)).start()
        threading.Thread(target=lambda: subprocess.run("DISM.exe /Online /Cleanup-Image /StartComponentCleanup", shell=True)).start()
        messagebox.showinfo(adv_cleanup_title, adv_clnp_done_title)
    elif mode == "manual":
        if messagebox.askyesno(adwmgui_txt_title, show_msg_ask_title) == True:
            messagebox.showinfo(adv_cleanup_title, adv_clnp_txt_title)
            time(2)
            messagebox.showinfo(adv_cleanup_title, adv_cleanup_step_one_txt_title)
            threading.Thread(target=lambda: subprocess.run("DISM.exe /Online /Cleanup-Image /AnalyzeComponentStore", shell=True)).start()
            messagebox.showinfo(adv_cleanup_title, adv_cleanup_step_two_txt_title)
            threading.Thread(target=lambda: subprocess.run("DISM.exe /Online /Cleanup-Image /StartComponentCleanup", shell=True)).start()
            messagebox.showinfo(adv_cleanup_title, adv_clnp_done_title)
        else:
            threading.Thread(target=lambda: subprocess.run("DISM.exe /Online /Cleanup-Image /AnalyzeComponentStore", shell=True)).start()
            threading.Thread(target=lambda: subprocess.run("DISM.exe /Online /Cleanup-Image /StartComponentCleanup", shell=True)).start()
            messagebox.showinfo(adv_cleanup_title, adv_clnp_done_title)

resx = config['SystemClean']['xsupportforresizability']
resy = config['SystemClean']['ysupportforresizability']

def AdvancedCleanup():
    advanced_cleanup = [
    f'del "{os.environ["WINDIR"]}\\Temp\\*.*" /s /q /f',
    f'for /d %p in ("{os.environ["WINDIR"]}\\Temp\\*.*") do rmdir "%p" /s /q',

    f'del "{os.environ["TMP"]}\\*.*" /s /q /f',
    f'for /d %p in ("{os.environ["TMP"]}\\*.*") do rmdir "%p" /s /q',

    f'del "{os.environ["WINDIR"]}\\Prefetch\\*.*" /s /q /f',
    f'for /d %p in ("{os.environ["WINDIR"]}\\Prefetch\\*.*") do rmdir "%p" /s /q',

    f'del "{os.environ["USERPROFILE"]}\\AppData\\Local\\Temp\\*.*" /s /q /f',
    f'for /d %p in ("{os.environ["USERPROFILE"]}\\AppData\\Local\\Temp\\*.*") do rmdir "%p" /s /q',

    f'del "{os.environ["WINDIR"]}\\SoftwareDistribution\\Download\\*.*" /s /q /f',
    f'for /d %p in ("{os.environ["WINDIR"]}\\SoftwareDistribution\\Download\\*.*") do rmdir "%p" /s /q'
]
    threads = []
    for clean in advanced_cleanup:
        t = threading.Thread(target=lambda: subprocess.run(clean, shell=True))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    messagebox.showinfo(adv_cleanup_title, adv_clnp_done_title)

def close(event=None):
    window.destroy()        

def SystemClean():
    global window
    window = Tk()
    window.title(system_clean_title)
    window.geometry("500x300")
    window.resizable(resx,resy)
    window.iconbitmap("Icon/adwmgui_system_clean.ico")
    window.configure(bg=window_bg)
    quick_clean_label = Label(window, text=quick_clean_title, font=("Arial",12,"bold"), anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    quick_clean_label.pack(fill="x", anchor="w")
    quick_clean = Button(window, text=sysclean_tray_title, command=Cleanmgr, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
    quick_clean.place(x=5, y=35)
    advanced_clean_label = Label(window, text=adv_clean_title, font=("Arial",12,"bold"), bg=label_bg, fg=label_fg)
    advanced_clean_label.place(y=70)
    advanced_clean = Button(window, text=sysclean_advanced_clean_title, command=AdvancedCleanup, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
    advanced_clean.place(x=5, y=100)
    advancedsystemclean = Button(window, text=advanced_system_clean_title, command=lambda: DISMClean(mode="manual"), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
    advancedsystemclean.place(x=105, y=100)
    window.bind('<Control-w>', close)
    window.mainloop()