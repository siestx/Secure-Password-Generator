import random
from time import sleep
import colorama
import ctypes
from colorama import *
import os
def enterprogram():
    ctypes.windll.kernel32.SetConsoleTitleA("SecurePasswordGenerator - V1.4 - Owned By Zenperr - Updated By Rask")
    print("""
                                            ░██████╗██████╗░░██████╗░███╗░░██╗
                                            ██╔════╝██╔══██╗██╔════╝░████╗░██║
                                            ╚█████╗░██████╔╝██║░░██╗░██╔██╗██║
                                            ░╚═══██╗██╔═══╝░██║░░╚██╗██║╚████║
                                            ██████╔╝██║░░░░░╚██████╔╝██║░╚███║
                                            ╚═════╝░╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝
                            Tool Owned By Zenperr | Help: Raphiel/Raluvy95/Gam3rr | Edited: Rask
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
                                                                                                                                            """)
        print(Fore.LIGHTMAGENTA_EX + "["  + Fore.LIGHTWHITE_EX + "CONSOLE" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + "Wlcome back " + usr + ",select an option to continue")
        print(Fore.LIGHTMAGENTA_EX + "["  + Fore.LIGHTWHITE_EX + "1" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Generator")
        print(Fore.LIGHTMAGENTA_EX + "["  + Fore.LIGHTWHITE_EX + "2" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Info")
        ch1 = int(input('[~]: '))
        if ch1 == 1:
            randomShit = "!@#$%^&*"
            low = "avcdefghijklmnopqrstuvwxyz"
            high = low.upper()
            digit = "0123456789"

            times = input("how many passwords do you want? ")
            times = int(times)

            length = input("How many lengths do you want to generate? ")
            length = int(length)

            typepwd = input("For what do you need these passwords? ")
            if typepwd == '\n':
                typepwd = "untitled"

            typepwd = f" {typepwd} "

            print("\nHere's your generated password!")
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
                sleep(0.5)

        if ch1 == 2:
            os.system("cls");
            print("""
                                                            ░██████╗██████╗░░██████╗░███╗░░██╗
                                                            ██╔════╝██╔══██╗██╔════╝░████╗░██║
                                                            ╚█████╗░██████╔╝██║░░██╗░██╔██╗██║
                                                            ░╚═══██╗██╔═══╝░██║░░╚██╗██║╚████║
                                                            ██████╔╝██║░░░░░╚██████╔╝██║░╚███║
                                                            ╚═════╝░╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝
                                            Tool Owned By Zenperr | Help: Raphiel/Raluvy95/Gam3rr | Edited: Rask
                                                                                                                                                        """)
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "CONSOLE" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + "Thank you for using SPGN, here are the credits and info")
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "Version" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "1.4")
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "Owner" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Zenperr")
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "Helpers" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Raphiel/Raluvy95/Gam3rr")
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "Editor" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Rask")












enterprogram()
