from PassfinderLogic import storepassword
import customtkinter as ctk
import tkinter as tk
from UserInterface import LoginUI, ProfileUI, UI, MainUI
from UserInterface.UI import Frame, PassFinder


class StorePasswordUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=50, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Password Vault", font=("Helvetica", 28))
        label.pack(pady=(15, 3), padx=10)

        canvas = ctk.CTkCanvas(master=frame, height=1)
        canvas.pack(fill="x", padx=10, pady=10)
        canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill="black")

        app_name = ctk.CTkEntry(master=frame, placeholder_text="Application Name") # app name text box
        app_name.pack(pady=12, padx=10)

        app_password = ctk.CTkEntry(master=frame, placeholder_text="Application Password", show="*") # app password textbox
        app_password.pack(pady=12, padx=10)

        def store_password():
            name = app_name.get()
            password = app_password.get()
            
            with open('TextFiles/username.txt', 'r') as file:
                username = file.read()
            
            password_saved = storepassword.StorePassword().save_password(username, name, password)

            if password_saved:
                tk.messagebox.showinfo("Password Saved", "Password has been saved.")
                app_name.delete(0, 'end')
                app_password.delete(0, 'end')
            else:  # popup saying password didn't save
                tk.messagebox.showerror("Error", "Password unable to be saved. Please try again.")  # intentionally vague for security purposes

        button = ctk.CTkButton(master=frame, text="Store New Password", command=store_password)
        button.pack(pady=10, padx=10)

        back_button = ctk.CTkButton(frame, text='Go Back', command=lambda: app.goto(MainUI.MainUI()))
        back_button.pack(pady=10, padx=10)