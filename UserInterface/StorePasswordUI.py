from PassfinderLogic import storepassword
import customtkinter as ctk
from UserInterface import LoginUI, ProfileUI, UI
from UserInterface.UI import Frame, PassFinder


class StorePasswordUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=50, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Password Storage", font=("Helvetica", 28))
        label.pack(pady=(15, 3), padx=10)

        canvas = ctk.CTkCanvas(master=frame, height=1)
        canvas.pack(fill="x", padx=10, pady=10)
        canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill="black")

        button = ctk.CTkButton(master=frame, text="Store Passwords", command=lambda: app.goto(LoginUI().LoginUI()))
        button.pack(pady=(4), padx=10)