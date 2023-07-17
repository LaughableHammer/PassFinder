"""Import UI elements and Logic"""
import re
import os
import tkinter as tk
import customtkinter as ctk

from UserInterface import LoginUI, MainUI
from UserInterface.ToolTip import ToolTip
from UserInterface.UI import Frame, PassFinder


class CreateAccountUI(Frame):
    """2/2 UI for accountmanager.py

    Args:
        Frame (class): The main app window
    """

    def frame(
        self,
        app: PassFinder,
    ):
        """The "mini" app window that overlays the main window

        Args:
            app (PassFinder): The root app
        """
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
            text="Register",
            font=("Helvetica", 28),
        )
        label.pack(
            pady=(15, 3),
            padx=10,
        )

        canvas = ctk.CTkCanvas(
            master=frame,
            height=1,
        )
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
        )

        username_entry.pack(
            pady=12,
            padx=10,
        )
        ToolTip(username_entry, "Enter a username")

        password_entry = ctk.CTkEntry(
            master=frame,
            placeholder_text="Password",
            show="*",
        )
        password_entry.pack(
            pady=12,
            padx=10,
        )
        ToolTip(password_entry, "Enter a master password")

        confirm_password = ctk.CTkEntry(
            master=frame,
            placeholder_text="Confirm password",
            show="*",
        )
        confirm_password.pack(
            pady=12,
            padx=10,
        )
        ToolTip(confirm_password, "Enter master password again")

        def create_account():
            """Take in user inputs and if valid, create an account in db"""
            username = username_entry.get()
            password = password_entry.get()
            confirm = confirm_password.get()

            # Set the environment variable
            os.environ["USERNAME"] = username

            # Check if username length is valid
            if len(username) > 25:
                tk.messagebox.showerror(
                    "Error",
                    "Username can't be longer than 25 characters.",
                )
                app.goto(
                    CreateAccountUI.CreateAccountUI(),
                )

            # Check password requirements using regular expressions
            if re.search(
                r"\d",
                password,
            ):  # uses REGEX to loop for numbers
                pass
            else:
                tk.messagebox.showinfo(
                    "Input Error",
                    "Password needs at least 1 number.",
                )
                app.goto(
                    CreateAccountUI.CreateAccountUI(),
                )

            if re.search(
                r"\W",
                password,
            ):  # finds symbols and special characters
                pass
            else:
                tk.messagebox.showinfo(
                    "Input Error",
                    "Password needs at least 1 special character",
                )
                app.goto(
                    CreateAccountUI.CreateAccountUI(),
                )

            if re.search(
                r"[a-z]",
                password,
            ):  # finds lowercase letters
                pass
            else:
                tk.messagebox.showinfo(
                    "Input Error",
                    "Password needs at least 1 lowercase letter",
                )
                app.goto(
                    CreateAccountUI.CreateAccountUI(),
                )

            if re.search(
                r"[A-Z]",
                password,
            ):  # finds uppercase letters
                pass
            else:
                tk.messagebox.showinfo(
                    "Input Error",
                    "Password needs at least 1 uppercase letter.",
                )
                app.goto(
                    CreateAccountUI.CreateAccountUI(),
                )

            # Show errors for different validation statements
            if password != confirm:
                tk.messagebox.showerror(
                    "Input Error",
                    "Passwords do not match. Please try again.",
                )
                app.goto(
                    CreateAccountUI.CreateAccountUI(),
                )

            if len(password) == 0:
                tk.messagebox.showinfo(
                    "Input Error",
                    "Password can't be empty",
                )
                app.goto(
                    CreateAccountUI.CreateAccountUI(),
                )

            if len(password) <= 2:
                tk.messagebox.showerror(
                    "Input Error",
                    "Password is too short.",
                )
                app.goto(
                    CreateAccountUI.CreateAccountUI(),
                )

            if len(password) > 100:
                tk.messagebox.showerror(
                    "Input Error",
                    "Password is too long.",
                )
                app.goto(
                    CreateAccountUI.CreateAccountUI(),
                )

            # Create the account and proceed to the main UI if successful
            is_created = app.account_manager.create_account(
                username,
                password,
            )
            if is_created:  # checks if account is made by passing through inputs
                app.account_manager.login(
                    username,
                    password,
                )
                app.goto(
                    MainUI.MainUI(),
                )
            else:
                tk.messagebox.showerror(
                    "Input Error",
                    "Username or Password unavailable.",
                )  # intentionally vague for security purposes

        button = ctk.CTkButton(
            master=frame,
            text="Create Account",
            command=create_account,
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

        back_button = ctk.CTkButton(
            frame,
            text="Go Back",
            command=lambda: app.goto(LoginUI.LoginUI()),
        )
        back_button.pack(
            pady=4,
            padx=10,
        )
