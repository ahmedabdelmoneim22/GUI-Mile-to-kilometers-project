#"Python Tkinter Widgets":
#"Tkinter-Widgets".
#These little Components or
#controls of Graphical User Interface (GUI) are known as widgets in Tkinter.
#(Widgets):
#(1)Button.
#(2)Check-button.
#(3)Canvas.
#(4)Entry.
#(5)Frame.
#(6)Label.
#(7)Menu.
#(8)Menubutton.
#(9)Message.
#(10)Listbox.
#(11)Radiobutton.
#################
#Graphical User Interfaces with Tk.
#tkinter widgets documentation.
##################
from tkinter import *
# Create a new window and configurations.
window = Tk()#Create Object From Class.
# Window title().
window.title("Widget Examples")
# set the minimum size of the Tkinter window.
window.minsize(width=500, height=500)

# Labels.
# Create Label.
label = Label(text="This is old text")
# Change Label text.
label.config(text="This is new text")
# pack() organizes widgets in horizontal and vertical boxes
# that are limited to left, right, top, bottom positions offset.
label.pack()

#Buttons.
def action():
    print("Do something")
#calls action() when pressed.
button = Button(text="Click Me", command=action)
button.pack()

#Entries.
entry = Entry(width=30)
#Add Some text to Begin with.
#END:(tkinter.constants)
entry.insert(END, string="Some text to begin with.")
#Gets text in entry.
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()#Cursor Begin With Text Entry.
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0.
print(text.get("1.0", END))
text.pack()

#Spinbox.
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale.
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton.
# Prints 1 if On button checked, otherwise 0.
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar() #Create Object From Class.
checkbutton = Checkbutton(text="Is On?",
                          variable=checked_state,
                          command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton.
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()#Create Object.
#IntVar(): We can set integer data and
# can retrieve it as well using getter and setter methods.
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
###################
#Listbox.
def listbox_used(event):
    # Gets current selection from listbox.
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
# tells Python to run the Tkinter Event loop.
window.mainloop()
#################
#################
#################
