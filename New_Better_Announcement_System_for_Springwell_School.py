import smtplib
import colorama
import time
from colorama import Fore
import os
import shutil
columns = shutil.get_terminal_size().columns
userdir = os.getenv("UserName")
clear = lambda: os.system('cls')
clear()
print(Fore.LIGHTBLUE_EX+'Put "commandlist" in the console to view the list of commands'.center(columns))
inputfunc = input("Input action: ")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('edugabri1217@gmail.com', 'euxqsquafrfzrngs')
    server.sendmail('edugabri1217@gmail.com', to, content)
    server.close()
def listConvert(string):
    out = list(string.split(","))
    return out
if "announce" in inputfunc:
    announcecontent = input("Input Announcement Content: ")
    with open("maillist.txt", "r") as maillist:
        for mail in maillist:
            to = listConvert(mail)
            sendEmail(to, announcecontent)
            print("Announcement sent!".center(columns) + Fore.WHITE)
            time.sleep(1.0)
            clear()
elif "add" in inputfunc:
    added = input("Email: ")
    with open("maillist.txt", "r") as maillist:
        mailtest = maillist.read()
        if mailtest == "":
            with open("maillist.txt", "a") as maillist:
                maillist.write(f"{added}")
                print(f"Added {added} to the email whitelist!".center(columns)+Fore.WHITE)
                time.sleep(1.0)
                clear()
        else:
            with open("maillist.txt", "a") as maillist:
                maillist.write(f", {added}")
                print(f"Added {added} to the email whitelist!".center(columns)+Fore.WHITE)
                time.sleep(1.0)
                clear()
elif "removelist" in inputfunc:
    with open("maillist.txt", "w") as remove:
        remove.write("")
        print("Removed email whitelist!".center(columns)+Fore.WHITE)
        time.sleep(1.0)
        clear()
elif "exit" in inputfunc:
    clear()
    print(Fore.RED+"Exitted".center(columns) + Fore.WHITE)
    time.sleep(1.0)
    clear()
    exit()
elif "commandlist" in inputfunc:
    print(Fore.LIGHTBLUE_EX+"---------------------------Command list-------------------------".center(columns))
    print("exit|Exits the program".center(columns))
    print("announce|Announces something".center(columns))
    print("add|Adds a email address to the email whitelist".center(columns))
    print("removelist|Removes the email whitelist".center(columns))
    print(Fore.LIGHTBLUE_EX+"---------------------------Command list-------------------------".center(columns)+Fore.WHITE)
elif "reload" in inputfunc:
    print("Reloading...")
    time.sleep(1.0)
    clear()
    os.system('exit')
    os.system(f"C:/Users/{userdir}/AppData/Local/Programs/Python/Python310/python.exe c:/Users/family/New_Better_Announcement_System_for_Springwell_School.py")
    print(Fore.WHITE)
else:
    print(Fore.RED + "Invalid option")
    print(Fore.WHITE)
