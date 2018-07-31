# Author: Daniel Godinez
# Date: 7/31/2018
# PassGen Version 1.2
# Python Version: 3.6.5

import random

#Introduction to application
print(" Welcome to passGen64, The Password Generator.")
print(" Provided by Daniel G.")
print(" With passGen64, generate as many passwords, however long you want them too!!")
    

def passGen():
    try:
        chars ='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ.!@#$%&*()'
        num_pass = int(input('How many passwords do you want: '))
        length = int(input('How many characters do you need?: '))
        print('Password(s) below: ')
        for p in range(num_pass):
            password = ''
            for c in range(length):
                password += random.choice(chars)
            print(password)
        print('Come back & have a good day!')
    except:
        print('Oh oh! Please try again')
# Call the Function
if __name__ == "__main__":
    passGen()
