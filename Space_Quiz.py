from tkinter import *
from PIL import ImageTK, Image
root = Tk()
root.title("Aarit's Space Quiz")
root.geometry("800x500")

#Background code below
#Defining the image
bg = ImageTk.PhotoImage(file="images/Space_Background_Image.png")

#Create a canvas
my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill='both', expand=True)

#Set image in canvas
my_canvas.create_image(0,0, image=bg, anchor='nw')

#Resizer
def resizer(e):
    Space_Background = Image.open('images/Space_Background_Image.pn')
    resized_Space_Background = Space_Background.resize((e.width, e.height), Image.ANTIALIAS)

root.bind('<Configure>', resizer)
root.mainloop()