"""
>>Mile to Kilometers Converter Project.
"""
# I WanT Change The World.
# import all tkinter objects from library;
from tkinter import *
def miles_to_km():
    """Get the miles from the Entry()"""
    miles = float(miles_Entry.get())
    """Convert Miles to Kilometers"""
    km = round(miles * 1.609)
    """Convert The Label Text to km"""
    mid_Label.config(text = km)
#############
window = Tk() # Main Window;
window.title("Mile to Km Converter") # Window title;
window.minsize(width=300, height=300) # Window size;
window.config(bg="red") # Background color;
window.config(padx=20, pady=20) # Padding space;
miles_Entry = Entry(width=20) # miles Entry();
miles_Entry.grid(row=0,column=1)# Placement;
miles_Label = Label(text="Miles",font=("Arial", 15,"bold"),bg="red")
miles_Label.grid(row=0,column=2)
left_Label = Label(text="is equal to",font=("Arial", 15,"bold"),bg="red")
left_Label.grid(row=1, column=0)
mid_Label = Label(text="0",font=("Arial", 15,"bold"),bg="red")
mid_Label.grid(row=1, column=1)
right_Label = Label(text="Km",font=("Arial", 15,"bold"),
                    width=4,bg="red")
right_Label.grid(row=1,column=2)
calculate_Button = Button(text="Calculate",width=15,command=miles_to_km)
calculate_Button.grid(row=2,column=1)
"""Function call keeps your Tkinter Application Running"""
window.mainloop()
################


