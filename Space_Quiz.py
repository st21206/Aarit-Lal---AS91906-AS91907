from tkinter import *

root = Tk()
root.title("Aarit's Space Quiz")
root.geometry('800x500')

#Defining the image
bg = PhotoImage(file="images/Space-Background-Image.jpg")

#Create a label
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, redwidth=1, relheight=1)