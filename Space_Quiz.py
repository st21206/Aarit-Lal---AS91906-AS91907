import tkinter as tk
from tkinter import messagebox
import json
from PIL import ImageTk, Image
import random

#Define a class named SpaceQuiz
class SpaceQuiz:
    #Constructor method to initialize the class
    def __init__(self, root):
        #Initialize the root window
        self.root = root
        self.root.title("Aarit's Space Quiz")  #Set the title of the window
        self.root.attributes('-fullscreen', True)  #Set the window to fullscreen