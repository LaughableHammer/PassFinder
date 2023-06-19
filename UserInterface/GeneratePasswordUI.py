import random
import string
import tkinter as tk
import customtkinter as ctk
from UserInterface.UI import Frame, PassFinder
from UserInterface import MainUI
from PassfinderLogic import generatepassword


class GeneratePasswordUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=50, fill="both", expand=True)

        label = ctk.CTkLabel(
            master=frame,
            text="Generate Password",
            font=("Helvetica", 28),
        )
        label.pack(
            pady=(15, 3),
            padx=10,
        )

        canvas = tk.Canvas(
            master=frame,
            height=1,
        )  # Horizontal line
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

        password_length = ctk.CTkEntry(
            master=frame,
            placeholder_text="Password Length",
        )
        password_length.pack(
            pady=5,
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
            password = generatepassword.PasswordGenerator.generate_password(
                self,
                password_length.get(),
                checkbox_special.get(),
                checkbox_numbers.get(),
                checkbox_normal.get(),
            )
            tk.messagebox.showinfo(
                "Generated Password",
                f"Generated Password: {password}",
            )

        button_generate = ctk.CTkButton(
            master=frame,
            text="Generate Password",
            command=generate_password,
        )
        button_generate.pack(
            pady=12,
            padx=10,
        )

        button_back = ctk.CTkButton(
            master=frame,
            text="Back",
            command=lambda: app.goto(MainUI.MainUI()),
        )
        button_back.pack(
            pady=12,
            padx=10,
        )
