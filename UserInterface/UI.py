from abc import ABC, abstractmethod
import customtkinter as ctk
import tkinter as tk
from PassfinderLogic.accountmanager import AccountManager
from PassfinderLogic import *
from PIL import Image, ImageTk

'''
    NOTE:
    Once again your imports are not separated.
    You need more documentation that is present here.
    As you have not outlined what these variables are 
    for, or why this class is present. 
    
    Docstrings are dearly needed in this section.
'''

class PassFinder:
    def __init__(self):
        ctk.set_appearance_mode("System")  # colour theme for app
        ctk.set_default_color_theme("blue")
        ctk.set_widget_scaling(1.1)  # widget size relative to app

        self.root = ctk.CTk()
        self.root.geometry("800x500")  # window size
        self.root.title("PassFinder")
        self.root.minsize(400, 450)  # minimum window size
        self.root.resizable(0, 0)
        self.account_manager = AccountManager()

    def destroy_frames(self):  # remove all frames open
        for frame in self.root.winfo_children():
            frame.destroy()

    def goto(
        self, frame: "Frame"
    ) -> None:  # destroy current frame, open new defined one
        self.destroy_frames()
        frame.frame(self)


class Frame(ABC):
    @abstractmethod
    def frame(self, app: PassFinder) -> None:
        ...
