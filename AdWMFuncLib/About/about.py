#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

from AdWMGUILang.lang import *
from Theme.theme import *

resx = config['About']['xsupportforresizability']
resy = config['About']['ysupportforresizability']

def close(event=None):
    window.destroy()

def About():
    global window
    window = Tk()
    window.title(about_title)
    window.geometry("500x500")
    window.resizable(resx,resy)
    window.configure(bg=window_bg)
    window.iconbitmap("Icon/adwmgui_about.ico")
    about_label = Label(window, text=app_information_title, font=("Arial", 12, "bold"), anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    about_label.pack(fill="x", anchor="w")
    app_name = Label(window, text=app_name_txt, anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    app_name.pack(fill="x", anchor="w")
    app_version = Label(window, text=app_version_txt, anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    app_version.pack(fill="x", anchor="w")
    version_type = Label(window, text=app_version_type_txt, anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    version_type.pack(fill="x", anchor="w")
    licence_information = Label(window, text=licence_information_title, font=("Arial",12,"bold"),anchor="w",justify=LEFT, bg=label_bg, fg=label_fg)
    licence_information.pack(fill="x", anchor="w")
    licence_name = Label(window, text=licence_name_txt, anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    licence_name.pack(fill="x", anchor="w")
    licence_version = Label(window, text=licence_version_txt, anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    licence_version.pack(fill="x", anchor="w")
    full_licence_name = Label(window, text=full_licence_name_txt, anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    full_licence_name.pack(fill="x", anchor="w")
    creator_information = Label(window, text=manufacturer_information_title, font=("Arial",12,"bold"), anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    creator_information.pack(fill="x", anchor="w")
    creator_name = Label(window, text=manufacturer_name_txt, anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    creator_name.pack(fill="x", anchor="w")
    organization = Label(window, text=organization_txt, anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    organization.pack(fill="x", anchor="w")
    website_information = Label(window, text=website_information_title, font=("Arial",12,"bold"), anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    website_information.pack(fill="x", anchor="w")
    organization_website = Label(window, text=organization_website_txt, anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    organization_website.pack(fill="x", anchor="w")
    window.bind('<Control-w>', close)
    window.mainloop() 