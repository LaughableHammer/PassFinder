from PassfinderLogic import storepassword
import customtkinter as ctk
from UserInterface import LoginUI, ProfileUI, UI, MainUI
from UserInterface.UI import Frame, PassFinder


class StorePasswordUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=50, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Password Vault", font=("Helvetica", 28))
        label.pack(pady=(15, 3), padx=10)

        canvas = ctk.CTkCanvas(master=frame, height=1)
        canvas.pack(fill="x", padx=10, pady=10)
        canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill="black")

        app_name = ctk.CTkEntry(master=frame, placeholder_text="App Name") # username text box
        app_name.pack(pady=12, padx=10)

        app_password = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*") # password textbox
        app_password.pack(pady=12, padx=10)

        def store_password():
            app_name = app_name.get()
            app_password = app_password.get()
            username = LoginUI.LoginUI.username_entry.get()
            save_password = app.storepassword.save_password()

        button = ctk.CTkButton(master=frame, text="Store New Password", command=lambda: app.goto(LoginUI().LoginUI()))
        button.pack(pady=(4), padx=10)

        back_button = ctk.CTkButton(frame, text='Go Back', command=lambda: app.goto(MainUI.MainUI()))
        back_button.pack(pady=4, padx=10)