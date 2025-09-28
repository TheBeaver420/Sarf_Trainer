import requests
import pyarabic.araby as araby
from customtkinter import *
from PIL import Image, ImageTk

from screens import SarfTrainerApp
from widgets import create_title, create_button


# app setup
def main():
    app = CTk()
    SarfTrainerApp(app)
    app.mainloop()

if __name__ == "__main__":
    main()