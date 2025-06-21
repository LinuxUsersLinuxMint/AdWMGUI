#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

import os
from tkinter import messagebox
from AdWMFuncLib.Systemrepair import *
from AdWMFuncLib.Systemclean import *
from tkinter import font
from Theme.theme import *

def get_input():
            user_input = str(private_time_input.get())
            shutdownpc(user_input)

def shutdownpc(second):
     os.system("cmd.exe /c shutdown -s -t {0}". format(second))

resx = config['ShutdownPC']['xsupportforresizability']
resy = config['ShutdownPC']['ysupportforresizability']

def close(event=None):
    window.destroy()

def ShutdownPC():
    global window
    global private_time_input
    if messagebox.askyesno(adwmgui_txt_title, shutdownpc_askyesno_txt_title) == True:
        window = Tk()
        window.title(shutdownpc_title)
        window.geometry("500x500")
        window.resizable(resx,resy)
        window.iconbitmap("Icon/adwmgui_shutdown_pc.ico")
        window.configure(bg=window_bg)
        quick_access = Label(window, text=quick_access_title, font=("Arial",12,"bold"), anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
        quick_access.pack(fill="x", anchor="w")
        zero_second = Button(window, text="0", width=10, command=lambda: shutdownpc(0), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        zero_second.place(x=5, y=35)
        five_second = Button(window, text="5", width=10, command=lambda: shutdownpc(5), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        five_second.place(x=85, y=35)
        ten_second = Button(window, text="10", width=10, command=lambda: shutdownpc(10), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        ten_second.place(x=165, y=35)
        fifteen_second = Button(window, text="15", width=10, command=lambda: shutdownpc(15), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        fifteen_second.place(x=245, y=35)
        twenty_second = Button(window, text="20", width=10, command=lambda: shutdownpc(20), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        twenty_second.place(x=325, y=35)
        twentyfive_second = Button(window, text="25", width=10, command=lambda: shutdownpc(25), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        twentyfive_second.place(x=405, y=35)
        thirty_second = Button(window, text="30", width=10, command=lambda: shutdownpc(30), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        thirty_second.place(x=5, y=70)
        thirtyfive_second = Button(window, text="35", width=10, command=lambda: shutdownpc(35), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        thirtyfive_second.place(x=85, y=70)
        fourty_second = Button(window, text="40", width=10, command=lambda: shutdownpc(40), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        fourty_second.place(x=165, y=70)
        fourtyfive_second = Button(window, text="45", width=10, command=lambda: shutdownpc(45), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        fourtyfive_second.place(x=245, y=70)
        fifty_second = Button(window, text="50", width=10, command=lambda: shutdownpc(50), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        fifty_second.place(x=325, y=70)
        fiftyfive_second = Button(window, text="55", width=10, command=lambda: shutdownpc(55), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        fiftyfive_second.place(x=405, y=70)
        sixty_second = Button(window, text="60", width=10, command=lambda: shutdownpc(60), bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        sixty_second.place(x=5, y=105)
        private_time = Label(window, text=private_time_title, font=("Arial",12,"bold"), bg=label_bg, fg=label_fg)
        private_time.place(y=140)
        private_time_input = Entry(window, width=20, font=("Arial",12,"bold"), bg=entry_bg, fg=entry_fg, insertbackground=entry_instert_bg)
        private_time_input.place(x=5, y=170)
        private_time_button = Button(window, text=private_time_button_title, width=13, command=get_input, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        private_time_button.place(x=195, y=170)
        all_operations_shutdownpc = Label(window, text=all_operations_shutdownpc_title_, font=("Arial",12,"bold"), bg=label_bg, fg=label_fg)
        all_operations_shutdownpc.place(y=200)
        all_operations_shutdownpc_button = Button(window, text=all_operations_shutdownpc_title, command=all_operations_ShutdownPC, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
        all_operations_shutdownpc_button.place(x=5, y=230)
        window.bind('<Control-w>', close)
        window.mainloop()
    else:
        print(shutdownpc_askyesno_cancel_txt_title)

def all_operations_ShutdownPC():
    if messagebox.askyesno(adwmgui_txt_title, shutdownpc_askyesno_txt_title) == True:
        time(0.5)
        Cleanmgr()
        time(0.5)
        DISMClean(mode="auto")
        time(0.5)
        RepairSystem(mode="auto")
        time(0.5)
        shutdownpc(0)
    else:
        print(shutdownpc_askyesno_cancel_txt_title)
