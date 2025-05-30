#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

from AdWMGUILang.lang import *

def AboutMsgBox():
    about = Tk()
    about.title(about_title)
    about.geometry("500x500")
    about.resizable(FALSE,FALSE)
    about_label = Label(about, text=app_information_title, font=("Arial", 12, "bold"), anchor="w", justify=LEFT)
    about_label.pack(fill="x", anchor="w")
    app_name = Label(about, text=app_name_txt, anchor="w", justify=LEFT)
    app_name.pack(fill="x", anchor="w")
    app_version = Label(about, text=app_version_txt, anchor="w", justify=LEFT)
    app_version.pack(fill="x", anchor="w")
    version_type = Label(about, text=app_version_type_txt, anchor="w", justify=LEFT)
    version_type.pack(fill="x", anchor="w")
    licence_information = Label(about, text=licence_information_title, font=("Arial",12,"bold"),anchor="w",justify=LEFT)
    licence_information.pack(fill="x", anchor="w")
    licence_name = Label(about, text=licence_name_txt, anchor="w", justify=LEFT)
    licence_name.pack(fill="x", anchor="w")
    licence_version = Label(about, text=licence_version_txt, anchor="w", justify=LEFT)
    licence_version.pack(fill="x", anchor="w")
    full_licence_name = Label(about, text=full_licence_name_txt, anchor="w", justify=LEFT)
    full_licence_name.pack(fill="x", anchor="w")
    creator_information = Label(about, text=manufacturer_information_title, font=("Arial",12,"bold"), anchor="w", justify=LEFT)
    creator_information.pack(fill="x", anchor="w")
    creator_name = Label(about, text=manufacturer_name_txt, anchor="w", justify=LEFT)
    creator_name.pack(fill="x", anchor="w")
    organization = Label(about, text=organization_txt, anchor="w", justify=LEFT)
    organization.pack(fill="x", anchor="w")
    website_information = Label(about, text=website_information_title, font=("Arial",12,"bold"), anchor="w", justify=LEFT)
    website_information.pack(fill="x", anchor="w")
    organization_website = Label(about, text=organization_website_txt, anchor="w", justify=LEFT)
    organization_website.pack(fill="x", anchor="w")
    about.mainloop()