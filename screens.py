from customtkinter import *
from widgets import create_title, create_button

class SarfTrainerApp:
    def __init__(self,root):
        self.root = root

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
        self.start_btn = create_button(self.root,"Done!",command=self.show_quiz_screen)
        self.start_btn.place(relx=0.5, rely=0.3, anchor="center")



    def show_quiz_screen(self):
        self.clear_screen()
        self.quiz_frame = QuizFrame(
            master = self.root,
            question_text="What does the word كتب mean?" ,
            on_submit=self.process_answer
        )
        self.quiz_frame.pack(fill="both",expand=True)

    def process_answer(self,answer):
        print(f"User selected:{answer}")
        self.show_quiz_screen()
        self.question_number += 1
        print(self.question_number)

#Defines frame that shows a question, checkboxes and a submit button
class QuizFrame(CTkFrame):
    def __init__(self,master, question_text, on_submit):
        super().__init__(master)
        self.onsubmit = on_submit

        # Create question text
        self.question_label = create_title(self, question_text)
        self.question_label.pack(pady=30)

        # Answer checkboxes
        self.answers_vars = []
        for i in range(4):
            var = IntVar()
            checkbox = CTkCheckBox(
                self, text=f"Option {i+1}", variable=var
            )
            checkbox.pack(pady=30)
            self.answers_vars.append(checkbox)

        #submit button
        submit_btn = create_button(self, "Submit", command=self.submit)
        submit_btn.pack(pady=30)

    def submit(self):
        selected_answer = [i + 1 for i, var in enumerate(self.answers_vars) if var.get() == 1]
        print("Selected answers:", selected_answer)
        self.onsubmit(selected_answer)

