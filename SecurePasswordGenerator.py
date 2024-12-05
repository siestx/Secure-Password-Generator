import random
from time import sleep
import colorama
import ctypes
from colorama import *
import os
from colorama import init, Fore, Back, Style

init()
def enterprogram():
    ctypes.windll.kernel32.SetConsoleTitleA("SecurePasswordGenerator - V2.2 - Owned By siestx")
    print("""
                                                ░██████╗██████╗░░██████╗░███╗░░██╗
                                                ██╔════╝██╔══██╗██╔════╝░████╗░██║
                                                ╚█████╗░██████╔╝██║░░██╗░██╔██╗██║
                                                ░╚═══██╗██╔═══╝░██║░░╚██╗██║╚████║
                                                ██████╔╝██║░░░░░╚██████╔╝██║░╚███║
                                                ╚═════╝░╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝
                                    Tool was made a long time ago by siestx with the help of others
                                            
                                                                                                                                        """)

    print("Loading...")
    sleep(1)
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
                                    Tool was made a long time ago by siestx with the help of others
                                                
                                                                                                                                            """)
        print(Fore.LIGHTMAGENTA_EX + "["  + Fore.LIGHTWHITE_EX + "CONSOLE" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + "Welcome back " + usr + ",select an option to continue ( Currently on version 2.2,1 )")
        print(Fore.LIGHTMAGENTA_EX + "["  + Fore.LIGHTWHITE_EX + "1" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Generator")
        print(Fore.LIGHTMAGENTA_EX + "["  + Fore.LIGHTWHITE_EX + "2" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "-was meant to be something-")
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
                                    Tool was made a long time ago by siestx with the help of others
                                                
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
                                    Tool was made a long time ago by siestx with the help of others
                                                            
                                                                                                                                                        """)
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "CONSOLE" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + "Thank you for using SPGN, here are the credits and info")
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "Version" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "2.2,1")
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "Owner" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "-")
            print(Fore.LIGHTMAGENTA_EX + "[" + Fore.LIGHTWHITE_EX + "Program" + Fore.LIGHTMAGENTA_EX + "]" + Fore.LIGHTWHITE_EX + " " + "Program is free to use, previously owned by zenperr")
            print(Fore.LIGHTMAGENTA_EX + "          This application is going to close in 15 seconds.")
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
                                    Tool was made a long time ago by siestx with the help of others
                                                            
                                                                                                                                                        """)

            print(Fore.LIGHTRED_EX + "CURRENTLY ON VERSION 2.2,1! \n Change log from when the program was released: \n V2.2,1 Disowning ( 8th of April 2023 ) \n V2.2 - ;) \n V2.1 - Added the function passwords ( still WIP ), updated the prints. \n V2.0 - Little Fixes, added clear. \n V1.9 - Fixed the Info \n V1.8 - Fixes, added change log in the tool directly \n V1.7 - Fixes \n V1.6 - Redesign and more ( helped by rask-yo) \n V1.5 - Updated some prints. \n V1.4 - Passwords save, questions about the password. \n V1.3 - CMD with the password, smaller file, from 16 to 32 characters.(changable) \n V1.2 - From 15 to 16 characters, print updated. \n V1.1 - Welcome Message \n V1.0 - Tool released. \n              This application is going to close in 30 seconds.")
            sleep(30)
            
        if ch1 == 0:
            clearConsole = lambda:os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clearConsole()
            print(Fore.GREEN + "Congratulaions! You found the secret easter egg ;D.\n This application will close in 15 seconds.")
            sleep(15)
            
        if ch1 == 2:       
            clearConsole = lambda:os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clearConsole()
            print(Fore.LIGHTMAGENTA_EX + "Hello, seems like you are still using this even tho it's not updated anymore. I, zenperr the one who made the program have gotten other projects that do not involve coding anymore and more like they now include editing so this program is left for use no copyrights no anything i don't mind if it's being used or something. Have a good day!\n\nThis application will close in 30 seconds")
            sleep(30)

def new_func():
    os.system("cls");









enterprogram()
