from tkinter import *
from PIL import ImageTk, Image

class SpaceQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Aarit's Space Quiz")
        self.root.geometry("800x500")
        
        # Load the original background image
        self.original_bg = Image.open('images/Space_Background_Image.png')
        self.bg = ImageTk.PhotoImage(self.original_bg)

        # Create a label to display the image without resizing
        self.bg_label = Label(root, image=self.bg)
        self.bg_label.pack()
        
        # Bind the resize function to window resize event
        self.root.bind('<Configure>', self.resizer)
        
    def resize_image(self, event):
        aspect_ratio = self.original_bg.width / self.original_bg.height
        new_width = event.width
        new_height = int(new_width / aspect_ratio)

    def resizer(self, event):
        # Get the resized image
        resized_image = self.resize_image(event)
        # Update the label with the resized image
        self.bg_label.configure(image=resized_image)
        self.bg_label.image = resized_image  # keep a reference to the image object to prevent garbage collection


if __name__ == "__main__":
    root = Tk()
    app = SpaceQuiz(root)
    root.mainloop()
