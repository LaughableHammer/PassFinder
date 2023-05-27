import customtkinter as ctk
import tkinter as tk

from PassfinderLogic import accountmanager
from UserInterface.UI import Frame, PassFinder
from UserInterface import MainUI, LoginUI, ProfileUI
from PIL import Image, ImageTk

class CreateAccountUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Register", font=("Helvetica", 28))
        label.pack(pady=(15, 3), padx=10)
        
        arrow_image = ImageTk.PhotoImage(Image.open("Images\\arrow.png"), size=(30, 40))
        
        back_button = ctk.CTkButton(frame, text='', image=arrow_image, command=lambda: app.goto(LoginUI.LoginUI()))
        back_button.image = arrow_image
        back_button.pack(anchor=tk.NW, side=tk.LEFT)
        
        canvas = ctk.CTkCanvas(master=frame, height=1)
        canvas.pack(fill="x", padx=10, pady=10)
        canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill="black")

        UsernameEntry = ctk.CTkEntry(master=frame, placeholder_text="Username")
        UsernameEntry.pack(pady=12, padx=10)

        PasswordEntry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
        PasswordEntry.pack(pady=12, padx=10)
        
        PasswordEntry = ctk.CTkEntry(master=frame, placeholder_text="Confirm password", show="*")
        PasswordEntry.pack(pady=12, padx=10)

        def create_account():
            username = UsernameEntry.get()
            password = PasswordEntry.get()

            is_created = app.account_manager.create_account(username, password)
            if is_created:
                app.account_manager.login(username, password)
                app.goto(MainUI.MainUI())
            else:
                tk.messagebox.showerror("Input Error", "Account already exists or Password doesn't meet requirements.")  # intentionally vague for security purposes

        button = ctk.CTkButton(master=frame, text="Create Account", command=create_account)
        button.pack(pady=12, padx=10)
