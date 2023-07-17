"""Import UI elements and Logic"""
import os
import tkinter as tk
import customtkinter as ctk

from PassfinderLogic import storepassword
from UserInterface import MainUI
from UserInterface.ToolTip import ToolTip


class StorePasswordUI:
    """UI for storepassword.py

    Args:
        Frame (class): The app window
    """

    def frame(
        self,
        app,
    ):
        """The "mini" app window that overlays the main window

        Args:
            app (PassFinder): The root app
        """
        frame = ctk.CTkFrame(
            master=app.root,
            corner_radius=15,
        )
        frame.pack(
            pady=40,
            padx=50,
            fill="both",
            expand=True,
        )

        frame_left = ctk.CTkFrame(
            master=frame,
        )
        frame_left.pack(
            pady=0,
            padx=(0, 0),
            fill="both",
            side="left",
        )

        frame_right = ctk.CTkFrame(
            master=frame,
        )
        frame_right.pack(
            padx=(10, 0),
            fill="both",
            expand=True,
            side="right",
        )

        #### Left side of the window (saving passwords) ####

        # Create a label for saving passwords
        label = ctk.CTkLabel(
            master=frame_left,
            text="Save Password",
            font=("Helvetica", 28),
        )
        label.pack(
            pady=(15, 3),
            padx=10,
        )

        # Create an entry field for the application name
        app_name = ctk.CTkEntry(
            master=frame_left,
            placeholder_text="Application Name",
        )
        app_name.pack(
            pady=12,
            padx=10,
        )
        ToolTip(app_name, "Enter the application name")

        # Create an entry field for the application password
        app_password = ctk.CTkEntry(
            master=frame_left,
            placeholder_text="Application Password",
            show="*",
        )
        app_password.pack(
            pady=12,
            padx=10,
        )
        ToolTip(app_password, "Enter password for application")

        username = os.environ.get("USERNAME")

        def store_password():
            """Get the name and password entered by the user and call function + validation"""
            name = app_name.get()
            password = app_password.get()

            if not name or not password:
                # Show an error message for null input
                tk.messagebox.showerror(
                    "Error",
                    "Please don't leave any input fields empty.",
                )
                return

            if len(name) > 50 or len(password) > 50:
                # Show an error message for exceeding the character limit
                tk.messagebox.showerror(
                    "Error",
                    "Please restrict input to 50 characters.",
                )
                return

            # Save the password using the storepassword module
            password_saved = storepassword.StorePassword().save_password(
                username,
                name,
                password,
            )

            if password_saved:
                # Show a success message and clear the input fields
                tk.messagebox.showinfo(
                    "Password Saved",
                    "Password has been saved.",
                )
                app_name.delete(
                    0,
                    "end",
                )
                app_password.delete(
                    0,
                    "end",
                )
            else:
                # Show an error message if the password could not be saved
                tk.messagebox.showerror(
                    "Error",
                    "Password unable to be saved. Please try again.",
                )

        # Create a button for storing the password
        button = ctk.CTkButton(
            master=frame_left,
            text="Store New Password",
            command=store_password,
        )
        button.pack(
            pady=10,
            padx=10,
        )

        # Create a button for going back to the main UI
        back_button = ctk.CTkButton(
            frame_left,
            text="Go Back",
            command=lambda: app.goto(MainUI.MainUI()),
        )
        back_button.pack(
            pady=10,
            padx=10,
        )

        #### Right side of main (deleting passwords) ####

        # Create a label for deleting passwords
        label = ctk.CTkLabel(
            master=frame_right,
            text="Delete Passwords",
            font=("Helvetica", 28),
        )
        label.pack(
            pady=(15, 3),
            padx=10,
        )

        # Create an entry field for the application name to delete
        app_name_delete = ctk.CTkEntry(
            master=frame_right,
            placeholder_text="Application Name",
        )
        app_name_delete.pack(
            pady=12,
            padx=10,
        )
        ToolTip(app_name_delete, "Enter application name to delete")

        def delete_password():
            """Get the password to delete entered by the user"""
            password_to_delete = app_name_delete.get()

            if not password_to_delete:
                # Show an error message for null input
                tk.messagebox.showerror(
                    "Error",
                    "Please specify application to delete.",
                )
                return

            # Delete the password using the storepassword module
            password_deletion = storepassword.StorePassword().delete_password(
                username,
                password_to_delete,
            )

            if password_deletion:
                # Show a success message if the password is deleted
                tk.messagebox.showinfo(
                    "Password Deleted",
                    "Password has been deleted.",
                )
            else:
                # Show an error message if the password deletion fails
                tk.messagebox.showerror(
                    "Error",
                    "Password deletion failed. Please try again.",
                )
            app_name_delete.delete(
                0,
                "end",
            )

        # Create a button for deleting the password
        button = ctk.CTkButton(
            master=frame_right,
            text="Delete Password",
            command=lambda: (delete_password(), app_name.delete(0, "end")),
        )
        button.pack(
            pady=10,
            padx=10,
        )
