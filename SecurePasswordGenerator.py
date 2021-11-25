import random
from time import sleep
import colorama
import ctypes
from colorama import *
import os
def enterprogram():
    ctypes.windll.kernel32.SetConsoleTitleA("SecurePasswordGenerator - V2.1 - Owned By Zenperr - Updated By Rask")
    print("""
                                            ░██████╗██████╗░░██████╗░███╗░░██╗
                                            ██╔════╝██╔══██╗██╔════╝░████╗░██║
                                            ╚█████╗░██████╔╝██║░░██╗░██╔██╗██║
                                            ░╚═══██╗██╔═══╝░██║░░╚██╗██║╚████║
                                            ██████╔╝██║░░░░░╚██████╔╝██║░╚███║
                                            ╚═════╝░╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝
                            Tool Owned By Zenperr | Help: Raphiel/Raluvy95/Gam3rr | Edited: Rask
                                                            Update coming soon! (redesign)
                                                                                                                                        """)

    print("Loading...")
    sleep(2)
    print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "CONSOLE" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + "Thanks for using this tool!, select an option to continue")
    print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "1" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + "Login")
    lg = int(input('[~]: '))
    if lg == 1:
        os.system("cls");
        usr = str(input("Enter Your Username: "))
        os.system("cls");
        print("""
                                                ░██████╗██████╗░░██████╗░███╗░░██╗
                                                ██╔════╝██╔══██╗██╔════╝░████╗░██║
                                                ╚█████╗░██████╔╝██║░░██╗░██╔██╗██║
                                                ░╚═══██╗██╔═══╝░██║░░╚██╗██║╚████║
                                                ██████╔╝██║░░░░░╚██████╔╝██║░╚███║
                                                ╚═════╝░╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝
                                Tool Owned By Zenperr | Help: Raphiel/Raluvy95/Gam3rr | Edited: Rask
                                                            Update coming soon! (redesign)
                                                                                                                                            """)
        print(Fore.LIGHTMAGENTA_EX + "["  + Fore.LIGHTWHITE_EX + "CONSOLE" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + "Welcome back " + usr + ",select an option to continue ( Currently on version 2.1 )")
        print(Fore.LIGHTMAGENTA_EX + "["  + Fore.LIGHTWHITE_EX + "1" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Generator")
        print(Fore.LIGHTMAGENTA_EX + "["  + Fore.LIGHTWHITE_EX + "2" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Passwords (coming soon, not available")
        print(Fore.LIGHTMAGENTA_EX + "["  + Fore.LIGHTWHITE_EX + "3" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Change Logs")
        print(Fore.LIGHTMAGENTA_EX + "["  + Fore.LIGHTWHITE_EX + "4" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Info")
        ch1 = int(input('[~]: '))
        if ch1 == 1:
            clearConsole = lambda:os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clearConsole()
            print("""
                                                ░██████╗██████╗░░██████╗░███╗░░██╗
                                                ██╔════╝██╔══██╗██╔════╝░████╗░██║
                                                ╚█████╗░██████╔╝██║░░██╗░██╔██╗██║
                                                ░╚═══██╗██╔═══╝░██║░░╚██╗██║╚████║
                                                ██████╔╝██║░░░░░╚██████╔╝██║░╚███║
                                                ╚═════╝░╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝
                                Tool Owned By Zenperr | Help: Raphiel/Raluvy95/Gam3rr | Edited: Rask
                                                            Update coming soon! (redesign)
                                                                                                                                            """)
            randomShit = "!@#$%^&*"
            low = "avcdefghijklmnopqrstuvwxyz"
            high = low.upper()
            digit = "0123456789"

            times = input(Fore.LIGHTMAGENTA_EX + "How many passwords do you want? ")
            times = int(times)

            length = input(Fore.LIGHTMAGENTA_EX + "How many lengths do you want to generate? ")
            length = int(length)

            typepwd = input(Fore.LIGHTMAGENTA_EX + "For what do you need these passwords? ")
            if typepwd == '\n':
                typepwd = "untitled"

            typepwd = f" {typepwd} "

            print(Fore.LIGHTMAGENTA_EX + "\nHere's your generated password!")
            combined = low + high + digit + randomShit

            with open("passwords.txt", "a") as f:
                f.write(typepwd.center(40, "=") + "\n")

            for i in range(times):
                a = ""
                reason = type
                for i in range(length):
                    a += random.choice(combined)
                with open("passwords.txt", "a") as f:
                    f.write(a + "\n")
                print(a)
                sleep(2.3)

        if ch1 == 4:
            os.system("cls");
            clearConsole = lambda:os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clearConsole()
            print("""
                                                            ░██████╗██████╗░░██████╗░███╗░░██╗
                                                            ██╔════╝██╔══██╗██╔════╝░████╗░██║
                                                            ╚█████╗░██████╔╝██║░░██╗░██╔██╗██║
                                                            ░╚═══██╗██╔═══╝░██║░░╚██╗██║╚████║
                                                            ██████╔╝██║░░░░░╚██████╔╝██║░╚███║
                                                            ╚═════╝░╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝
                                            Tool Owned By Zenperr | Help: Raphiel/Raluvy95/Gam3rr | Edited: Rask
                                                            Update coming soon! (redesign)
                                                                                                                                                        """)
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "CONSOLE" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + "Thank you for using SPGN, here are the credits and info")
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "Version" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "2.1")
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "Owner" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Zenperr")
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "Helpers" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Raphiel/Raluvy95/Gam3rr")
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "Editor" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Rask")
            print(Fore.LIGHTMAGENTA_EX + "          This window will last for 15 seconds.")
            sleep(15)

        if ch1 == 3:
            clearConsole = lambda:os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clearConsole()
            print("""
                                                            ░██████╗██████╗░░██████╗░███╗░░██╗
                                                            ██╔════╝██╔══██╗██╔════╝░████╗░██║
                                                            ╚█████╗░██████╔╝██║░░██╗░██╔██╗██║
                                                            ░╚═══██╗██╔═══╝░██║░░╚██╗██║╚████║
                                                            ██████╔╝██║░░░░░╚██████╔╝██║░╚███║
                                                            ╚═════╝░╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝
                                            Tool Owned By Zenperr | Help: Raphiel/Raluvy95/Gam3rr | Edited: Rask
                                                            Update coming soon! (redesign)
                                                                                                                                                        """)

            print(Fore.LIGHTRED_EX + "CURRENTLY ON VERSION 2.1! \n Change log from when the program was released: \n V2.1 - Added the function passwords ( still WIP ), updated the prints. \n V2.0 - Little Fixes, added clear. \n V1.9 - Fixed the Info \n V1.8 - Fixes, added change log in the tool directly \n V1.7 - Fixes \n V1.6 - Redesign and more ( helped by rask-yo) \n V1.5 - Updated some prints. \n V1.4 - Passwords save, questions about the password. \n V1.3 - CMD with the password, smaller file, from 16 to 32 characters.(changable) \n V1.2 - From 15 to 16 characters, print updated. \n V1.1 - Welcome Message \n V1.0 - Tool released. \n              This window lasts for 30 seconds than it automatically closes.")
            sleep(30)

        if ch1 == 2:
            clearConsole = lambda:os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clearConsole()
            print("""
                                                            ░██████╗██████╗░░██████╗░███╗░░██╗
                                                            ██╔════╝██╔══██╗██╔════╝░████╗░██║
                                                            ╚█████╗░██████╔╝██║░░██╗░██╔██╗██║
                                                            ░╚═══██╗██╔═══╝░██║░░╚██╗██║╚████║
                                                            ██████╔╝██║░░░░░╚██████╔╝██║░╚███║
                                                            ╚═════╝░╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝
                                            Tool Owned By Zenperr | Help: Raphiel/Raluvy95/Gam3rr | Edited: Rask
                                                            Update coming soon! (redesign)
                                                                                                                                                        """)

            print(Fore.LIGHTCYAN_EX + "Currently Working in progress ( WIP ). This feature should get released after the redesign.")
            sleep(10)

def new_func():
    os.system("cls");









enterprogram()
