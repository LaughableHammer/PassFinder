class StorePasswordUI(Frame):
    def frame(self, app: PassFinder):
        frame = ctk.CTkFrame(master=app.root, corner_radius=15)
        frame.pack(pady=40, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Register", font=("Helvetica", 28))
        label.pack(pady=(15, 3), padx=10)
        
        canvas = ctk.CTkCanvas(master=frame, height=1)
        canvas.pack(fill="x", padx=10, pady=10)
        canvas.create_line(0, 1, int(frame.winfo_width() * 0.5), 1, fill="black")

        username_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
        username_entry.pack(pady=12, padx=10)

        password_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
        password_entry.pack(pady=12, padx=10)
        
        confirm_password = ctk.CTkEntry(master=frame, placeholder_text="Confirm password", show="*")
        confirm_password.pack(pady=12, padx=10)

        def create_account():
            username = username_entry.get()
            password = password_entry.get()
            confirm = confirm_password.get()

            if password != confirm:
                tk.messagebox.showerror("Input Error", "Passwords do not match. Please try again.")
            else:
                is_created = app.account_manager.create_account(username, password)
                if is_created:
                    app.account_manager.login(username, password)
                    app.goto(MainUI.MainUI())
                else:
                    tk.messagebox.showerror("Input Error", "Account already exists or password doesn't meet requirements.")  # intentionally vague for security purposes
#######need to implement the password requirements feature later########
            
            
        button = ctk.CTkButton(master=frame, text="Create Account", command=create_account)
        button.pack(pady=(12, 4), padx=10)
        
        create_account_label = ctk.CTkLabel(master=frame, text="OR")
        create_account_label.pack(pady=0.8)
        
        back_button = ctk.CTkButton(frame, text='Go Back', command=lambda: app.goto(LoginUI.LoginUI()))
        back_button.pack(pady=4, padx=10)