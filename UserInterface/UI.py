from abc import ABC, abstractmethod
import customtkinter as ctk
import tkinter as tk
from PassfinderLogic.accountmanager import AccountManager
from PIL import Image, ImageTk


class PassFinder:
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        

        self.root = ctk.CTk()
        self.root.geometry("800x500")
        self.root.title("PassFinder")
        self.root.minsize(400, 400)

        self.account_manager = AccountManager()

    def destroy_frames(self):
        for frame in self.root.winfo_children():
            frame.destroy()

    def goto(self, frame: "Frame") -> None:
        self.destroy_frames()
        frame.frame(self)


class Frame(ABC):
    @abstractmethod
    def frame(self, app: PassFinder) -> None:
        ...
