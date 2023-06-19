import tkinter as tk
from PassfinderLogic import storepassword
import customtkinter as ctk
from UserInterface import MainUI

'''
    NOTE: 
    I have no idea what this class is for, 
    as there is no docstring which is telling me what 
    any of the functions are used for.
    
    The comments which are present seem to indicate 
    changes of behaviour halfway through some functions.
    Should this not be separated into different responsibilities.
    
    There are a lot of repeated magic numbers, none of which 
    have an explanation. And the comments which are added; add 
    no context to what the code is doing. 
'''

class StorePasswordUI:
    def frame(self, app):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=50, fill="both", expand=True)

        frame_left = ctk.CTkFrame(master=frame)
        frame_left.pack(pady=0, padx=(0, 0), fill="both", side="left")

        frame_right = ctk.CTkFrame(master=frame)
        frame_right.pack(padx=(10, 0), fill="both", expand=True, side="right")

        #### Left side of the window (saving passwords) ####

        label = ctk.CTkLabel(
            master=frame_left, text="Save Password", font=("Helvetica", 28)
        )
        label.pack(pady=(15, 3), padx=10)

        app_name = ctk.CTkEntry(
            master=frame_left, placeholder_text="Application Name"
        )
        app_name.pack(pady=12, padx=10)

        app_password = ctk.CTkEntry(
            master=frame_left, placeholder_text="Application Password", show="*"
        )
        app_password.pack(pady=12, padx=10)

        with open("TextFiles/username.txt", "r") as file:
            username = file.read()

        def store_password():
            name = app_name.get()
            password = app_password.get()

            if len(name) > 50 or len(password) > 50:
                tk.messagebox.showerror(
                    "Error", "Please restrict input to 50 characters."
                )
                app.goto(MainUI.MainUI())

            password_saved = storepassword.StorePassword().save_password(
                username, name, password
            )

            if password_saved:
                tk.messagebox.showinfo("Password Saved", "Password has been saved.")
                app_name.delete(0, "end")
                app_password.delete(0, "end")
            else:
                tk.messagebox.showerror(
                    "Error", "Password unable to be saved. Please try again."
                )

        button = ctk.CTkButton(
            master=frame_left, text="Store New Password", command=store_password
        )
        button.pack(pady=10, padx=10)

        back_button = ctk.CTkButton(
            frame_left, text="Go Back", command=lambda: app.goto(MainUI.MainUI())
        )
        back_button.pack(pady=10, padx=10)

        #### Right side of main (deleting passwords) ####
        label = ctk.CTkLabel(
            master=frame_right, text="Delete Passwords", font=("Helvetica", 28)
        )
        label.pack(pady=(15, 3), padx=10)

        app_name_delete = ctk.CTkEntry(
            master=frame_right, placeholder_text="Application Name"
        )
        app_name_delete.pack(pady=12, padx=10)

        def delete_password():
            password_to_delete = app_name_delete.get()
            password_deletion = storepassword.StorePassword().delete_password(username, password_to_delete)
            if password_deletion:
                tk.messagebox.showinfo("Password Deleted", "Password has been deleted.")
            else:
                tk.messagebox.showerror("Error", "Password deletion failed. Please try again.")
            app_name_delete.delete(0, "end")


        button = ctk.CTkButton(
            master=frame_right,
            text="Delete Password",
            command=lambda: (delete_password(), app_name.delete(0, "end")),
        )
        button.pack(pady=10, padx=10)





# from PassfinderLogic import storepassword
# import customtkinter as ctk
# import tkinter as tk
# from UserInterface import LoginUI, ProfileUI, UI, MainUI
# from UserInterface.UI import Frame, PassFinder


# class StorePasswordUI(Frame):
#     def frame(self, app: PassFinder):
#         frame = ctk.CTkFrame(master=app.root, corner_radius=15)
#         frame.pack(pady=40, padx=50, fill="both", expand=True)

#         frame_left = ctk.CTkFrame(master=frame)  # Create a frame
#         frame_left.pack(pady=0, padx=(0,0), fill="both", side="left")

#         frame_right = ctk.CTkFrame(master=frame)  # Create a frame
#         frame_right.pack(padx=(10, 0), fill="both", expand=True, side="right")

#         ####Left side of the window (saving passwords)####

#         label = ctk.CTkLabel(
#             master=frame_left, text="Save Password", font=("Helvetica", 28)
#         )
#         label.pack(pady=(15, 3), padx=10)

#         app_name = ctk.CTkEntry(
#             master=frame_left, placeholder_text="Application Name"
#         )  # app name text box
#         app_name.pack(pady=12, padx=10)

#         app_password = ctk.CTkEntry(
#             master=frame_left, placeholder_text="Application Password", show="*"
#         )  # app password textbox
#         app_password.pack(pady=12, padx=10)

#         with open("TextFiles/username.txt", "r") as file:  # read user username
#             username = file.read()

#         def store_password():
#             name = app_name.get()  # retrieve details from input box
#             password = app_password.get()

#             if len(name) or len(password) > 50:
#                 tk.messagebox.showerror(
#                     "Error", "Please restrict input to 50 characters."
#                 )
#                 app.goto(StorePasswordUI.StorePasswordUI())

#             password_saved = storepassword.StorePassword().save_password(
#                 username, name, password
#             )  # calls save_password function in storepassword.py

#             if password_saved:
#                 tk.messagebox.showinfo("Password Saved", "Password has been saved.")
#                 app_name.delete(0, "end")
#                 app_password.delete(0, "end")
#             else:  # popup saying password didn't save
#                 tk.messagebox.showerror(
#                     "Error", "Password unable to be saved. Please try again."
#                 )  # intentionally vague for security purposes

#         button = ctk.CTkButton(
#             master=frame_left, text="Store New Password", command=store_password
#         )
#         button.pack(pady=10, padx=10)

#         back_button = ctk.CTkButton(
#             frame_left, text="Go Back", command=lambda: app.goto(MainUI.MainUI())
#         )
#         back_button.pack(pady=10, padx=10)

#         ####Right side of main (deleting passwords)####
#         label = ctk.CTkLabel(
#             master=frame_right, text="Delete Passwords", font=("Helvetica", 28)
#         )
#         label.pack(pady=(15, 3), padx=10)
        
#         app_name_delete = ctk.CTkEntry( # by making user input the application name, accidental deletions can be prevented
#             master=frame_right, placeholder_text="Application Name"
#         )  # app name text box
#         app_name_delete.pack(pady=12, padx=10)

#         button = ctk.CTkButton(
#             master=frame_right, text="Delete Password", command=lambda: (delete_password, app_name.delete(0, "end"))
#         )
#         button.pack(pady=10, padx=10)

#         def delete_password():
#             password_to_delete = app_name_delete.get()
#             password_deletion = storepassword.StorePassword().delete_password(username, password_to_delete)
#             if password_deletion:
#                 tk.messagebox.showinfo("Password Deleted", "Password has been deleted.")
#             else:
#                 tk.messagebox.showerror("Error", "Password deletion failed. Please try again.")



        