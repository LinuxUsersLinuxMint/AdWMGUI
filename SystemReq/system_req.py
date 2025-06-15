#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

from AdWMGUILang.lang import *
from Theme.theme import *

resx = config['SysRequirements']['xsupportforresizability']
resy = config['SysRequirements']['ysupportforresizability']

def close(event=None):
    window.destroy()

def sys_req():
    global window
    window = Tk()
    window.title(sys_req_title)
    window.geometry("1400x700")
    window.configure(bg=window_bg)
    window.resizable(FALSE,FALSE)
    sysreq_title = Label(window, text=sys_req_title, font=("Arial",12,"bold"), anchor="n", justify=LEFT, bg=label_bg, fg=label_fg)
    sysreq_title.pack(fill="x", anchor="w")
    minsysreq_title = Label(window, text=min_sys_req_title, font=("Arial",12,"bold"), bg=label_bg, fg=label_fg)
    minsysreq_title.place(x=150, y=26)
    recsysreq_title = Label(window, text=rec_sys_req_title, font=("Arial",12,"bold"), bg=label_bg, fg=label_fg)
    recsysreq_title.place(x=750, y=26)
    os_req = Label(window, text=os_req_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    os_req.place(x=5, y=60)
    cpu_req = Label(window, text=cpu_req_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    cpu_req.place(x=5, y=80)
    ram_req = Label(window, text=ram_req_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    ram_req.place(x=5, y=100)
    disk_type_req = Label(window, text=disk_type_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    disk_type_req.place(x=5, y=120)
    disk_size_req = Label(window, text=disk_size_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    disk_size_req.place(x=5, y=140)
    minsys_req_os = Label(window, text=min_sys_req_os_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    minsys_req_os.place(x=150, y=60)
    minsys_req_cpu = Label(window, text=min_sys_req_cpu_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    minsys_req_cpu.place(x=150, y=80)
    minsys_req_ram = Label(window, text=min_sys_req_ram_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    minsys_req_ram.place(x=150, y=100)
    minsys_req_disk_type = Label(window, text=min_sys_req_disk_type_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    minsys_req_disk_type.place(x=150, y=120)
    minsys_req_disk_size = Label(window, text=min_sys_req_disk_size_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    minsys_req_disk_size.place(x=150, y=140)
    recsys_req_os = Label(window, text=rec_sys_req_os_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    recsys_req_os.place(x=750, y=60)
    recsys_req_cpu = Label(window, text=rec_sys_req_cpu_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    recsys_req_cpu.place(x=750, y=80)
    recsys_req_ram = Label(window, text=rec_sys_req_ram_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    recsys_req_ram.place(x=750, y=100)
    recsys_req_disk_type = Label(window, text=rec_sys_req_disk_type_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    recsys_req_disk_type.place(x=750, y=120)
    recsys_req_disk_size = Label(window, text=rec_sys_req_disk_size_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    recsys_req_disk_size.place(x=750, y=140)
    note = Label(window, text=note_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    note.place(x=5, y=180)
    note_two = Label(window, text=note_two_title, font=("Arial",10,"bold"),  bg=label_bg, fg=label_fg)
    note_two.place(x=5, y=200)
    window.bind('<Control-w>', close)
    window.mainloop()