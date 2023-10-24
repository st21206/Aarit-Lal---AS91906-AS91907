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

        #Create Next and Restart Quiz buttons
        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=('Helvetica', 25), bg='blue', fg='black')
        self.next_button.place(relx=0.90, rely=0.5, anchor='center')  #Position the Next button

        self.restart_button = tk.Button(self.root, text="Restart Quiz", command=self.restart_quiz, font=('Helvetica', 25), bg='blue', fg='black')
        self.restart_button.place(relx=0.10, rely=0.5, anchor='center')  #Position the Restart Quiz button

        self.load_question()  #Call load_question method to load the first question

    #Method to handle the user's answer selection
    def process_answer(self, index):
        if self.selected_answer.get() != -1:
            self.option_buttons[self.selected_answer.get()].config(bg='SystemButtonFace', fg='black')  #Reset previous choice color
        self.selected_answer.set(index)
        self.option_buttons[index].config(bg='orange', fg='white')  #Highlight the new choice

    #Method to reset answer button colors on mouse click
    def reset_colors(self, event):
        if self.selected_answer.get() != -1:
            self.option_buttons[self.selected_answer.get()].config(bg='SystemButtonFace', fg='black')  #Reset previous choice color

    #Method to load the next question
    def load_question(self):
        #Check if all questions have been asked, if yes, display the result
        if len(self.asked_questions) == len(self.questions):
            self.show_result()
            return

        #Get available questions that have not been asked
        available_questions = list(set(range(len(self.questions))) - self.asked_questions)
        self.current_question = random.choice(available_questions)  #Choose a random question from available questions

        self.asked_questions.add(self.current_question)  # Add the current question to asked questions set

        #Update question number and question text labels
        self.question_number_label.config(text=f"Question {len(self.asked_questions)}/15")
        self.question_label.config(text=self.questions[self.current_question])
        #Update answer buttons with options for the current question
        for i, option_text in enumerate(self.options[self.current_question]):
            self.option_buttons[i].config(text=option_text, state=tk.NORMAL, bg='SystemButtonFace')
        self.selected_answer.set(-1)  # Deselect all options

    #Method to handle the Next button click
    def next_question(self):
        selected_answer_index = self.selected_answer.get()
        #Check if an answer is selected, if not, show an error message
        if selected_answer_index == -1:
            messagebox.showinfo("Error", "Please select an option.")
        else:
            self.user_answers.append(selected_answer_index)  # Add the selected answer to user's answers
            self.current_question += 1  # Move to the next question
            self.load_question()  # Load the next question

    #Method to display the quiz result
    def show_result(self):
        #Calculate the score by comparing user's answers with correct answers
        score = sum(1 for user_answer, correct_answer in zip(self.user_answers, self.correct_answers) if user_answer == correct_answer)
        #Show a messagebox with the user's score
        messagebox.showinfo("Result", f"Your Score: {score}/15")
        self.restart_quiz()  # Restart the quiz after displaying the result

    #Method to restart the quiz
    def restart_quiz(self):
        self.asked_questions.clear()  #Clear the set of asked questions
        for button in self.option_buttons:
            button.config(state=tk.NORMAL, bg='SystemButtonFace')  #Reset answer buttons
        self.current_question = 0  #Reset current question index
        self.user_answers = []  #Clear user's answers list
        self.load_question()  #Load the first question

# Main entry point of the program
if __name__ == "__main__":
    root = tk.Tk()  #Create a tkinter root window
    app = SpaceQuiz(root)  #Create an instance of the SpaceQuiz class
    root.mainloop()  #Start the tkinter main event loop


