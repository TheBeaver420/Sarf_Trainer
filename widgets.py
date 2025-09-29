from customtkinter import *

# title

def create_title(root,text):
    return CTkLabel(
        root,
        text=text,
        fg_color="transparent",
        font=("Arabic Typesetting",100,"bold")
    )

# start button

def create_button(root,text,command):
    return CTkButton(
        master=root,
        text=text,
        corner_radius=32,
        command=command,
        width=200,
        height=100,
        fg_color="transparent",
        font=("Arial",40,"bold")
    )

