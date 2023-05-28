import customtkinter as ctk

from UserInterface import LoginUI, ProfileUI, MainUI
from UserInterface.UI import Frame, PassFinder

class StorePasswordUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Store Passwords", font=("Helvetica", 28))
        label.pack(pady=(15, 3), padx=10)
        
        canvas = ctk.CTkCanvas(master=frame, height=1)
        canvas.pack(fill="x", padx=10, pady=10)
        canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill="black")      
        
        back_button = ctk.CTkButton(frame, text='Go Back', command=lambda: app.goto(MainUI.MainUI()))
        back_button.pack(pady=4, padx=10)
