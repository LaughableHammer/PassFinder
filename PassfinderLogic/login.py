import customtkinter as ctk
from PIL import Image
import sqlite3
import hashlib

class PassFinder:
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.geometry("800x500")
        self.root.title("PassFinder")
        
        self.frame = ctk.CTkFrame(master=self.root, corner_radius=15)
        self.frame.pack(pady=40, padx=60, fill="both", expand=True)
        
        self.label = ctk.CTkLabel(master=self.frame, text="Login System", font=("Arial", 24))
        self.label.pack(pady=12, padx=10)
        
        self.UsernameEntry = ctk.CTkEntry(master=self.frame, placeholder_text="Username")
        self.UsernameEntry.pack(pady=12, padx=10)
        
        self.PasswordEntry = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.PasswordEntry.pack(pady=12, padx=10)
        
        self.button = ctk.CTkButton(master=self.frame, text="Login", command=self.login)
        self.button.pack(pady=12, padx=10)
        
        self.canvas = ctk.CTkCanvas(master=self.frame, height=1)
        self.canvas.pack(fill='x', padx=10, pady=10)
        LineLength = int(self.frame.winfo_width() * 0.5)
        self.canvas.create_line(0, 1, LineLength, 1, fill='black')
        
        self.root.mainloop()
        
if __name__ == '__main__':
    pass_finder = PassFinder()