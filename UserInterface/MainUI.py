from PassfinderLogic import accountmanager
import customtkinter as ctk
from PIL import Image
from UserInterface import (
    LoginUI,
    ProfileUI,
    StorePasswordUI,
    ViewPasswordsUI,
)  # Import UI classes
from UserInterface.UI import Frame, PassFinder

'''
    NOTE:
    Your commenting is very poor, you have some comments 
    here which are less than helpful. You need to make sure that you
    have a consistent scheme for documenting the code you are writing.
    
    Furthermore, you should make sure that you are commenting as you 
    write your code. You need to explain your current decisions. 
    Likewise, you can come and clean these comments up. Then they can be
    finalised. 
    
    You code is not very reusable. If you use object oriented design to 
    reuse common user interface elements you will be able to recreate those
    using simple imports and objects. 
    
    You are using a function within a function, why? 
'''

class MainUI(Frame):
    def frame(self, app: PassFinder):
        frame_main = ctk.CTkFrame(master=app.root, corner_radius=15)  # Create a frame
        frame_main.pack(pady=40, padx=50, fill="both", expand=True)

        frame = ctk.CTkFrame(master=frame_main)  # Create a frame
        frame.pack(pady=0, padx=(0,0), fill="both", side="left")

        frame_right = ctk.CTkFrame(master=frame_main)  # Create a frame
        frame_right.pack(padx=(10, 0), fill="both", expand=True, side="right")

        label = ctk.CTkLabel(master=frame, text="Dashboard", font=("Helvetica", 28))
        label.pack(pady=(15, 3), padx=10)

        button = ctk.CTkButton(
            master=frame,
            text="Store Passwords",
            command=lambda: app.goto(StorePasswordUI.StorePasswordUI()),
        )
        button.pack(pady=12, padx=5)

        button = ctk.CTkButton(
            master=frame,
            text="View Passwords",
            command=lambda: app.goto(ViewPasswordsUI.ViewPasswordsUI()),
        )
        button.pack(pady=12, padx=5)

        def logout():  #  Logout function
            app.account_manager.logout()
            app.goto(LoginUI.LoginUI())

        label = ctk.CTkLabel(  # displays username
            master=frame_right,
            text="Profile - " + app.account_manager.user.username,
            font=("Helvetica", 28),
        )
        label.pack(pady=(15, 3), padx=10)

        button = ctk.CTkButton(
            master=frame_right, text="Back", command=lambda: app.goto(MainUI.MainUI())
        )
        button.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame, text="Logout", command=logout)
        button.pack(pady=12, padx=5)
