import random
from time import sleep

print(+ """
   _____ ____  ______
  / ___// __ \/ ____/
  \__ \/ /_/ / / __  
 ___/ / ____/ /_/ /  
/____/_/    \____/                         
""")  #  https://patorjk.com
print('Thanks for using this tool! Made with love by zenperr and helped by Raphiel, Gam3rr and Raluvy95.\n\n')

randomShit = "!@#$%^&*"
low = "avcdefghijklmnopqrstuvwxyz"
high = low.upper()
digit = "0123456789"

times = input("How many passwords do you want? ")
times = int(times)

length = input("How many lengths do you want the password/s to be? ")
length = int(length)

typepwd = input("For what do you need these password/s? ")
if typepwd == '\n':
    typepwd = "untitled"

typepwd = f" {typepwd} "

print("\nHere is/are your generated Password/s. Your passwords will also be stored in a notepad named Passwords.")
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
    sleep(10.0)
