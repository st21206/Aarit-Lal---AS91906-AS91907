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
        self.asked_questions = set()  #Initialize a set to store asked questions
        self.selected_answer = tk.IntVar(value=-1)  #Initialize selected_answer as IntVar with a default value of -1
        self.root.bind("<Button-1>", self.reset_colors)  #Bind left mouse button click event to reset_colors method

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

        #Method to validate age input and start the quiz if the age is valid
    def check_age(self, age):
        try:
            age = int(age)
            if age >= 4:
                self.setup_quiz_window()  #Call setup_quiz_window method to start the quiz
            else:
                messagebox.showinfo("Error", "Sorry, you must be 4 years or older to take the quiz.")  #Show error message if age is less than 4
        except ValueError:
            messagebox.showinfo("Error", "Please enter a valid age.")  #Show error message if age is not a valid number

    #Method to set up the quiz window
    def setup_quiz_window(self):
        #Destroy all widgets in the root window
        for widget in self.root.winfo_children():
            widget.destroy()

        #Create a label for the background image
        self.bg_label = tk.Label(self.root, image=self.bg_img_path)
        self.bg_label.place(relwidth=1, relheight=1)  #Place the background label to cover the whole window

        #Create a Quit button for the quiz window
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy, font=('Helvetica', 30), bg='red', fg='white')
        self.quit_button.pack(side=tk.LEFT, padx=20, pady=20, anchor='nw')  #Position the Quit button at the top-left corner

        #Create labels for question number and question text
        self.question_number_label = tk.Label(self.root, text="", font=('Helvetica', 24))
        self.question_number_label.place(relx=0.85, rely=0.05, anchor='ne')  #Position the question number label

        self.question_label = tk.Label(self.root, text="", font=('Helvetica', 40), wraplength=800, justify='center')
        self.question_label.place(relx=0.5, rely=0.27, anchor='center')  #Position the question label

        #Create a frame for answer buttons
        option_frame = tk.Frame(self.root)
        option_frame.place(relx=0.5, rely=0.5, anchor='center')  #Position the frame for answer buttons

        self.option_buttons = []  #List to store answer buttons
        #Create answer buttons and add them to the option_buttons list
        for i, option_text in enumerate(self.options[self.current_question]):
            option_button = tk.Button(option_frame, text=option_text, command=lambda i=i: self.process_answer(i), font=('Helvetica', 25), fg='black', width=60)
            option_button.pack(pady=10)
            self.option_buttons.append(option_button)
