from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from tkinter import messagebox


#make a window
root = Tk()
root.title("window")

#get wigth & height of screen
width= root.winfo_screenwidth()
height= root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d" % (width, height))
root.resizable(True, True)

# put image in a label and place label as background
imgTemp = Image.open("/Users/admiralaarit/Desktop/Space_Background_Image.png")
img2 = imgTemp.resize((width,height))
img = ImageTk.PhotoImage(img2)

label = Label(root,image=img)
label.pack(side='top',fill=Y,expand=True)

#text, welcome and boundary testing through age, ages 0-8 not allowed
def age():
    pass




root.mainloop()