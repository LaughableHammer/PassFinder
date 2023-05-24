from PassfinderLogic import accountmanager
import customtkinter as ctk
from PIL import Image
from UserInterface import LoginUI2

from UserInterface.UI import PassFinder

def mainUI(app: PassFinder):
    
    frame = ctk.CTkFrame(master=app.root, corner_radius=15)
    frame.pack(pady=40, padx=60, fill="both", expand=True)
    
    label = ctk.CTkLabel(master=frame, text="Main System", font=("Arial", 24))
    label.pack(pady=12, padx=10)

    canvas = ctk.CTkCanvas(master=frame, height=1)
    canvas.pack(fill='x', padx=10, pady=10)
    canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill='black')

    def logout():
        app.destroy_frames()
        LoginUI2.loginUI(app)

    button = ctk.CTkButton(master=frame, text="Logout", command=logout)
    button.pack(pady=12, padx=10)