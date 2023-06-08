from PassfinderLogic import storepassword
import customtkinter as ctk
import tkinter as tk
from UserInterface import LoginUI, ProfileUI, UI, MainUI
from UserInterface.UI import Frame, PassFinder


class ViewPasswordsUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=50, fill="both", expand=True)

        label = ctk.CTkLabel(
            master=frame, text="Password Vault", font=("Helvetica", 28)
        )
        label.pack(pady=(15, 3), padx=10)

        with open("TextFiles/username.txt", "r") as file:
            username = file.read()

        tk.messagebox.showwarning(
            "Warning", "Please remember, never share your password with anyone."
        )

        stored_passwords = storepassword.StorePassword.get_password(username)

        if stored_passwords:
            # Display the passwords on the GUI
            for password in stored_passwords:
                password_label = ctk.CTkLabel(
                    master=frame, text=password, font=("Helvetica", 12)
                )
                password_label.pack(pady=5, padx=10)
        else:
            no_password_label = ctk.CTkLabel(
                master=frame, text="No passwords found.", font=("Helvetica", 12)
            )
            no_password_label.pack(pady=5, padx=10)

        canvas = ctk.CTkCanvas(master=frame, height=1)
        canvas.pack(fill="x", padx=10, pady=10)
        canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill="black")

        back_button = ctk.CTkButton(
            frame, text="Go Back", command=lambda: app.goto(MainUI.MainUI())
        )
        back_button.pack(pady=10, padx=10)
