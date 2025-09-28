from customtkinter import *
from widgets import create_title, create_button

class SarfTrainerApp:
    def __init__(self,root):
        self.title = None
        self.start_btn = None
        self.next_label = None
        self.root = root

        # get monitor resolution

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Resize window

        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.resizable(True,True)

        #Ui Setup

        self.root.title("Sarf Trainer")
        set_appearance_mode("dark")

        # Start screen
        self.show_start_screen()

    def show_start_screen(self):
        # Create title
        self.title = create_title(self.root,"Sarf Trainer")
        self.title.place(relx=0.5, rely=0.1, anchor="center")

        # Create button
        self.start_btn = create_button(
            self.root,text="Start",command=self.start_pressed
        )
        self.start_btn.place(relx=0.5, rely=0.2, anchor="center")

    def start_pressed(self):
        # Destroy old widgets
        self.title.destroy()
        self.start_btn.destroy()

        # Show next screen

        self.next_label = create_title(
            self.root,"Welcome to Sarf Trainer"
        )
        self.next_label.place(relx=0.5, rely=0.2, anchor="center")