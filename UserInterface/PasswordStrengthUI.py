import os
import tkinter as tk
import customtkinter as ctk

from PassfinderLogic.strengthtest import PasswordStrengthTest
from PassfinderLogic import storepassword
from UserInterface import MainUI
from UserInterface.ToolTip import ToolTip


class PasswordStrengthUI:
    """UI for strengthtest.py"""

    def frame(self, app):
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

        frame_left = ctk.CTkFrame(
            master=frame,
        )
        frame_left.pack(
            pady=0,
            padx=(0, 0),
            fill="both",
            side="left",
        )

        frame_right = ctk.CTkFrame(
            master=frame,
        )
        frame_right.pack(
            padx=(10, 0),
            fill="both",
            expand=True,
            side="right",
        )

        # Left side: Inputting own password for strength test

        # Create a label for password input
        label_left = ctk.CTkLabel(
            master=frame_left,
            text="Strength Test",
            font=("Helvetica", 28),
        )
        label_left.pack(
            pady=(15, 3),
            padx=10,
        )

        # Create an entry field for password input
        password_input = ctk.CTkEntry(
            master=frame_left,
            placeholder_text="Password",
        )
        password_input.pack(
            pady=12,
            padx=10,
        )
        ToolTip(password_input, "Enter password to test")

        def strength_test(pwd_input):
            """Input validation + output for strength test"""
            if not pwd_input:
                tk.messagebox.showerror("Error", "Please enter a password.")
                return

            strength_tester = PasswordStrengthTest()

            strength_test = strength_tester.run_strength_test(pwd_input)

            tk.messagebox.showinfo(
                "Strength Test",
                strength_test,
            )

        # Create a button to test the password
        password_test = ctk.CTkButton(
            master=frame_left,
            text="Test Password",
            command=lambda: strength_test(password_input.get()),
        )
        password_test.pack(
            pady=10,
            padx=10,
        )

        # Right side: Using pre-saved passwords for strength test

        # Create a label for stored passwords
        label_right = ctk.CTkLabel(
            master=frame_right,
            text="Stored Passwords",
            font=("Helvetica", 28),
        )
        label_right.pack(
            pady=(15, 3),
            padx=10,
        )

        ### Test already saved passwords ###
        username = os.environ.get("USERNAME")

        # Calls storepassword to retrieve all stored passwords associated with username
        stored_passwords = storepassword.StorePassword().get_password(username)

        scrollable_frame = ctk.CTkScrollableFrame(master=frame_right)
        scrollable_frame.pack(padx=15, fill="both", expand=True)

        if stored_passwords:
            # Logic to align the passwords side by side
            row = 0
            column = 0
            max_columns = 2
            button_height = 25
            button_padding = 10
            button_width_percentage = 0.088
            screen_width = app.root.winfo_screenwidth()
            button_width = int(screen_width * button_width_percentage)

            app_name_len = 20

            for app_name, password in stored_passwords:  # Iterate for every password
                truncated_name = (
                    app_name[:app_name_len] + "..."
                    if len(app_name) > app_name_len
                    else app_name
                )

                button = ctk.CTkButton(
                    scrollable_frame,
                    text=truncated_name,
                    command=lambda pwd_input=password: strength_test(pwd_input),
                    # Pop-up message box that displays password
                )
                button.configure(
                    width=button_width,
                    height=button_height,
                )
                button.grid(
                    row=row,
                    column=column,
                    padx=button_padding,
                    pady=button_padding,
                )
                ToolTip(button, "Click to test password")

                column += 1
                if column == max_columns:  # Next row if column is full
                    row += 1
                    column = 0

        # Create a button to go back to the main UI
        button_back = ctk.CTkButton(
            master=frame_left,
            text="Go Back",
            command=lambda: app.goto(MainUI.MainUI()),
        )
        button_back.pack(
            pady=12,
            padx=10,
        )
