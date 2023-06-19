from PassfinderLogic import storepassword
import customtkinter as ctk
import tkinter as tk
from UserInterface import LoginUI, ProfileUI, UI, MainUI
from UserInterface.UI import Frame, PassFinder


class StorePasswordUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=50, fill="both", expand=True)

        frame_left = ctk.CTkFrame(master=frame)  # Create a frame
        frame_left.pack(pady=0, padx=(0,0), fill="both", side="left")

        frame_right = ctk.CTkFrame(master=frame)  # Create a frame
        frame_right.pack(padx=(10, 0), fill="both", expand=True, side="right")

        ####Left side of the window (saving passwords)####

        label = ctk.CTkLabel(
            master=frame_left, text="Save Password", font=("Helvetica", 28)
        )
        label.pack(pady=(15, 3), padx=10)

        app_name = ctk.CTkEntry(
            master=frame_left, placeholder_text="Application Name"
        )  # app name text box
        app_name.pack(pady=12, padx=10)

        app_password = ctk.CTkEntry(
            master=frame_left, placeholder_text="Application Password", show="*"
        )  # app password textbox
        app_password.pack(pady=12, padx=10)

        with open("TextFiles/username.txt", "r") as file:  # read user username
            username = file.read()

        def store_password():
            name = app_name.get()  # retrieve details from input box
            password = app_password.get()

            if len(name) or len(password) > 50:
                tk.messagebox.showerror(
                    "Error", "Please restrict input to 50 characters."
                )
                app.goto(StorePasswordUI.StorePasswordUI())

            password_saved = storepassword.StorePassword().save_password(
                username, name, password
            )  # calls save_password function in storepassword.py

            if password_saved:
                tk.messagebox.showinfo("Password Saved", "Password has been saved.")
                app_name.delete(0, "end")
                app_password.delete(0, "end")
            else:  # popup saying password didn't save
                tk.messagebox.showerror(
                    "Error", "Password unable to be saved. Please try again."
                )  # intentionally vague for security purposes

        button = ctk.CTkButton(
            master=frame_left, text="Store New Password", command=store_password
        )
        button.pack(pady=10, padx=10)

        back_button = ctk.CTkButton(
            frame_left, text="Go Back", command=lambda: app.goto(MainUI.MainUI())
        )
        back_button.pack(pady=10, padx=10)

        ####Right side of main (deleting passwords)####
        label = ctk.CTkLabel(
            master=frame_right, text="Delete Passwords", font=("Helvetica", 28)
        )
        label.pack(pady=(15, 3), padx=10)
        
        app_name = ctk.CTkEntry( # by making user input the application name, accidental deletions can be prevented
            master=frame_right, placeholder_text="Application Name"
        )  # app name text box
        app_name.pack(pady=12, padx=10)

        def delete_password():
            password_to_delete = app_name.get()

            confirm = tk.messagebox.askquestion("Confirm", "Are you sure you want to delete the password?")
            if confirm == "yes":
                success = storepassword.StorePassword().delete_password(username, password_to_delete)
                if success:
                    tk.messagebox.showinfo("Password Deleted", "Password has been deleted.")
                else:
                    tk.messagebox.showerror("Error", "Password deletion failed. Please try again.")
            else:
                tk.messagebox.showinfo("Deletion Cancelled", "Password deletion has been cancelled.")

            app_name.delete(0, "end")

button = ctk.CTkButton(
    master=frame_right, text="Delete Password", command=delete_password
)
button.pack(pady=10, padx=10)















        
        confirm = tk.messagebox.askquestion("Confirm", "Are you sure?")

        button = ctk.CTkButton(
            master=frame_right, text="Delete Password", 
            command=lambda: 
            
        )
        button.pack(pady=10, padx=10)

        password_to_delete = app_name.get()
        delete_password = storepassword.StorePassword.delete_password()

        delete_password(username, password_to_delete)
        app_name.delete(0, "end")

        