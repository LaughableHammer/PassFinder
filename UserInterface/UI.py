from abc import ABC, abstractmethod
import customtkinter as ctk
from PassfinderLogic.accountmanager import AccountManager


class PassFinder:
    """Main UI Window"""

    def __init__(self):
        """Initialise the main window"""
        ctk.set_appearance_mode("System")  # Set the color theme for the app
        ctk.set_default_color_theme("blue")
        ctk.set_widget_scaling(1.1)  # Adjust the widget size relative to the app

        self.root = ctk.CTk()
        self.root.geometry("800x500")  # Set the window size
        self.root.title("PassFinder")
        self.root.minsize(
            400,
            450,
        )  # Set the minimum window size
        self.root.resizable(
            0,
            0,
        )  # Disable window resizing
        self.root.iconbitmap("Icon\PassFinder.ico")
        self.account_manager = AccountManager()

    def destroy_frames(self):
        """Remove all frames that are currently open"""
        for frame in self.root.winfo_children():
            frame.destroy()

    def goto(
        self,
        frame: "Frame",
    ) -> None:
        """Destroy the current frame and open a new one as specified

        Args:
            frame (Frame): frame to open
        """
        self.destroy_frames()
        frame.frame(self)


class Frame(ABC):
    """Defines the frame that all the UI elements assemble on

    Args:
        ABC (_type_):
    """

    @abstractmethod
    def frame(
        self,
        app: PassFinder,
    ) -> None:
        """Abstract method to be implemented by subclasses

        Args:
            app (PassFinder): app window
        """
        ...
