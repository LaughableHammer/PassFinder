import customtkinter as ctk

ctk.set_appearance_mode("System")

root = ctk.CTk()
root.geometry("800x500")
root.title("PassFinder")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=40, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Login System", font=("Arial", 24))
label.pack(pady=12, padx=10)

UsernameEntry = ctk.CTkEntry(master=frame, placeholder_text="Username")
UsernameEntry.pack(pady=12, padx=10)

PasswordEntry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
PasswordEntry.pack(pady=12, padx=10)

def Login():
    Username = UsernameEntry.get()
    Password = PasswordEntry.get()
    print("Hello, you username is " + Username + " and your password is " + Password + ".")

button = ctk.CTkButton(master=frame, text="Login", command=Login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text = "Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()

