import smtplib
import time
from colorama import Fore
import os
import shutil
try:
    import psutil
    import keyboard
except ImportError:
    os.system('pip install keyboard psutil')
columns = shutil.get_terminal_size().columns
userdir = os.getenv("UserName")
parent_pid = os.getppid()
if psutil.Process(parent_pid).name() == 'powershell.exe':
    cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')
else:
    cls = lambda: print('\033[12A\033[2K', end='')
cls()
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
while True:
    print(Fore.LIGHTBLUE_EX+'\n╭'+'Put "help" in the console to view the list of commands'.center(columns-1, '─'))
    inputfunc = input("╰───Input action: ")
    cls()
    if "announce" in inputfunc:
        announcecontent = input("Input Announcement Content: ")
        with open("maillist.txt", "r") as maillist:
            for mail in maillist:
                to = listConvert(mail)
                sendEmail(to, announcecontent)
                print("Announcement sent!".center(columns, '=') + Fore.WHITE)
                time.sleep(1.0)
                cls()
    elif "add" in inputfunc:
        added = input("Email: ")
        with open("maillist.txt", "r") as maillist:
            mailtest = maillist.read()
            if mailtest == "":
                with open("maillist.txt", "a") as maillist:
                    maillist.write(f"{added}")
                    print(f"Added {added} to the email whitelist!".center(columns, '=')+Fore.WHITE)
                    time.sleep(1.0)
                    cls()
            else:
                with open("maillist.txt", "a") as maillist:
                    maillist.write(f", {added}")
                    print(f"Added {added} to the email whitelist!".center(columns, '=')+Fore.WHITE)
                    time.sleep(1.0)
                    cls()
    elif "removelist" in inputfunc:
        with open("maillist.txt", "w") as remove:
            remove.write("")
            print("Removed email whitelist!".center(columns, '=')+Fore.WHITE)
            time.sleep(1.0)
            cls()
    elif "exit" in inputfunc:
        cls()
        keyboard.send('ctrl+c')
        print(Fore.RED+"Exiting DO NOT PRESS ANYTHING DUE TO KEYBOARD INTERUPT".center(columns, "=")+Fore.WHITE)
        time.sleep(0.1)
        cls()
    elif "help" in inputfunc:
        cmdlist1 = ["1. exit | Exits the program", "2. announce | Announces something", "3. add | Adds a email address to the email whitelist", "4. removelist | Removes the email whitelist", "5. cls | Clears output"]
        lengths = []
        for item in cmdlist1:
            length = len(item)
            lengths.append(length)
        cmdlist2 = []
        for item in cmdlist1:
            spaces = max(lengths) - len(item)
            space = ''
            for i in range(spaces):
                space = space+' '
            cmdlist2.append(f'{item}{space}')
        cls()
        out = ''
        for item in cmdlist2:
            for item1 in [*item]:
                time.sleep(0.007)
                out = out + item1
                cls()
                print(Fore.GREEN+"Command list".center(columns, '─'))
                if cmdlist2.index(item) >= 1:
                    for i in range(cmdlist2.index(item)):
                        print(str(cmdlist2[i]).center(columns))
                spaces = max(lengths) - len(out)
                space = ''
                for i in range(spaces):
                    space = space+' '
                print(str(out+space).center(columns))
                print("Command list".center(columns, '─'))
            out = ''
    elif "reload" in inputfunc:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Reloading...")
        time.sleep(1.0)
        os.system('exit')
        os.system(f'python {__file__}')
        print(Fore.WHITE)
    elif "cls" in inputfunc:
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(Fore.RED + "Invalid option" + Fore.LIGHTBLUE_EX)
