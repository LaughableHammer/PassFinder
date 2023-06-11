import customtkinter as ctk
import tkinter as tk

from tkinter import ttk

from PassfinderLogic import storepassword

from UserInterface import MainUI

from UserInterface.UI import Frame, PassFinder


class ViewPasswordsUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)

        frame.pack(pady=40, padx=50, fill="both", expand=True)

        label = ctk.CTkLabel(
            master=frame, text="Password Vault", font=("Helvetica", 28)
        )

        label.pack(pady=(15, 3), padx=10)

        canvas = ctk.CTkCanvas(master=frame, height=1)  # Horizontal line
        canvas.pack(fill="x", padx=10, pady=10)
        canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill="black")

        with open("TextFiles/username.txt", "r") as file:
            username = str(file.read())

        tk.messagebox.showwarning("Reminder", "Never share your password with anyone!")

        stored_passwords = storepassword.StorePassword().get_password(
            username
        )  # calls storepassword to retrieve all stored passwords associated with username

        scrollable_frame = ctk.CTkScrollableFrame(master=frame)
        scrollable_frame.pack(padx=20, fill="both", expand=True)

        if stored_passwords:
            #### Logic to align the passwords side by side ####
            row = 0

            column = 0

            max_columns = 3

            button_height = 30

            button_padding = 5

            button_width_percentage = 0.092

            screen_width = app.root.winfo_screenwidth()

            button_width = int(screen_width * button_width_percentage)

            for app_name, password in stored_passwords:  # iterates for every password
                app_password = password

                button = ctk.CTkButton(  # button for every password
                    scrollable_frame,
                    text=app_name,
                    command=lambda name=app_name, pwd=password: tk.messagebox.showinfo(
                        name, pwd
                    ),  # pop-up message box that displays password
                )

                button.configure(width=button_width, height=button_height)
                button.grid(
                    row=row, column=column, padx=button_padding, pady=button_padding
                )

                column += 1

                if column == max_columns: # next row if column is full
                    row += 1
                    column = 0

        else:
            print("No stored passwords.")

        back_button = ctk.CTkButton(
            frame, text="Go Back", command=lambda: app.goto(MainUI.MainUI())
        )

        back_button.pack(pady=10, padx=10, anchor="s", side="bottom")
