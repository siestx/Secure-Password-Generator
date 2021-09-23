import random
from time import sleep
print('Thanks for using this tool! Made with love by zenperr and helped by Raphiel, Gam3rr and Raluvy95.\nPlease press the key enter to generate more passwords!\n\n')

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