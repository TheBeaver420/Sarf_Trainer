import requests
import pyarabic.araby as araby
from customtkinter import *
from PIL import Image, ImageTk

app = CTk()
app.geometry("1920x1080")
app.title("SarfTrainer")
set_appearance_mode("dark")


btn = CTkButton(master=app,text="Click Me", corner_radius=32,command=app.destroy,width=500,height=500,font=("Arial",200,"bold"))
btn.place(relx=0.5, rely=0.5,anchor="center")

app.mainloop()