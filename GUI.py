##"Creating Windows and Labels with Tkinter"
##import tkinter
##window = tkinter.Tk()
##window.title("My First GUI Program")
##window.minsize(width=500,height=300)
###Label.
##my_label = tkinter.Label(text="I Am a Label",font=("Arial",24,"bold"))
##my_label.pack()#(side="left")
##import turtle
##tim = turtle.Turtle()
###tim.write()
##window.mainloop()
###Arguments with Default Values.
#def my_function(a=1, b=2, c=3):
#    print(f"Do this with {a}")
#    print(f"Then do this with {b}")
#    print(f"Finally do this with {c}")
#my_function(b=5)
#######################################
#######################################
#print("*"*30)
##*args: Many Positional Arguments.
#print("Unlimited Arguments")
#def add(n1, n2):
#    return n1 + n2
#print(add(n1=10,n2=15))
##Unlimited Arguments.
#def add(*args):
#    print(args)
#    #for n in args:
#    #    print(n)
#add(3,5,7,8)
############################
############################
#Tcl-->>(tk Documentation).
import tkinter
from tkinter import *
window = tkinter.Tk()#Create Tkinter Window.
window.title("My First GUI Program")#Create Title.
window.minsize(width=500,height=300)#set the window Size.
#Label.
my_label = tkinter.Label(text="I Am a Label",font=("Arial",24,"bold"))
my_label.pack()#(side="left")
#Change Text.
#my_label["text"] = "New Text"
#my_label.config(text="New Text")
#################################
#Button.
def button_clicked():
    print("I got clicked")
    # Change Label Text When Clicked.
    #my_label.config(text="Button Got Clicked")
    my_label.config(text=f"{input.get()}")
button = Button(text="Click Me",command=button_clicked)
button.pack()
#Entry.
input = Entry(width=20)
input.pack()
#Other Tkinter Widgets: Radio buttons, Scales, Check buttons and more.

my_label.mainloop()
#Tkinter Widgets:
#Label.
#Buttons.
#Entry.
#Text.
#Text Entry Box.
#Spinbox.-->>(a sort of Counter).
#Scale.
#Check-button.
#Radio-button.
#Listbox.
#################################
#################################



