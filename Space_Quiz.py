from tkinter import *
from PIL import ImageTk, Image
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
    global Space_Background, resized_bg, new_bg 
    Space_Background = Image.open('images/Space_Background_Image.png')
    resized_bg = Space_Background.resize((e.width, e.height), Image.ANTIALIAS)
    new_bg = ImageTk.PhotoImage(resized_bg)
    my_canvas.create_image(0,0, image=new_bg, anchor='nw')
    my_canvas.itemconfig(bg, image=new_bg)
    #make sure to add text below

    
root.bind('<Configure>', resizer)
root.mainloop()