#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

from tkinter import messagebox
from AdWMFuncLib.Systemrepair import *
from AdWMFuncLib.Systemclean import *
from tkinter import font

def get_input():
            user_input = str(private_time_input.get("1.0", "end-1c"))
            print(user_input)
            os.system("cmd.exe /c shutdown -s -t {0}". format(user_input))

def shutdownpc(second):
     os.system("cmd.exe /c shutdown -s -t {0}". format(second))
     print(second)

def ShutdownPC():
    global private_time_input
    if messagebox.askyesno(adwmgui_txt_title, shutdownpc_askyesno_txt_title) == True:
        window = Tk()
        window.title(shutdownpc_title)
        window.geometry("500x500")
        window.resizable(FALSE,FALSE)
        quick_access = Label(window, text=quick_access_title, font=("Arial",12,"bold"), anchor="w", justify=LEFT)
        quick_access.pack(fill="x", anchor="w")
        zero_second = Button(window, text="0", width=10, command=lambda: shutdownpc(0))
        zero_second.place(x=5, y=35)
        five_second = Button(window, text="5", width=10, command=lambda: shutdownpc(5))
        five_second.place(x=85, y=35)
        ten_second = Button(window, text="10", width=10, command=lambda: shutdownpc(10))
        ten_second.place(x=165, y=35)
        fifteen_second = Button(window, text="15", width=10, command=lambda: shutdownpc(15))
        fifteen_second.place(x=245, y=35)
        twenty_second = Button(window, text="20", width=10, command=lambda: shutdownpc(20))
        twenty_second.place(x=325, y=35)
        twentyfive_second = Button(window, text="25", width=10, command=lambda: shutdownpc(25))
        twentyfive_second.place(x=405, y=35)
        thirty_second = Button(window, text="30", width=10, command=lambda: shutdownpc(30))
        thirty_second.place(x=5, y=70)
        thirtyfive_second = Button(window, text="35", width=10, command=lambda: shutdownpc(35))
        thirtyfive_second.place(x=85, y=70)
        fourty_second = Button(window, text="40", width=10, command=lambda: shutdownpc(40))
        fourty_second.place(x=165, y=70)
        fourtyfive_second = Button(window, text="45", width=10, command=lambda: shutdownpc(45))
        fourtyfive_second.place(x=245, y=70)
        fifty_second = Button(window, text="50", width=10, command=lambda: shutdownpc(50))
        fifty_second.place(x=325, y=70)
        fiftyfive_second = Button(window, text="55", width=10, command=lambda: shutdownpc(55))
        fiftyfive_second.place(x=405, y=70)
        sixty_second = Button(window, text="60", width=10, command=lambda: shutdownpc(60))
        sixty_second.place(x=5, y=105)
        private_time = Label(window, text=private_time_title, font=("Arial",12,"bold"), anchor="w", justify=LEFT)
        private_time.place(y=140)
        private_time_input = Text(window, width=15, height=1)
        private_time_input.place(x=5, y=170)
        private_time_button = Button(window, text=private_time_button_title, width=13, command=get_input)
        private_time_button.place(x=135, y=170)
        all_operations_shutdownpc = Label(window, text=all_operations_shutdownpc_title_, font=("Arial",12,"bold"), anchor="w", justify=LEFT)
        all_operations_shutdownpc.place(y=200)
        all_operations_shutdownpc_button = Button(window, text=all_operations_shutdownpc_title, command=all_operations_ShutdownPC)
        all_operations_shutdownpc_button.place(x=5, y=230)
        window.mainloop()
    else:
        print(shutdownpc_askyesno_cancel_txt_title)

def all_operations_ShutdownPC():
    if messagebox.askyesno(adwmgui_txt_title, shutdownpc_askyesno_txt_title) == True:
        time(0.5)
        OpenCleanmgr()
        time(0.5)
        AdvancedCleanup()
        time(0.5)
        RepairSystem()
        time(0.5)
        shutdownpc(0)
    else:
        print(shutdownpc_askyesno_cancel_txt_title)