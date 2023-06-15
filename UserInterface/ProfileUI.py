from PassfinderLogic import accountmanager
import customtkinter as ctk
from PIL import Image
from UserInterface import MainUI, LoginUI
from UserInterface.UI import Frame, PassFinder


class ProfileUI(Frame):
    def frame(self, app: PassFinder):
        if not app.account_manager.user:
            app.goto(LoginUI.LoginUI())

        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=50, fill="both", expand=True)

        label = ctk.CTkLabel(  # displays username
            master=frame,
            text="Welcome, " + app.account_manager.user.username,
            font=("Helvetica", 28),
        )
        label.pack(pady=(15, 3), padx=10)

        canvas = ctk.CTkCanvas(master=frame, height=1)  # Horizontal line
        canvas.pack(fill="x", padx=10, pady=10)
        canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill="black")