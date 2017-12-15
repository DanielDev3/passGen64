# Developer: Daniel Godinez
# Version 1.0 | Created 11/29/2017
# email: danieltech64@gmail.com
from guizero import App, Combo, Text, TextBox, CheckBox, ButtonGroup, PushButton, info
import random
chars ='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ.!@#$%&*'

def getInteger():
    
def pass_gen():
    info("Password(s) Generated")
    print( film_choice.get() )
    print( vip_seat.get_value() )
    print( row_choice.get() )
    


app = App(title="Password Generator", width=300, height=200, layout="grid")
app_desc = Text(app, text="Welcome to the password Generator Application", grid=[0,0], align="left", size=14, font="Times New Roman", color="black")
num_pass_desc = Text(app, text="Enter the number of passwords needed", font="Times New Roman", grid=[1,0], align="left")
num_pass = TextBox(app, grid=[1,1], align="left")

len_desc = Text(app, text="How many charachters do you need", font="Times New Roman", grid=[2,0], align="left")
len_pass = TextBox(app, grid=[2,1], align="left")
get_pass = PushButton(app, command=pass_gen, text="Generate Password", grid=[3,1], align="left")

app.display()
#film_choice = Combo(app, options=["Star Wars", "Indiana Jones", "Batman"], grid=[0,1], align="left")
#film_description = Text(app, text="Which film?", grid=[0,0], align="left")
#vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")
#vip_seat_desc = Text(app, text="Seat type", grid=[1,0], align="left")
#row_choice = ButtonGroup(app, options=[ ["Front", "F"], ["Middle", "M"],["Back", "B"] ],
#selected="M", horizontal=True, grid=[2,1], align="left")
#row_choice_desc = Text(app, text="Seat Location", grid=[2,0], align="left")
#book_seats = PushButton(app, command=do_booking, text="Book seat", grid=[3,1], align="left")





#for p in range(num_pass):
#    password = ''
#    for c in range(length):
#        password += random.choice(chars)
#    print("Password below \n" + password)
