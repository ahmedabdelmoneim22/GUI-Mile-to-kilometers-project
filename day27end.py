"""
Python GUI development with Tkinter!
imports all symbols from A module;
from tkinter import Tk, Button, Label;
"""
from tkinter import *
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
# The-main-window-object;
window = Tk()
# The-main-window-title;
window.title("My First GUI Program")
# size-of-the-main-window;
window.minsize(width=500, height=300)
# Add-padding-around-the-window;
window.config(padx=100, pady=200)
#Label;
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
"""Convert text to New-Text"""
my_label.config(text="New Text")
my_label.grid(column=0, row=0, columnspan=2)
my_label.config(padx=50, pady=50)
#Button;
button = Button(text="Click Me",
                command=button_clicked,fg="white",background="red")
button.grid(column=0, row=1)
new_button = Button(text="New Button",fg="white",background="red")
new_button.grid(column=1, row=1)
#Entry;
input = Entry(window,width=30)
print(input.get())
input.grid(column=0, row=2,columnspan=2)
window.mainloop()
#################
# *args: Positional Variable-Length Arguments;
def add(*args):
    # print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3, 5, 6, 2, 1, 7, 4, 3))
# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)
calculate(2, add=3, multiply=5)
# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
# Create Instance from class Car();
my_car = Car(make="Nissan", model="Skyline",
             colour="red", seats=4)
print(my_car.model)
print(my_car.make)
print(my_car.colour)
print(my_car.seats)
###################
"""A Dictionary:->>Arguments to a function.
>>The 2 ** Notation Allows you to Pass a Dictionary{Key:Value};
"""
def WorkLive(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(f"Working in {kwargs.get("state")},Live in Austin,{kwargs.get("Lovestate")}")
# Calling the function with keyword Arguments;
WorkLive(name="Alice", age=30, city="New York",
         state="California", Lovestate="Texas")
"""
>>Tuple(), List[];
>>The 1 * Notation Allows you to Pass Tuple(),List[];
"""
def MyLove(*args):
    for arg in args:
        print(arg)
#>>Calling the function with Positional-Arguments();
print("List Positional Argument",MyLove([1, 2, 3, 4, 5]))
print("Tuple Positional Argument",MyLove(1,2,3,4,5))


