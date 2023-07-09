import customtkinter as ctk
from UserInterface import (
    LoginUI,
    StorePasswordUI,
    ViewPasswordsUI,
    GeneratePasswordUI,
    PasswordStrengthUI,
)  # Import UI classes
from UserInterface.UI import Frame, PassFinder


class MainUI(Frame):
    """UI for the main page, allows access to all other functions

    Args:
        Frame (class): The app window
    """

    def frame(
        self,
        app: PassFinder,
    ):
        """The "mini" app window that overlays the main window

        Args:
            app (PassFinder): The root app
        """
        frame_main = ctk.CTkFrame(
            master=app.root,
            corner_radius=15,
        )  # Create a frame
        frame_main.pack(
            pady=40,
            padx=50,
            fill="both",
            expand=True,
        )

        frame = ctk.CTkFrame(
            master=frame_main,
        )  # Create a frame
        frame.pack(
            pady=0,
            padx=(0, 0),
            fill="both",
            side="left",
        )

        frame_right = ctk.CTkFrame(
            master=frame_main,
        )  # Create a frame
        frame_right.pack(
            padx=(10, 0),
            fill="both",
            expand=True,
            side="right",
        )

        label = ctk.CTkLabel(
            master=frame,
            text="Dashboard",
            font=("Helvetica", 28),
        )
        label.pack(
            pady=(15, 3),
            padx=10,
        )

        button = ctk.CTkButton(
            master=frame,
            text="Store Passwords",
            command=lambda: app.goto(StorePasswordUI.StorePasswordUI()),
        )
        button.pack(
            pady=12,
            padx=5,
        )

        button = ctk.CTkButton(
            master=frame,
            text="View Passwords",
            command=lambda: app.goto(ViewPasswordsUI.ViewPasswordsUI()),
        )
        button.pack(pady=12, padx=5)

        button = ctk.CTkButton(
            master=frame,
            text="Generate Password",
            command=lambda: app.goto(GeneratePasswordUI.GeneratePasswordUI()),
        )
        button.pack(
            pady=12,
            padx=5,
        )

        button = ctk.CTkButton(
            master=frame,
            text="Strength Test",
            command=lambda: app.goto(PasswordStrengthUI.PasswordStrengthUI()),
        )
        button.pack(
            pady=12,
            padx=5,
        )

        def logout():
            """Logs user out by moving them to the login page"""
            app.account_manager.logout()
            app.goto(LoginUI.LoginUI())

        label = ctk.CTkLabel(  # displays username
            master=frame_right,
            text="Profile - " + app.account_manager.user.username,
            font=("Helvetica", 28),
        )
        label.pack(
            pady=(15, 3),
            padx=10,
        )

        button = ctk.CTkButton(
            master=frame,
            text="Logout",
            command=logout,
        )
        button.pack(
            pady=12,
            padx=5,
        )
