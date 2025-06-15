#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

import configparser

config = configparser.ConfigParser()
config.read("Settings/settings.ini")

userTheme = config['Theme']['userTheme']

if userTheme == "dark":
    window_bg = "#2e2e2e"
    button_bg = "#3a3a3a"
    button_fg = "#dcdcdc"
    button_active_bg = "#666666"
    button_active_fg = "#dcdcdc"
    label_bg = "#2e2e2e"
    label_fg = "#dcdcdc"
    entry_bg = "#3a3a3a"
    entry_fg = "#dcdcdc"
    entry_instert_bg = "#dcdcdc"
elif userTheme == "light":
    window_bg = None
    button_bg = None
    button_fg = None
    button_active_bg = None
    button_active_fg = None
    label_bg = None
    label_fg = None
    entry_bg = None
    entry_fg = None
    entry_instert_bg = None
elif userTheme == "amoled":
    window_bg = "black"
    button_bg = "black"
    button_fg = "#dcdcdc"
    button_active_bg = "black"
    button_active_fg = "#dcdcdc"
    label_bg = "black"
    label_fg = "#dcdcdc"
    entry_bg = "#3a3a3a"
    entry_fg = "#dcdcdc"
    entry_instert_bg = "#dcdcdc"
else:
    raise ValueError("Invalid theme")