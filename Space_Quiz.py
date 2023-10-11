from tkinter import *
from PIL import ImageTk, Image


#make a window
ws = Tk()
ws.title("window")

#get wigth & height of screen
width= ws.winfo_screenwidth()
height= ws.winfo_screenheight()

#set screensize as fullscreen and not resizable
ws.geometry("%dx%d" % (width, height))
ws.resizable(True, True)

# put image in a label and place label as background
imgTemp = Image.open("/Users/admiralaarit/Desktop/Space_Background_Image.png")
img2 = imgTemp.resize((width,height))
img = ImageTk.PhotoImage(img2)

label = Label(ws,image=img)
label.pack(side='top',fill=Y,expand=True)

#text = Text(ws,height=10,width=53)
#text.place(x=30, y=50)

#button = Button(ws,text='SEND',relief=RAISED,font=('Arial Bold', 18))
#button.place(x=190, y=250)

ws.mainloop()