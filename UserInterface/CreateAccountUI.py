from PassfinderLogic import accountmanager
import customtkinter as ctk
from tkinter import messagebox
from UserInterface.UI import PassFinder
from UserInterface import MainUI
from PIL import Image

def createAccountUI(app: PassFinder):
    frame = ctk.CTkFrame(master=app.root, corner_radius=15)
    frame.pack(pady=40, padx=60, fill="both", expand=True)
    
    label = ctk.CTkLabel(master=frame, text="Create Account System", font=("Arial", 24))
    label.pack(pady=12, padx=10)
    
    UsernameEntry = ctk.CTkEntry(master=frame, placeholder_text="Username")
    UsernameEntry.pack(pady=12, padx=10)
    
    PasswordEntry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    PasswordEntry.pack(pady=12, padx=10)

    def create_account():
        username = UsernameEntry.get()
        password = PasswordEntry.get()

        is_created = app.account_manager.create_account(username, password)
        if is_created:
            app.account_manager.login(username, password)
            app.destroy_frames()
            MainUI.mainUI(app)
        else:
            messagebox.showerror("Popup", "Account already exists or Password doesn't meet requirements.") # intentionally vague for security purposes

    button = ctk.CTkButton(master=frame, text="Create Account", command=create_account)
    button.pack(pady=12, padx=10)