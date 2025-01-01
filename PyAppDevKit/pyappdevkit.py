#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
PyAppDevKit Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyAppDevKit All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/PyAppDevKit
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/PyAppDevKit"""

def time(number):
    while number > 0:
        number -= 1
        for _ in range(100000000):
            pass

def error_msg(error_dialog):
    print(error_dialog)

def exit_program_dialog_time(exit_dialog_msg,userTime):
    print(exit_dialog_msg)
    userTime = int(userTime)
    time(userTime)
    exit()

def exit_program_time(userTime):
    userTime = int(userTime)
    time(userTime)
    exit()

def exit_program_dialog(exit_dialog_msg):
    print(exit_dialog_msg)

""" Example Dialog (ExitSelectDialog): "Select the method to exit the program (0: Dialogue and Time entry, 1: Time entry only, 2: Dialogue entry only, 3: Normal exit (old style)): "
 Example Dialog (userTimeDialog): "After how many seconds should the program be closed?: "
 Example Dialog (exitDialog): "Exit program..."
 Example Dialog (errormsgDialog): "Invalid Command!" """

def all_exit(ExitSelectDialog,userTimeDialog,exitDialog,errormsgDialog):
    exit_select = int(input(ExitSelectDialog))
    exit_select = int(exit_select)
    if exit_select == 0:
        userTime = input(userTimeDialog)
        exit_program_dialog_time(exitDialog, userTime)
    elif exit_select == 1:
        userTime = input(userTimeDialog)
        exit_program_time(userTime)
    elif exit_select == 2:
        exit_program_dialog(exitDialog)
    elif exit_select == 3:
        exit()
    else:
        print(errormsgDialog)

def program_info(dialog_one,dialog_one_t,dialog_two,dialog_two_t,dialog_three,dialog_three_t,dialog_four,dialog_four_t,dialog_five,dialog_five_t,dialog_six,dialog_six_t,dialog_seven,dialog_seven_t,dialog_eigth,dialog_eight_t,dialog_nine,dialog_nine_t,dialog_ten,dialog_ten_t):
    print("{0} {1}". format(dialog_one,dialog_one_t))
    print("{0} {1}". format(dialog_two,dialog_two_t))
    print("{0} {1}". format(dialog_three,dialog_three_t))
    print("{0} {1}". format(dialog_four,dialog_four_t))
    print("{0} {1}". format(dialog_five,dialog_five_t))
    print("{0} {1}". format(dialog_six,dialog_six_t))
    print("{0} {1}". format(dialog_seven,dialog_seven_t))
    print("{0} {1}". format(dialog_eigth,dialog_eight_t))
    print("{0} {1}". format(dialog_nine,dialog_nine_t))
    print("{0} {1}". format(dialog_ten,dialog_ten_t))

def library_info(dialog_one,dialog_one_t,dialog_two,dialog_two_t,dialog_three,dialog_three_t,dialog_four,dialog_four_t,dialog_five,dialog_five_t,dialog_six,dialog_six_t,dialog_seven,dialog_seven_t,dialog_eigth,dialog_eight_t,dialog_nine,dialog_nine_t,dialog_ten,dialog_ten_t):
    print("{0} {1}". format(dialog_one,dialog_one_t))
    print("{0} {1}". format(dialog_two,dialog_two_t))
    print("{0} {1}". format(dialog_three,dialog_three_t))
    print("{0} {1}". format(dialog_four,dialog_four_t))
    print("{0} {1}". format(dialog_five,dialog_five_t))
    print("{0} {1}". format(dialog_six,dialog_six_t))
    print("{0} {1}". format(dialog_seven,dialog_seven_t))
    print("{0} {1}". format(dialog_eigth,dialog_eight_t))
    print("{0} {1}". format(dialog_nine,dialog_nine_t))
    print("{0} {1}". format(dialog_ten,dialog_ten_t))

def program_welcome_msg(welcome_msg,cfg,cfg_,appname,libname,websitelink):
    print(welcome_msg)
    if cfg == 1:
        print(websitelink)
    elif cfg == 0:
        if cfg_ == "lib":
            library_info("Library Name: ",libname,"","","","","","","","","","","","","","","","","","")
        elif cfg_ == "app":
            program_info("Program Name: ",appname,"","","","","","","","","","","","","","","","","","")
        else:
            error_msg("Invalid definition!")