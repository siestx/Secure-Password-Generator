print('Thanks for using this tool! Made with love by zenperr and helped by Raphiel and Gam3rr.')

import random
randomShit = "!@#$%^&*"
low = "avcdefghijklmnopqrstuvwxyz"
high = low.upper()
digit = "0123456789"
a = ""
combined = low + high + digit + randomShit
for i in range(32):
    a += random.choice(combined)
print(a)
input()