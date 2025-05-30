#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/LinuxUsersLinuxMint/AdWMGUI """

from tkinter import *
from tkinter import font

def set_tr():
    global userLang
    userLang = "TR"
    lang.destroy()

def set_en():
    global userLang
    userLang = "EN"
    lang.destroy()

lang = Tk()
lang.title("Select Language")
lang.iconphoto(False, PhotoImage(file="Icon/adwmgui_icon.png"))
lang.geometry("200x100")
lang.resizable(FALSE,FALSE)
lang_label = Label(lang, text="Select Language")
lang_label.pack()
btnfrm = Frame(lang)
btnfrm.pack()
lang_button_tr = Button(btnfrm, text="Türkçe",command=set_tr,width=10)
lang_button_tr.pack(side=LEFT)
lang_button_en = Button(btnfrm, text="English",command=set_en,width=10)
lang_button_en.pack(side=LEFT)
exit_button = Button(lang, text="Exit",command=lang.destroy,width=10)
exit_button.pack()
adwmgui_version_label = Label(lang,text="AdWMGUI v1.6", font=("Arial",10,"bold"))
adwmgui_version_label.pack()
lang.mainloop()

if userLang == "EN":
    windows_title = "AdWMGUI (Advanced Windows Manager GUI)"
    system_clean_title = "SystemClean"
    advanced_system_clean_title = "DISM WinSxS Folder clean"
    system_repair_title = "SystemRepair"
    about_title = "About"
    shutdownpc_title = "ShutdownPC"
    all_operations_shutdownpc_title = "Do all operations and then shut down the computer"
    app_information_title = "App knowledge:\n"
    app_name_txt = "App name: AdWMGUI (Advanced Windows Manager GUI)"
    app_version_txt = "Version: 1.6"
    app_version_type_txt = "Version type: Stable version"
    licence_information_title = "Licence information:\n"
    licence_name_txt = "Licence name: GPL"
    licence_version_txt = "Licence version: 2"
    full_licence_name_txt = "Full licence name: GPL2 (General Public License)"
    manufacturer_information_title = "Manufacturer information:\n"
    manufacturer_name_txt = "Manufacturer name: LinuxUsersLinuxMint"
    organization_txt = "Organization: LinuxUsersLinuxMint"
    website_information_title = "Website information:\n"
    organization_website_txt = "Organization website: https://linuxuserslinuxmint.github.io/"
    adwmgui_txt_title = "AdWMGUI"
    shutdownpc_askyesno_txt_title = "Are you sure you want to shutdown your computer?"
    shutdownpc_askyesno_cancel_txt_title = "Shutdown cancelled."
    show_msg_ask_title = "Show messages?"
    adv_cleanup_title = "AdvancedCleanup"
    adv_clnp_txt_title = "Advanced Cleanup..."
    adv_cleanup_step_one_txt_title = "Advanced Cleanup 1/2... (DISM.exe /Online /Cleanup-Image /AnalyzeComponentStore)"
    adv_cleanup_step_two_txt_title = "Advanced Cleanup 2/2... (DISM.exe /Online /Cleanup-Image /StartComponentCleanup)"
    adv_clnp_done_title = "Advanced Cleanup done!"
    repair_sys_title =  "RepairSystem"
    repair_sys_txt_title = "Repairing System..."
    repair_sys_step_one_title = "Repair System 1/4... (sfc /scannow)"
    repair_sys_step_two_title = "Repair System 2/4... (dism /Online /Cleanup-Image /CheckHealth)"
    repair_sys_step_three_title = "Repair System 3/4... (dism /Online /Cleanup-Image /ScanHealth)"
    repair_sys_step_four_title = "Repair System 4/4... (dism /Online /Cleanup-Image /RestoreHealth)"
    repair_sys_done_title = "Reapiring System done!"
    usertm_title = "After how many seconds should the computer be shut down?: "
    adwmgui_platform_error_title_txt = "AdWMGUI platform system error"
    adwmgui_platform_error_txt = "Sorry! You do not meet the Platform system requirement to use the AdWMGUI application."
if userLang == "TR":
    windows_title = "AdWMGUI (Gelişmiş Windows Yönetimi GUI)"
    system_clean_title = "Sistem Temizliği"
    advanced_system_clean_title = "DISM WinSxS Klasör temizliği"
    system_repair_title = "Sistem Onarımı"
    about_title = "Hakkımda"
    shutdownpc_title = "Bilgisayarı Kapat"
    all_operations_shutdownpc_title = "Tüm işlemleri yap ardından Bilgisayarı kapat"
    app_information_title = "Uygulama bilgisi:\n"
    app_name_txt = "Uygulama adı: AdWMGUI (Advanced Windows Manager GUI)"
    app_version_txt = "Sürüm: 1.6"
    app_version_type_txt = "Sürüm tipi: Stabil sürüm"
    licence_information_title = "Lisans bilgisi:\n"
    licence_name_txt = "Lisans adı: GPL"
    licence_version_txt = "Lisans sürümü: 2"
    full_licence_name_txt = "Tam lisans ismi: GPL2 (General Public License)"
    manufacturer_information_title = "Üretici bilgisi:\n"
    manufacturer_name_txt = "Program üreticisi: LinuxUsersLinuxMint"
    organization_txt = "Organizasyon: LinuxUsersLinuxMint"
    website_information_title = "Web site bilgisi:\n"
    organization_website_txt = "Organizasyon web sitesi: https://linuxuserslinuxmint.github.io/"
    adwmgui_txt_title = "AdWMGUI"
    shutdownpc_askyesno_txt_title = "Bilgisayarı kapatmak istediğinizden emin misiniz?"
    shutdownpc_askyesno_cancel_txt_title = "Kapatma iptal edildi."
    show_msg_ask_title = "Mesajlar gösterilsin mi?"
    adv_cleanup_title = "Gelişmiş Temizlik"
    adv_clnp_txt_title = "Gelişmiş Temizlik..."
    adv_cleanup_step_one_txt_title = "Gelişmiş Temizlik 1/2... (DISM.exe /Online /Cleanup-Image /AnalyzeComponentStore)"
    adv_cleanup_step_two_txt_title = "Gelişmiş Temizlik 2/2... (DISM.exe /Online /Cleanup-Image /StartComponentCleanup)"
    adv_clnp_done_title = "Gelişmiş Temizlik tamamlandı!"
    repair_sys_title =  "Sistem Onarımı"
    repair_sys_txt_title = "Sistem onarılıyor..."
    repair_sys_step_one_title = "Sistem onarımı 1/4... (sfc /scannow)"
    repair_sys_step_two_title = "Sistem Onarımı 2/4... (dism /Online /Cleanup-Image /CheckHealth)"
    repair_sys_step_three_title = "Sistem Onarımı 3/4... (dism /Online /Cleanup-Image /ScanHealth)"
    repair_sys_step_four_title = "Sistem Onarımı 4/4... (dism /Online /Cleanup-Image /RestoreHealth)"
    repair_sys_done_title = "Sistem Onarımı tamamlandı!"
    usertm_title = "Bilgisayar kaç saniye sonra kapatılsın?: "
    adwmgui_platform_error_title_txt = "AdWMGUI platform sistem hatası"
    adwmgui_platform_error_txt = "Üzgünüm! AdWMGUI uygulamasını kullanmak için Platform sistem gereksinimini karşılamıyorsunuz."