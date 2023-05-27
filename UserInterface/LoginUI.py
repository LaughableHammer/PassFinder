from PassfinderLogic import accountmanager
import customtkinter as ctk
import tkinter as tk
from UserInterface.UI import Frame, PassFinder
from UserInterface import MainUI, CreateAccountUI


class LoginUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(
            master=frame, text="Login", font=("Arial", 24)
        )  # text at the top
        label.pack(pady=12, padx=10)

        UsernameEntry = ctk.CTkEntry(
            master=frame, placeholder_text="Username"
        )  # username text box
        UsernameEntry.pack(pady=12, padx=10)

        PasswordEntry = ctk.CTkEntry(
            master=frame, placeholder_text="Password", show="*"
        )  # password textbox
        PasswordEntry.pack(pady=12, padx=10)

        def login():
            username = UsernameEntry.get()
            password = PasswordEntry.get()
            is_logged_in = app.account_manager.login(
                username, password
            )  # verify creditials in account manager python file
            if is_logged_in:
                app.goto(MainUI.MainUI())
            else:  # popup saying invalid details
                tk.messagebox.showerror(
                    "Popup", "Invalid username or password. Please try again."
                )  # intentionally vague for security purposes

        button = ctk.CTkButton(master=frame, text="Login", command=login)
        button.pack(pady=12, padx=10)

        separator = tk.ttk.Separator(master=frame, orient="horizontal")
        separator.place(relx=0.5, rely=0.5, relwidth=1, anchor="center")
        separator.pack()
        # canvas = ctk.CTkCanvas(master=frame, height=1)
        # canvas.pack(fill='x', padx=10, pady=10)
        # canvas.create_line(0, 1, frame.winfo_width() * 0.5, 1, fill='black')

        button = ctk.CTkButton(
            master=frame,
            text="Create Account",
            command=lambda: app.goto(CreateAccountUI.CreateAccountUI()),
        )
        button.pack(pady=12, padx=10)
