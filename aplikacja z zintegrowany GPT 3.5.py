import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import customtkinter
from PIL import Image, ImageTk

root = customtkinter.CTk()

def settings():
    opcje = customtkinter.CTk()
    opcje.title("Ustawienia")
    opcje.geometry("400x600")
    Motyw = customtkinter.CTkLabel(opcje, text="wybierz motyw", font=customtkinter.CTkFont(family="sans-serif", weight="bold", size=27, slant="roman"))
    Motyw.place(x=110, y=75)
    jasny = customtkinter.CTkButton(opcje, text="light", corner_radius=90, font=customtkinter.CTkFont(weight="bold"), width=80, command=lambda: zmianamotywu_jasny())
    jasny.place(x=107, y=120)
    ciemny = customtkinter.CTkButton(opcje, text="dark", corner_radius=90, font=customtkinter.CTkFont(weight="bold"), width=80, command=lambda: zmianamotywu_ciemny())
    ciemny.place(x=225, y=120)
    
    def zmianamotywu_jasny():
        customtkinter.set_appearance_mode("light")
        
    def zmianamotywu_ciemny():
        customtkinter.set_appearance_mode("dark")
    
    opcje.mainloop()

root.title("SoulGPT")
root.geometry("800x600")
customtkinter.set_appearance_mode("system")
image_menu = PhotoImage(file="menu3.png")
button = customtkinter.CTkButton(root, width=10, height=40, text="", corner_radius=120, image=image_menu, fg_color='transparent', bg_color="transparent", background_corner_colors=None, border_color=None, hover_color="#ffffff", command=lambda: settings())
button.place(x=720, y=10)
hasło_label = customtkinter.CTkLabel(root, text="Password", font=customtkinter.CTkFont(family="sans-serif", weight="bold", size=27, slant="roman"))
hasło_label.place(x=350, y=100)
password_entry = customtkinter.CTkEntry(root, width=230, height=40, corner_radius=50, border_color="grey", show="*")
password_entry.place(x=300, y=150)
login = customtkinter.CTkButton()

check_var = customtkinter.StringVar(value="off")
def hasło_checkbox():
    if check_var.get() == "on":
        password_entry.configure(show="")
    else:
        password_entry.configure(show="*")

check = customtkinter.CTkCheckBox(root, text="Show Password", font=customtkinter.CTkFont(family="sans-serif", weight="bold", slant="roman"), fg_color="black", hover_color="white", variable=check_var, onvalue="on", offvalue="off", command=hasło_checkbox)
check.place(x=300, y=220)

root.mainloop()
