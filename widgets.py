from customtkinter import CTkLabel, CTkButton
from functions import title_change

# title

def create_title(root):
    title = CTkLabel(
        root,
        text="Sarf Trainer",
        fg_color="transparent",
        font=("Arabic Typesetting",100,"bold")
    )
    return title

# start button

def create_start_btn(root,title):
    start_btn = CTkButton(
        master=root,
        text="Start",
        corner_radius=32,
        command=lambda: title_change(title,start_btn),
        width=100,
        height=100,
        fg_color="transparent",
        font=("Arial",40,"bold")
    )
    return start_btn