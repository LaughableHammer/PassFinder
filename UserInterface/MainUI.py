from PassfinderLogic import accountmanager  # Import the account manager module
import customtkinter as ctk  # Import the custom tkinter module
from PIL import Image  # Import the Image class from the PIL library
from UserInterface import LoginUI, ProfileUI, StorePasswordUI, ViewPasswordsUI  # Import UI classes
from UserInterface.UI import Frame, PassFinder  # Import Frame and PassFinder classes

class MainUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)  # Create a frame with rounded corners
        frame.pack(pady=40, padx=50, fill="both", expand=True)  # Pack the frame with padding and expansion options

        label = ctk.CTkLabel(master=frame, text="Dashboard", font=("Helvetica", 28))  # Create a label with the text "Dashboard" and a font size of 28
        label.pack(pady=(15, 3), padx=10)  # Pack the label with vertical and horizontal padding

        canvas = ctk.CTkCanvas(master=frame, height=1)  # Create a canvas
        canvas.pack(fill="x", padx=10, pady=10)  # Pack the canvas to fill the horizontal space with padding
        canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill="black")  # Draw a horizontal line on the canvas

        button = ctk.CTkButton(
            master=frame,
            text="Profile",
            command=lambda: app.goto(ProfileUI.ProfileUI()),  # Bind the button click event to navigate to the ProfileUI
        )
        button.pack(pady=12, padx=10)  # Pack the button with padding

        button = ctk.CTkButton(
            master=frame,
            text="Store Passwords",
            command=lambda: app.goto(StorePasswordUI.StorePasswordUI()),  # Bind the button click event to navigate to the StorePasswordUI
        )
        button.pack(pady=12, padx=10)  # Pack the button with vertical padding

        button = ctk.CTkButton(
            master=frame,
            text="View Passwords",
            command=lambda: app.goto(ViewPasswordsUI.ViewPasswordsUI()),  # Bind the button click event to navigate to the StorePasswordUI
        )
        button.pack(pady=12, padx=10)  # Pack the button with vertical padding

        def logout():  # Define a logout function
            app.account_manager.logout()  # Call the logout method of the account manager
            app.goto(LoginUI.LoginUI())  # Navigate to the LoginUI

        button = ctk.CTkButton(master=frame, text="Logout", command=logout)  # Create a logout button
        button.pack(pady=12, padx=10)  # Pack the button with padding
