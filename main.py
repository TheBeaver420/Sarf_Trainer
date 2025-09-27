import requests
import pyarabic.araby as araby
from customtkinter import *
from PIL import Image, ImageTk
from widgets import create_title, create_start_btn
from functions import title_change

# app setup
app = CTk()
app.geometry("1920x1080")
app.title("SarfTrainer")
set_appearance_mode("dark")

# Creates widgets, passing app
title = create_title(app)
start_btn = create_start_btn(app,title)

# Place widgets
title.place(relx=.5,rely=.1, anchor="center")
start_btn.place(relx=0.5, rely=0.5,anchor="center")

#run the app

app.mainloop()