import requests
import pyarabic.araby as araby
from customtkinter import *
from PIL import Image, ImageTk
import buttons
from buttons import title_change

# app setup

app = CTk()
app.geometry("1920x1080")
app.title("SarfTrainer")
set_appearance_mode("dark")

# label

label = CTkLabel(
    app,
    text="Sarf Trainer",
    fg_color="transparent",
    font=("Arabic Typesetting",100,"bold")
)
label.place(relx=.5,rely=.1, anchor="center")

#start button

start_btn = CTkButton(
    master=app,
    text="Start",
    corner_radius=32,
    command=lambda: title_change(label,start_btn),
    width=100,
    height=100,
    fg_color="transparent",
    font=("Arial",40,"bold")
)
start_btn.place(relx=0.5, rely=0.5,anchor="center")

#run the app

app.mainloop()