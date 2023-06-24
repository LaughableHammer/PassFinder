import random
import string
import tkinter as tk
import customtkinter as ctk
import pyperclip
from UserInterface.UI import Frame, PassFinder
from UserInterface import MainUI
from PassfinderLogic import generatepassword


class GeneratePasswordUI(Frame):
    """UI for generatepassword.py

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
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=50, fill="both", expand=True)

        # Create the title label
        label = ctk.CTkLabel(
            master=frame,
            text="Generate Password",
            font=("Helvetica", 28),
        )
        label.pack(
            pady=(15, 3),
            padx=10,
        )

        # Create a horizontal line using canvas
        canvas = tk.Canvas(
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

        def validate_input(
            value,
        ):
            """Provides input validation for the entry boxes -> credits: https://www.geeksforgeeks.org/python-tkinter-validating-entry-widget/

            Args:
                value (any input): Whatever the user types

            Returns:
                _type_: _description_
            """
            if value.isdigit() or value == "":  # check input
                if value and int(value) > 50:
                    return False
                return True
            return False

        # Create an entry field for password length
        password_length = ctk.CTkEntry(
            master=frame,
            placeholder_text="Password Length",
        )
        password_length.pack(
            pady=5,
        )

        reg = frame.register(validate_input)

        password_length.configure(
            validate="key",
            validatecommand=(reg, "%P"),
        )

        # Checkboxes for character types
        checkbox_special = ctk.CTkCheckBox(
            master=frame,
            text="Special Characters",
        )
        checkbox_special.pack(
            pady=5,
        )

        checkbox_numbers = ctk.CTkCheckBox(
            master=frame,
            text="Numbers",
        )
        checkbox_numbers.pack(
            pady=5,
        )

        checkbox_normal = ctk.CTkCheckBox(
            master=frame,
            text="Normal Characters",
        )
        checkbox_normal.pack(
            pady=5,
        )

        def generate_password():
            """Get user specifications for the password + validation"""
            button_generate.configure(state=tk.DISABLED)
            length = password_length.get()
            special_chars = checkbox_special.get()
            numbers = checkbox_numbers.get()
            normal_chars = checkbox_normal.get()

            # Validate password length input
            if not length:
                tk.messagebox.showerror("Error", "Please enter a password length.")
                return
            elif length == "0":
                tk.messagebox.showerror(
                    "Input Error", "Password length cannot be zero."
                )
                return

            if not special_chars and not numbers and not normal_chars:
                tk.messagebox.showerror(
                    "Input Error", "Please select at least one option."
                )
                return

            # Generate the password
            password = generatepassword.PasswordGenerator.generate_password(
                self,
                length,
                special_chars,
                numbers,
                normal_chars,
            )

            # Create a Toplevel window to display the generated password
            top = tk.Toplevel()
            top.title("Generated Password")

            # Create a label to show the password
            password_label = tk.Label(
                top,
                text="Generated Password:",
                width=50,
            )
            password_label.pack(
                pady=10,
            )

            # Create a text entry field to display the password
            password_entry = tk.Entry(
                top,
                width=20,
            )
            password_entry.insert(
                0,
                password,
            )
            password_entry.pack(
                pady=10,
            )
            button_generate.configure(state=tk.NORMAL)
            # Function to copy the password to the clipboard
            def copy_password():
                top.clipboard_clear()
                top.clipboard_append(password)
                top.update()

            # Create a button to copy the password
            copy_button = tk.Button(
                top,
                text="Copy Password",
                command=copy_password,
            )
            copy_button.pack(
                pady=10,
            )

        # Create a button to generate the password
        button_generate = ctk.CTkButton(
            master=frame,
            text="Generate Password",
            command=generate_password,
        )
        button_generate.pack(
            pady=12,
            padx=10,
        )

        # Create a button to go back to the main UI
        button_back = ctk.CTkButton(
            master=frame,
            text="Back",
            command=lambda: app.goto(MainUI.MainUI()),
        )
        button_back.pack(
            pady=12,
            padx=10,
        )
