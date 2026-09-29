from customtkinter import *
from widgets import create_title, create_button
from functions import generate_conjugations, pickform
import random

class SarfTrainerApp:
    def __init__(self,root):
        self.root = root
        self.score = 0
        self.questions = 0

        # Widgets
        self.title = None
        self.start_btn = None
        self.next_label = None
        self.quiz_frame = None

        # Get monitor resolution

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Resize window

        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.resizable(True,True)

        # Ui Setup

        self.root.title("Sarf Trainer")
        set_appearance_mode("dark")

        # Start screen
        self.show_start_screen()

        self.question_number = 0

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_start_screen(self):
        self.clear_screen()
        # Create title
        self.title = create_title(self.root,"Sarf Trainer")
        self.title.place(relx=0.5, rely=0.1, anchor="center")

        # Create button
        self.start_btn = create_button(
            self.root,text="Start",command=self.show_options_screen)
        self.start_btn.place(relx=0.5, rely=0.2, anchor="center")

    def show_options_screen(self):
        self.clear_screen()
        # Show next screen

        self.next_label = create_title(
            self.root,"Welcome to Sarf Trainer, pick your options"
        )
        self.next_label.place(relx=0.5, rely=0.2, anchor="center")
        self.next_label = create_title(
            self.root,"Set your timer", font = ("Sans Serif", 70)
        )
        self.timer_entry = CTkEntry(
            self.root,
            placeholder_text="Enter time in seconds",
            height=49
        )
        self.timer_entry.place(relx=0.5, rely=0.5, anchor="center")
        self.next_label.place(relx=0.5, rely=0.4, anchor="center")
        self.start_btn = create_button(self.root,"Done!",command=self.start_quiz)
        self.start_btn.place(relx=0.5, rely=0.75, anchor="center")

    def process_answer(self):
        self.show_quiz_screen(self.timer)
        self.question_number += 1

    def show_quiz_screen(self,timer):
        generated_forms = (generate_conjugations(questions=1))
        self.clear_screen()
        self.quiz_frame = QuizFrame(
            master = self.root,
            question_text=f"What does the word '{generated_forms[0]}' mean?" ,
            on_submit=self.process_answer,
            increment_score=self.incrementScore,
            increment_questions=self.incrementQuestions,
            time=timer
        )
        for checkbox in self.quiz_frame.answers_vars:
            if checkbox.correct_answer:
                checkbox.configure(text=f"Option {self.quiz_frame.answers_vars.index(checkbox)+1}: {generated_forms[1]}")
            else:
                checkbox.configure(text=f"Option {self.quiz_frame.answers_vars.index(checkbox)+1}: {list(pickform())}")

        self.next_label = create_title(
                    self.root,f"Score = {self.getScore()} out of {self.getQuestions()}", font = ("Arial", 50)
                )
        self.next_label.place(relx=0.5, rely=0.95, anchor="center")
        self.quiz_frame.pack(fill="both",expand=True)

    def getScore(self):
        return self.score

    def incrementScore(self):
        self.score += 1

    def getQuestions(self):
            return self.questions
    
    def incrementQuestions(self):
        self.questions += 1    

    def start_quiz(self):
        self.timer = int(self.timer_entry.get())
        self.show_quiz_screen(self.timer)

#Defines frame that shows a question, checkboxes and a submit button
class QuizFrame(CTkFrame):
    def __init__(self,master, question_text, on_submit, increment_score, increment_questions, time):
        super().__init__(master)
        self.timer_id = None
        self.onsubmit = on_submit
        self.increment_score = increment_score
        self.increment_questions = increment_questions
        self.time_left = time

        # Create question text
        self.question_label = create_title(self, question_text)
        self.question_label.pack(pady=100)

        # Answer checkboxes
        self.answers_vars = []
        numbers = random.randint(0, 3)  # Randomize the order of options
        self.answer_var = IntVar()
        for i in range(4):
            radio_button = QuizRadio(
                self,
                text=f"Option {i+1}:",
                variable=self.answer_var,
                value=i,
                font = ("Arial", 24)
            )
            if i == numbers:  # Set a random checkbox as the correct answer
                radio_button.set_correct_answer()
            radio_button.pack(pady=30)
            self.answers_vars.append(radio_button)
        self.timer_label = create_title(self, f"Time: {self.time_left}")
        self.timer_label.pack()
        self.update_timer()

        #submit button
        submit_btn = create_button(self, "Submit", command=self.submit)
        submit_btn.pack(pady=30)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.configure(text=f"Time: {self.time_left}")
            self.timer_id = self.after(1000, self.update_timer)
        else:
            self.increment_questions()
            self.onsubmit()

    def submit(self):
        if self.timer_id is not None:
            self.after_cancel(self.timer_id)
        selected_radio = self.answer_var.get()
        selected_answer = self.answers_vars[selected_radio]
        self.increment_questions()
        if selected_answer.is_correct():
            self.increment_score()
        self.onsubmit()

    

class QuizRadio(CTkRadioButton):
    def __init__(self, master, text, variable, value, font):
        super().__init__(master, text=text, variable=variable, value = value, font = font)
        self.correct_answer = False  # Placeholder for the correct answer

    def set_correct_answer(self):
        self.correct_answer = True

    def is_correct(self):
        return self.correct_answer

