' Author: Daniel Godinez
' Date: 12/15/2017
' Python 3.6.3
import random

print(" ###Welcome to the password generator###")
chars ='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ.!@#$%&*'
num_pass = int(input('How many passwords do you want: '))
length = int(input('How many characters do you need?: '))
for p in range(num_pass):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print("Password below \n" + password)
