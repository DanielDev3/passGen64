# Author: Daniel Godinez
# Date: 12/15/2017
# PassGen Version 1.1
# Python Version: 3.6.3

import random

#Introduction to application
print(" ###Welcome to the Free password generator###")
print(" ###Provided by Daniel Godinez, danieldba1867@gmail.com###")
print(" ###With passGen, you can generate as many passwords as you want!###")


def passGen():
    try:
        chars ='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ.!@#$%&*'
        num_pass = int(input('How many passwords do you want: '))
        length = int(input('How many characters do you need?: '))

        for p in range(num_pass):
            password = ''
            for c in range(length):
                password += random.choice(chars)
            print("Password below: \n" + password)
        print("Come back & have a good day!")
    except:
        print("Error, please try again")
if __name__ == "__main__":
      passGen()
