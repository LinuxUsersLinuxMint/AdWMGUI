#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

import subprocess,threading
from tkinter import *
from tkinter import messagebox
from AdWMGUILang.lang import *
from Theme.theme import *
from PyAppDevKit.pyappdevkit import *

def RepairSystem(mode):
    if mode == "auto":
        threading.Thread(target=lambda: subprocess.run("sfc /scannow", shell=True)).start()
        time(2)
        threading.Thread(target=lambda: subprocess.run("dism /Online /Cleanup-Image /CheckHealth", shell=True)).start()
        time(2)
        threading.Thread(target=lambda: subprocess.run("dism /Online /Cleanup-Image /ScanHealth", shell=True)).start()
        time(2)
        threading.Thread(target=lambda: subprocess.run("dism /Online /Cleanup-Image /RestoreHealth", shell=True)).start()
        time(2)
        messagebox.showinfo(repair_sys_title, repair_sys_done_title)
    elif mode == "manual":
        if messagebox.askyesno(adwmgui_txt_title, show_msg_ask_title) == True:
            messagebox.showinfo(repair_sys_title, repair_sys_txt_title)
            time(2)
            messagebox.showinfo(repair_sys_title, repair_sys_step_one_title)
            threading.Thread(target=lambda: subprocess.run("sfc /scannow", shell=True)).start()
            time(2)
            messagebox.showinfo(repair_sys_title, repair_sys_step_two_title)
            threading.Thread(target=lambda: subprocess.run("dism /Online /Cleanup-Image /CheckHealth", shell=True)).start()
            time(2)
            messagebox.showinfo(repair_sys_title, repair_sys_step_three_title)
            threading.Thread(target=lambda: subprocess.run("dism /Online /Cleanup-Image /ScanHealth", shell=True)).start()
            time(2)
            messagebox.showinfo(repair_sys_title, repair_sys_step_four_title)
            threading.Thread(target=lambda: subprocess.run("dism /Online /Cleanup-Image /RestoreHealth", shell=True)).start()
            time(2)
            messagebox.showinfo(repair_sys_title, repair_sys_done_title)
        else:
            threading.Thread(target=lambda: subprocess.run("sfc /scannow", shell=True)).start()
            time(2)
            threading.Thread(target=lambda: subprocess.run("dism /Online /Cleanup-Image /CheckHealth", shell=True)).start()
            time(2)
            threading.Thread(target=lambda: subprocess.run("dism /Online /Cleanup-Image /ScanHealth", shell=True)).start()
            time(2)
            threading.Thread(target=lambda: subprocess.run("dism /Online /Cleanup-Image /RestoreHealth", shell=True)).start()
            time(2)
            messagebox.showinfo(repair_sys_title, repair_sys_done_title)

def close(event=None):
    window.destroy()

resx = config['SystemRepair']['xsupportforresizability']
resy = config['SystemRepair']['ysupportforresizability']

def SystemRepair():
    global window
    window = Tk()
    window.title(system_repair_title)
    window.geometry("500x300")
    window.resizable(resx,resy)
    window.iconbitmap("Icon/adwmgui_system_repair.ico")
    window.configure(bg=window_bg)
    window.bind('<Control-w>', close)
    basic_sys_repair_label = Label(window, text=basic_sys_repair_title, anchor="w", justify=LEFT, font=("Arial", 12, "bold"), bg=label_bg, fg=label_fg)
    basic_sys_repair_label.pack(fill="x", anchor="w")
    systemrepair = Button(window, text=system_repair_title, command=lambda: RepairSystem(mode="manual"), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
    systemrepair.place(x=5, y=30)
    window.mainloop()