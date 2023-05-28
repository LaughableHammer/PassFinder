from PassfinderLogic import accountmanager
import customtkinter as ctk
from PIL import Image
from UserInterface import LoginUI, ProfileUI, StorePasswordUI
from UserInterface.UI import Frame, PassFinder


class MainUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Dashboard", font=("Helvetica", 28))
        label.pack(pady=(15, 3), padx=10)

        canvas = ctk.CTkCanvas(master=frame, height=1)
        canvas.pack(fill="x", padx=10, pady=10)
        canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill="black")

        button = ctk.CTkButton(
            master=frame,
            text="Profile",
            command=lambda: app.goto(ProfileUI.ProfileUI()),
        )
        button.pack(pady=12, padx=10)

        button = ctk.CTkButton(master=frame, text="Store Passwords", command=lambda: app.goto(CreateAccountUI.CreateAccountUI()))
        button.pack(pady=(4), padx=10)

        def logout():
            app.account_manager.logout()
            app.goto(LoginUI.LoginUI())

        button = ctk.CTkButton(master=frame, text="Logout", command=logout)
        button.pack(pady=12, padx=10)
