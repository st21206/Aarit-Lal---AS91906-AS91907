from tkinter import *
from PIL import ImageTK, Image
root = Tk()
root.title("Aarit's Space Quiz")
root.geometry("800x500")

#Background code below
#Defining the image
bg = PhotoImage(file="images/Space_Background_Image.png")

#Create a canvas
my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill='both', expand=True)

#Set image in canvas
my_canvas.create_image(0,0, image=bg, anchor='nw')

#Resizer

root.bind('<Configure>', resizer)
root.mainloop()