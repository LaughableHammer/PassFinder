from PassfinderLogic import accountmanager
import customtkinter as ctk
import tkinter as tk
import tkinter.tix as tix

from UserInterface.UI import Frame, PassFinder
from UserInterface import MainUI, CreateAccountUI


class LoginUI(Frame):
    """1/2 UI for accountmanager.py

    Args:
        Frame (class): The app window
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

        # Create the title label
        label = ctk.CTkLabel(
            master=frame,
            text="Login",
            font=("Helvetica", 28),
        )
        label.pack(
            pady=(15, 3),
            padx=10,
        )

        # Create a horizontal line using canvas
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

        # Create an entry field for the username
        username_entry = ctk.CTkEntry(
            master=frame,
            placeholder_text="Username",
        )
        username_entry.pack(
            pady=12,
            padx=10,
        )

        # Create an entry field for the password
        password_entry = ctk.CTkEntry(
            master=frame,
            placeholder_text="Password",
            show="*",
        )
        password_entry.pack(
            pady=12,
            padx=10,
        )

        def login():
            """Attempt to login with the provided credentials"""
            username = username_entry.get()
            password = password_entry.get()

            with open("TextFiles/username.txt", "w") as file:
                file.write(username)

            is_logged_in = app.account_manager.login(
                username,
                password,
            )

            if is_logged_in:
                # Redirect to the main UI upon successful login
                app.goto(
                    MainUI.MainUI(),
                )
            else:
                # Show an error message for invalid credentials
                tk.messagebox.showerror(
                    "Input Error",
                    "Invalid username or password. Please try again.",
                )  # intentionally vague for security purposes

        # Create a button for login
        button = ctk.CTkButton(
            master=frame,
            text="Login",
            command=login,
        )
        button.pack(
            pady=(12, 4),
            padx=10,
        )           

        # Create a label for "OR"
        create_account_label = ctk.CTkLabel(
            master=frame,
            text="OR",
        )
        create_account_label.pack(
            pady=0.8,
        )

        # Create a button to go to the create account UI
        button = ctk.CTkButton(
            master=frame,
            text="Create Account",
            command=lambda: app.goto(CreateAccountUI.CreateAccountUI()),
        )
        button.pack(pady=(4), padx=10)
