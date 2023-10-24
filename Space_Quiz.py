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

        #Method to set up the start screen
    def setup_start_screen(self):
        #Create a label for the background image
        start_bg_label = tk.Label(self.root, image=self.bg_img_path)
        start_bg_label.place(relwidth=1, relheight=1)  #Place the background label to cover the whole window

        #Create and place a label for the title which will be called Space Quiz
        title_label = tk.Label(self.root, text="Space Quiz", font=('Helvetica', 50, 'bold'))
        title_label.place(relx=0.5, rely=0.3, anchor='center')  #Position the title label at the center

        #Create a frame for age input widgets
        age_frame = tk.Frame(self.root)
        age_frame.place(relx=0.5, rely=0.6, anchor='center')  #Position the frame below the title

        #Create labels, entry box, and start quiz button for age input
        age_label = tk.Label(age_frame, text="Please enter your age:", font=('Helvetica', 30))
        age_label.pack()

        age_entry = tk.Entry(age_frame, font=('Helvetica', 30))
        age_entry.pack()

        start_button = tk.Button(age_frame, text="Start Quiz", command=lambda: self.check_age(age_entry.get()), font=('Helvetica', 30))
        start_button.pack()

        # Create a quit button
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy, font=('Helvetica', 30), bg='red', fg='white')
        self.quit_button.place(relx=0.05, rely=0.05)  #Place the Quit button in the top left corner
