import smtplib
import time
from colorama import init
from colorama import Fore as FG
import os
import shutil
import subprocess
try:
    import psutil
    import keyboard
except ImportError:
    os.system('pip install keyboard psutil')
columns = shutil.get_terminal_size().columns
userdir = os.getenv("UserName")
parent_pid = os.getppid()
init()
cls2 = lambda: os.system('cls' if os.name == 'nt' else 'clear')
# Set terminal level for ANSI code usage
os.system(r"powershell -Command Set-ItemProperty HKCU:\Console VirtualTerminalLevel -Type DWORD 1")
cls1 = lambda: print('\033[12A\033[2K', end='')
cls2()
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('edugabri1217@gmail.com', 'Input app password')
    server.sendmail('edugabri1217@gmail.com', to, content)
    server.close()
def listConvert(string):
    out = str(string).split(",")
    return out
inputfunc = ''
while True:
    print(FG.LIGHTBLUE_EX+'╭'+'Type "help" in the console to view the list of commands'.center(columns-2, '─')+'╯')
    inputfunc = input("╰───Input action: "+FG.YELLOW,)
    print(FG.LIGHTBLUE_EX)
    cls1()
    if "announce" in inputfunc:
        cls2()
        announcecontent = input("Input Announcement Content: ")
        with open("maillist.txt", "r") as maillist:
            for mail in maillist:
                to = listConvert(mail)
                sendEmail(to, announcecontent)
                print("Announcement sent!".center(columns, '=') + FG.WHITE)
                time.sleep(1.0)
                cls1()
    elif "add" in inputfunc:
        cls2()
        added = input("Email: ")
        with open("maillist.txt", "r") as maillist:
            mailtest = maillist.read()
            if mailtest == "":
                with open("maillist.txt", "a") as maillist:
                    maillist.write(f"{added}")
                    cls2()
                    print(f"Added {added} to the email whitelist!".center(columns, '=')+FG.WHITE)
                    time.sleep(1.0)
                    cls1()
            else:
                with open("maillist.txt", "a") as maillist:
                    maillist.write(f", {added}")
                    print(f"Added {added} to the email whitelist!".center(columns, '=')+FG.WHITE)
                    time.sleep(1.0)
                    cls1()
    elif "removelist" in inputfunc:
        with open("maillist.txt", "w") as remove:
            remove.write("")
            cls2()
            print("Removed email whitelist!".center(columns, '=')+FG.WHITE)
            time.sleep(1.0)
            cls1()
    elif "exit" in inputfunc:
        cls1()
        keyboard.send('ctrl+c')
        print(FG.RED+"Exiting DO NOT PRESS ANYTHING DUE TO KEYBOARD INTERRUPT".center(columns, "=")+FG.WHITE)
        time.sleep(0.1)
        cls1()
    elif "help" in inputfunc:
        cmdlist1 = ["1. exit | Exits the program", "2. announce | Announces something", "3. add | Adds a email address to the email whitelist", "4. removelist | Removes the email whitelist", "5. cls | Clears output", "6. shell | Opens a powershell instance using subprocess for debugging"]
        lengths = []
        for item in cmdlist1:
            lengths.append(len(item))
        cmdlist2 = []
        for item in cmdlist1:
            spaces = max(lengths) - len(item)
            space = ''
            for i in range(spaces):
                space = space+' '
            cmdlist2.append(f'{item}{space}')
        cls2()
        out = ''
        for item in cmdlist2:
            for item1 in [*item]:
                time.sleep(0.009)
                out = out + item1
                cls1()
                print(FG.LIGHTBLUE_EX+'╭'+"Command list".center(columns-2, '─')+'╯'+FG.GREEN)
                if cmdlist2.index(item) >= 1:
                    for i in range(cmdlist2.index(item)):
                        print(FG.LIGHTBLUE_EX+'│'+FG.GREEN+str(cmdlist2[i]).center(columns-1))
                spaces = max(lengths) - len(out)
                space = ''
                for i in range(spaces):
                    space = space+' '
                print(FG.LIGHTBLUE_EX+'│'+FG.GREEN+str(out+space).center(columns-1))
                if cmdlist2.index(item) == len(cmdlist2)-1:
                    print(FG.LIGHTBLUE_EX+'╰'+"Command list".center(columns-2, '─')+'╮')
                else:
                    print(FG.LIGHTBLUE_EX+'╰'+"Command list".center(columns-2, '─')+'─')
            out = ''
    elif "reload" in inputfunc:
        cls2()
        print("Reloading...")
        time.sleep(1.0)
        os.system('exit')
        os.system(f'python {__file__}')
        print(FG.WHITE)
    elif "cls" in inputfunc:
        cls2()
    elif "shell" in inputfunc:
        from powershell import __main__
        __main__()
    else:
        cls2()
        print(FG.RED + "Invalid option."+FG.CYAN+" Type 'shell' to run commands into shell" + FG.LIGHTBLUE_EX)
