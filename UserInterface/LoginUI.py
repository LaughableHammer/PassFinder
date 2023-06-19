from PassfinderLogic import accountmanager
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

from UserInterface.UI import Frame, PassFinder
from UserInterface import MainUI, CreateAccountUI


class LoginUI(Frame):
    def frame(
        self,
        app: PassFinder,
    ):
        frame = ctk.CTkFrame(
            master=app.root,
            corner_radius=15,
        )
        frame.pack(
            pady=40,
            padx=50,
            fill="both",
            expand=True,
        )

        label = ctk.CTkLabel(
            master=frame,
            text="Login",
            font=("Helvetica", 28),
        )  # text at the top
        label.pack(
            pady=(15, 3),
            padx=10,
        )

        canvas = ctk.CTkCanvas(
            master=frame,
            height=1,
        )  # separator line
        canvas.pack(
            fill="x",
            padx=10,
            pady=10,
        )
        canvas.create_line(
            0,
            1,
            int(frame.winfo_width() * 0.5),
            1,
            fill="black",
        )

        username_entry = ctk.CTkEntry(
            master=frame,
            placeholder_text="Username",
        )  # username text box
        username_entry.pack(
            pady=12,
            padx=10,
        )

        password_entry = ctk.CTkEntry(
            master=frame,
            placeholder_text="Password",
            show="*",
        )  # password textbox
        password_entry.pack(
            pady=12,
            padx=10,
        )

        def login():  # verify creditials in account manager python file
            username = username_entry.get()
            password = password_entry.get()

            with open("TextFiles/username.txt", "w") as file:
                file.write(username)

            is_logged_in = app.account_manager.login(
                username,
                password,
            )

            if is_logged_in:
                app.goto(
                    MainUI.MainUI(),
                )
            else:  # popup saying invalid details
                tk.messagebox.showerror(
                    "Input Error",
                    "Invalid username or password. Please try again.",
                )  # intentionally vague for security purposes

        button = ctk.CTkButton(
            master=frame,
            text="Login",
            command=login,
        )
        button.pack(
            pady=(12, 4),
            padx=10,
        )

        create_account_label = ctk.CTkLabel(
            master=frame,
            text="OR",
        )
        create_account_label.pack(
            pady=0.8,
        )

        button = ctk.CTkButton(
            master=frame,
            text="Create Account",
            command=lambda: app.goto(CreateAccountUI.CreateAccountUI()),
        )
        button.pack(pady=(4), padx=10)
