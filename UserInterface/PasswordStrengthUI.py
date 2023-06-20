import random
import string
import tkinter as tk
import customtkinter as ctk
from UserInterface.UI import Frame, PassFinder
from UserInterface import MainUI
from PassfinderLogic.strengthtest import PasswordStrengthTest


class PasswordStrengthUI(Frame):
    def frame(self, app: PassFinder):
        # Create the main frame for the generate password UI
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=50, fill="both", expand=True)

        # Create the title label
        label = ctk.CTkLabel(
            master=frame,
            text="Password Strength Test",
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

        # Create an entry field for password length
        password_input = ctk.CTkEntry(
            master=frame,
            placeholder_text="Password",
        )
        password_input.pack(
            pady=5,
        )

        def strength_test():
            input = password_input.get()

            strength_tester = PasswordStrengthTest()

            strength_test = strength_tester.run_strength_test(input)

            tk.messagebox.showinfo(
                "Strength Test",
                strength_test,
            )

        # Create a button to generate the password
        password_test = ctk.CTkButton(
            master=frame,
            text="Test Password",
            command=strength_test,
        )
        password_test.pack(
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
