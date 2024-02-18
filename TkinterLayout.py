# Tkinter Layout Managers: pack(), place() and grid().
# 1) Pack.
# 2) Place.
# 3) Grid.
#####################################################
#Layout and positioning of each of our Widgets.
def print_Function():
    print("Applied Data scientist Ahmed")
from tkinter import *
window = Tk()
window.title("My First GUI Program.")
window.minsize(width=500, height=500)
#Add more space around all Four edges.
#window.config(padx=20,pady=20)
window.config(padx=100,pady=200)
#Label.
my_Label = Label(text="I Am a Label", font=("Arial", 24,"bold"))
my_Label.config(text="New Text")
my_Label.grid(row=0,column=0)
#Able to Add space Around your Widgets.
my_Label.config(padx=50,pady=0)#Add space Around.
#New Button.
my_button = Button(text="Austin Texas", command=print_Function)
my_button.grid(row=0,column=2)
#Button.
button = Button(text="Click Me", command=print_Function)
button.grid(row=1,column=1)
#Entry.
input = Entry(width=30)
print(input.get())
input.grid(row=2, column=3)

window.mainloop()
#########################################
#########################################
#Grid.
#Row    Row     Row
#Column Column  Column
#Column Column  Column
#Column Column  Column
###########################################
###########################################
