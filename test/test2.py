import tkinter as tk
from tkinter import messagebox
import json
from PIL import ImageTk, Image
import random

class SpaceQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Aarit's Space Quiz")
        self.root.attributes('-fullscreen', True)
        self.bg_img_path = ImageTk.PhotoImage(Image.open("images/Space_Background_Image_resized.png"))
        self.asked_questions = set()
        self.selected_answer = tk.IntVar(value=-1)  # Initialize selected_answer as IntVar with a default value of -1
        self.root.bind("<Button-1>", self.reset_colors)


        # Load questions and answers from JSON file
        with open("test/space_questions.json", "r") as file:
            data = json.load(file)
            self.questions = data["questions"]
            self.options = data["options"]
            self.correct_answers = data["correct_answers"]

        self.current_question = 0
        self.user_answers = []
        self.setup_start_screen()

    def setup_start_screen(self):
        start_bg_label = tk.Label(self.root, image=self.bg_img_path)
        start_bg_label.place(relwidth=1, relheight=1)

        title_label = tk.Label(self.root, text="Space Quiz", font=('Helvetica', 50, 'bold'))
        title_label.place(relx=0.5, rely=0.3, anchor='center')  # Adjust the rely parameter for vertical placement

        age_frame = tk.Frame(self.root)
        age_frame.place(relx=0.5, rely=0.6, anchor='center')  # Adjust the rely parameter for vertical placement

        age_label = tk.Label(age_frame, text="Please enter your age:", font=('Helvetica', 30))
        age_label.pack()

        age_entry = tk.Entry(age_frame, font=('Helvetica', 30))
        age_entry.pack()

        start_button = tk.Button(age_frame, text="Start Quiz", command=lambda: self.check_age(age_entry.get()), font=('Helvetica', 30))
        start_button.pack()

    # Quit Button
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy, font=('Helvetica', 30), bg='red', fg='white')
        self.quit_button.place(relx=0.05, rely=0.05)  # Place the Quit button in the top left corner


    def check_age(self, age):
        try:
            age = int(age)
            if age >= 4:
                self.setup_quiz_window()
            else:
                messagebox.showinfo("Error", "Sorry, you must be 4 years or older to take the quiz.")
        except ValueError:
            messagebox.showinfo("Error", "Please enter a valid age.")

    def setup_quiz_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.bg_label = tk.Label(self.root, image=self.bg_img_path)
        self.bg_label.place(relwidth=1, relheight=1)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy, font=('Helvetica', 30), bg='red', fg='white')
        self.quit_button.pack(side=tk.LEFT, padx=20, pady=20, anchor='nw')  # Place the Quit button at the top-left corner

        self.question_number_label = tk.Label(self.root, text="", font=('Helvetica', 24))
        self.question_number_label.place(relx=0.85, rely=0.05, anchor='ne')  # Display question number in the center

        self.question_label = tk.Label(self.root, text="", font=('Helvetica', 40))
        self.question_label.place(relx=0.5, rely=0.3, anchor='center')

        option_frame = tk.Frame(self.root)  # Frame to hold the answer buttons
        option_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.option_buttons = []
        for i, option_text in enumerate(self.options[self.current_question]):
            option_button = tk.Button(option_frame, text=option_text, command=lambda i=i: self.process_answer(i), font=('Helvetica', 25), fg='black', width=60)
            option_button.pack(pady=10)
            self.option_buttons.append(option_button)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, font=('Helvetica', 25), bg='blue', fg='black')
        self.next_button.place(relx=0.90, rely=0.5, anchor='center')  # Position Next button to the right of the screen in the middle

        self.restart_button = tk.Button(self.root, text="Restart Quiz", command=self.restart_quiz, font=('Helvetica', 25), bg='blue', fg='black')
        self.restart_button.place(relx=0.10, rely=0.5, anchor='center')

        self.load_question()



    def process_answer(self, index):
        if self.selected_answer.get() != -1:
            self.option_buttons[self.selected_answer.get()].config(bg='SystemButtonFace', fg='black')  # Reset previous choice color
        self.selected_answer.set(index)
        self.option_buttons[index].config(bg='orange', fg='white')  # Highlight the new choice


    def reset_colors(self, event):
        if self.selected_answer.get() != -1:
            self.option_buttons[self.selected_answer.get()].config(bg='SystemButtonFace', fg='black')  # Reset previous choice color

        

    def load_question(self):
        if len(self.asked_questions) == len(self.questions):
            self.show_result()
            return

        available_questions = list(set(range(len(self.questions))) - self.asked_questions)
        self.current_question = random.choice(available_questions)

        self.asked_questions.add(self.current_question)

        self.question_number_label.config(text=f"Question {len(self.asked_questions)}/15")
        self.question_label.config(text=self.questions[self.current_question])
        for i, option_text in enumerate(self.options[self.current_question]):
            self.option_buttons[i].config(text=option_text, state=tk.NORMAL, bg='SystemButtonFace')
        self.selected_answer.set(-1)  # Deselect all options



    def next_question(self):
        selected_answer_index = self.selected_answer.get()
        if selected_answer_index == -1:
            messagebox.showinfo("Error", "Please select an option.")
        else:
            self.user_answers.append(selected_answer_index)
            self.current_question += 1
            self.load_question()

    def show_result(self):
        score = sum(1 for user_answer, correct_answer in zip(self.user_answers, self.correct_answers) if user_answer == correct_answer)
        messagebox.showinfo("Result", f"Your Score: {score}/{len(self.questions)}")
        self.restart_quiz()

    def restart_quiz(self):
        self.asked_questions.clear()  # Clear the set of asked questions
        for button in self.option_buttons:
            button.config(state=tk.NORMAL, bg='SystemButtonFace')  # Reset answer buttons
        self.current_question = 0
        self.user_answers = []
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpaceQuiz(root)
    root.mainloop()
