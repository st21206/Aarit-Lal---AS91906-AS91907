from tkinter import *
from PIL import ImageTk, Image, ImageFont, ImageDraw
from datetime import datetime
from tkinter import messagebox


#make a window
root = Tk()
root.title("Aarit's Space Quiz")
root.geometry('600x650')

#Add text to font
def add_it():
    pass

#get width & height of screen
width= root.winfo_screenwidth()
height= root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d" % (width, height))
root.resizable(True, True)

#Defining background
Space_Background = PhotoImage(file='images/Space_Background_Image.png')

#labels
my_label = Label (root, image=Space_Background)
my_label.pack(pady=20)

"""# put image in a label and place label as background
imgTemp = Image.open("/Users/admiralaarit/Desktop/Space_Background_Image.png")
img2 = imgTemp.resize((width,height))
img = ImageTk.PhotoImage(img2)

label = Label(root,image=img)
label.pack(side='top',fill=Y,expand=True)"""

#Text 2.0, implementing a entry box
entry_box = Entry(root, font=('Helvetica', 24))
entry_box.pack(pady=20)

#Button
my_button = Button(root, text="Enter the Year you were Born in to Continue",
    command=add_it, font=('Helvetica', 24))
my_button.pack(pady=20)

"""#text, welcome and boundary testing through age, ages 0-8 not allowed
def age():
    pass

my_label = Label(root, text='Enter the Year you were Born to Continue', font=('Helvetica', 24))
my_label.pack(pady = 20)

#Entry Boxes
my_entry = Entry(root, font=('Helvetica', 18))
my_entry.pack(pady=20)

#Buttons
my_button = Button(root, text='Enter', font=('Helvetica', 24), command =age)
my_button.pack(pady=20)"""



root.mainloop()