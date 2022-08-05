import string
import random

ls1 = list(string.ascii_lowercase)
ls2 = list(string.ascii_uppercase)
ls3 = list(string.digits)
ls4 = list(string.punctuation)

char_number = input('Enter the number of the characters in your password: ')

while True:
    try:
        char_number = int(char_number)
        if char_number < 6:
            print('too small password lenth')
            char_number = input('Please enter at least 6 char: ')
        else:
            break
    except:
        char_number = input('Please enter numbers only: ')

random.shuffle(ls1)
random.shuffle(ls2)
random.shuffle(ls3)
random.shuffle(ls4)

pass_percent1 = round(char_number * (30/100))
pass_percent2 = round(char_number * (20/100))

password = []

for x in range(pass_percent1):
    password.append(ls1[x])
    password.append(ls2[x])

for x in range(pass_percent2):
    password.append(ls3[x])
    password.append(ls4[x])

random.shuffle(password)
password = ''.join(password)

print(password)
