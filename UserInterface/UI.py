from abc import ABC, abstractmethod
import customtkinter as ctk
from PassfinderLogic.accountmanager import AccountManager

class PassFinder:
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.geometry("800x500")
        self.root.title("PassFinder")

        self.account_manager = AccountManager()

    def destroy_frames(self):
        for frame in self.root.winfo_children():
            frame.destroy()