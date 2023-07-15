"""Import UI and Logic elements"""
import os
import tkinter as tk
import customtkinter as ctk

from PassfinderLogic import storepassword
from UserInterface import MainUI
from UserInterface.UI import Frame, PassFinder
from UserInterface.ToolTip import ToolTip


class ViewPasswordsUI(Frame):
    """UI to view passwords from storepassword.py

    Args:
        Frame (class): The app window
    """

    def frame(self, app: PassFinder):
        """The "mini" app window that overlays the main window

        Args:
            app (PassFinder): The root app
        """

        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=50, fill="both", expand=True)

        label = ctk.CTkLabel(
            master=frame, text="Password Vault", font=("Helvetica", 28)
        )
        label.pack(pady=(15, 3), padx=10)

        canvas = ctk.CTkCanvas(master=frame, height=1)  # Horizontal line
        canvas.pack(fill="x", padx=10, pady=10)
        canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill="black")

        username = os.environ.get('USERNAME')

        tk.messagebox.showwarning("Reminder", "Never share your password with anyone!")
        
        # Calls storepassword to retrieve all stored passwords associated with username
        stored_passwords = storepassword.StorePassword().get_password(username)

        scrollable_frame = ctk.CTkScrollableFrame(master=frame)
        scrollable_frame.pack(padx=20, fill="both", expand=True)

        if stored_passwords:
            # Logic to align the passwords side by side
            row = 0
            column = 0
            max_columns = 3
            button_height = 30
            button_padding = 5
            button_width_percentage = 0.092
            screen_width = app.root.winfo_screenwidth()
            button_width = int(screen_width * button_width_percentage)

            for app_name, password in stored_passwords:  # Iterate for every password
                button = ctk.CTkButton(
                    scrollable_frame,
                    text=app_name,
                    command=lambda name=app_name, pwd=password: tk.messagebox.showinfo(
                        name, pwd
                    ),
                    # Pop-up message box that displays password
                )
                button.configure(width=button_width, height=button_height)
                button.grid(
                    row=row, column=column, padx=button_padding, pady=button_padding
                )
                ToolTip(button, "Click to reveal password")

                column += 1
                if column == max_columns:  # Next row if column is full
                    row += 1
                    column = 0
        else:
            print("No stored passwords.")

        back_button = ctk.CTkButton(
            frame,
            text="Go Back",
            command=lambda: app.goto(MainUI.MainUI()),
        )
        back_button.pack(pady=10, padx=10, anchor="s", side="bottom")
