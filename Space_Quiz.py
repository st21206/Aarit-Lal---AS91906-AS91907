#Import necessary modules
import tkinter as tk  #Import tkinter library for GUI
from tkinter import messagebox  #Import messagebox module for displaying messages
import json  #Import json module for working with JSON file contaning my questions and answers
from PIL import ImageTk, Image  #Import ImageTk and Image modules from PIL (Pillow) for background image handling
import random  #Import random module for generating random questions

#Define a class named SpaceQuiz
class SpaceQuiz:
    #Constructor method to initialize the class
    def __init__(self, root):
        #Initialize the root window
        self.root = root
        self.root.title("Aarit's Space Quiz")  #Set the title of the window
        self.root.attributes('-fullscreen', True)  #Set the window to fullscreen
        self.bg_img_path = ImageTk.PhotoImage(Image.open("images/Space_Background_Image_resized.png"))  #Load and set the background image
        

        #Load questions and answers from JSON file
        with open("test/space_questions.json", "r") as file:
            data = json.load(file)
            self.questions = data["questions"]
            self.options = data["options"]
            self.correct_answers = data["correct_answers"]

        #Initialize variables for tracking current question and user answers
        self.current_question = 0
        self.user_answers = []
        #Call setup_start_screen method to display the start screen
        self.setup_start_screen()