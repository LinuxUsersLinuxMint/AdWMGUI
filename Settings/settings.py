#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

from AdWMGUILang.lang import *
from Theme.theme import *
import configparser

CONFIG_PATH = "Settings/settings.ini"

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

def set_theme(theme):
    global userTheme
    userTheme = theme
    if theme == "dark":
        theme_status.config(text=theme_status_title+" "+dark_theme_title.lower())
    elif theme == "light":
        theme_status.config(text=theme_status_title+" "+light_theme_title.lower())
    elif theme == "amoled":
        theme_status.config(text=theme_status_title+" "+amoled_theme_title.lower())
    config['Theme']['userTheme'] = userTheme
    with open(CONFIG_PATH, 'w') as configfile:
        config.write(configfile)

def set_langs(lang):
    global userLang
    userLang = lang
    if lang == "tr":
        language_status.config(text=language_status_title+" "+language_tr_title.lower())
    elif lang == "en":
        language_status.config(text=language_status_title+" "+language_en_title.lower())
    config['Language']['userLang'] = userLang
    with open(CONFIG_PATH, 'w') as configfile:
        config.write(configfile)

def set_resizability(resizability):
    global userResizability
    userResizability = resizability
    window_name_x = str(resizability_x_window_name.get())
    window_name_y = str(resizability_y_window_name.get())
    if resizability == "x.on":
        resizability_x_status.config(text=resizability_x_status_title+" "+on.lower())
        config[window_name_x]['xsupportforresizability'] = "True"
        with open(CONFIG_PATH, 'w') as configfile:
            config.write(configfile)
    elif resizability == "x.off":
        resizability_x_status.config(text=resizability_x_status_title+" "+off.lower())
        config[window_name_x]['xsupportforresizability'] = "False"
        with open(CONFIG_PATH, 'w') as configfile:
            config.write(configfile)
    elif resizability == "y.on":
        resizability_y_status.config(text=resizability_y_status_title+" "+on.lower())
        config[window_name_y]['ysupportforresizability'] = "True"
        with open(CONFIG_PATH, 'w') as configfile:
            config.write(configfile)
    elif resizability == "y.off":
        resizability_y_status.config(text=resizability_y_status_title+" "+off.lower())
        config[window_name_y]['ysupportforresizability'] = "False"
        with open(CONFIG_PATH, 'w') as configfile:
            config.write(configfile)

def close(event=None):
    window.destroy()

def Settings():
    global window
    resx = config['Settings']['xsupportforresizability']
    resy = config['Settings']['ysupportforresizability']
    global theme_status,language_status,resizability_x_status,resizability_y_status,custom_resolution_status,window,resizability_x_window_name,resizability_y_window_name
    window = Tk()
    window.title(settings_title)
    window.geometry("450x460")
    window.configure(bg=window_bg)
    window.resizable(resx,resy)
    theme_select = Label(window, text=theme_title, font=("Arial",12,"bold"), anchor="w", justify=LEFT, bg=label_bg, fg=label_fg)
    theme_select.pack(fill="x", anchor="w")
    dark_theme_btn = Button(window, text=dark_theme_title, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, command=lambda: set_theme("dark"))
    dark_theme_btn.place(x=5, y=35)
    light_theme_btn = Button(window, text=light_theme_title, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, command=lambda: set_theme("light"))
    light_theme_btn.place(x=60, y=35)
    amoled_theme_btn = Button(window, text=amoled_theme_title, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, command=lambda: set_theme("amoled"))
    amoled_theme_btn.place(x=115, y=35)
    theme_status = Label(window, text=theme_status_title, bg=label_bg, fg=label_fg)
    theme_status.place(y=65)
    language = Label(window, text=language_title, font=("Arial",12,"bold"), bg=label_bg, fg=label_fg)
    language.place(y=95)
    turkish_lang_btn = Button(window, text=language_tr_title, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, command=lambda: set_langs("tr"))
    turkish_lang_btn.place(x=5, y=130)
    english_lang_btn = Button(window, text=language_en_title, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, command=lambda: set_langs("en"))
    english_lang_btn.place(x=54, y=130)
    language_status = Label(window, text=language_status_title, bg=label_bg, fg=label_fg)
    language_status.place(y=160)
    support_for_resizability = Label(window, text=support_for_resizability_title, font=("Arial",12,"bold"), bg=label_bg, fg=label_fg)
    support_for_resizability.place(y=190)
    resizability_x = Label(window, text="X:", bg=label_bg, fg=label_fg)
    resizability_x.place(y=220)
    resizability_x_status = Label(window, text=resizability_x_status_title, bg=label_bg, fg=label_fg)
    resizability_x_status.place(y=245)
    resizability_x_on_btn = Button(window, text=on, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, command=lambda: set_resizability("x.on"))
    resizability_x_on_btn.place(x=15, y=220)
    resizability_x_off_btn = Button(window, text=off, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, command=lambda: set_resizability("x.off"))
    resizability_x_off_btn.place(x=50, y=220)
    resizability_x_window_name = Entry(window, width=20)
    resizability_x_window_name.place(x=100, y=220)
    resizability_y = Label(window, text="Y:", bg=label_bg, fg=label_fg)
    resizability_y.place(y=270)
    resizability_y_on_btn = Button(window, text=on, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, command=lambda: set_resizability("y.on"))
    resizability_y_on_btn.place(x=15, y=270)
    resizability_y_off_btn = Button(window, text=off, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, command=lambda: set_resizability("y.off"))
    resizability_y_off_btn.place(x=50, y=270)
    resizability_y_status = Label(window, text=resizability_y_status_title, bg=label_bg, fg=label_fg)
    resizability_y_status.place(y=295)
    resizability_y_window_name = Entry(window, width=20)
    resizability_y_window_name.place(x=100, y=270)
    if config['Theme']['usertheme'] == "dark":
        theme_status.config(text=theme_status_title+" "+dark_theme_title.lower())
    elif config['Theme']['usertheme'] == "light":
        theme_status.config(text=theme_status_title+" "+light_theme_title.lower())
    elif config['Theme']['usertheme'] == "amoled":
        theme_status.config(text=theme_status_title+" "+amoled_theme_title.lower())
    if config['Language']['userlang'] == "tr":
        language_status.config(text=language_status_title+" "+language_tr_title.lower())
    elif config['Language']['userlang'] == "en":
        language_status.config(text=language_status_title+" "+language_en_title.lower())
    window.bind('<Control-w>', close)
    window.mainloop()