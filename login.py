import customtkinter as ctk
import sqlite3
import hashlib

# User interface

ctk.set_appearance_mode("System")                                                 # Dark and light mode based on system settings
ctk.set_default_color_theme("blue")                                               # Colour theme to blue

root = ctk.CTk()
root.geometry("800x500")
root.title("PassFinder")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=40, padx=60, fill="both", expand=True)                            # Padding

label = ctk.CTkLabel(master=frame, text="Login System", font=("Aria ", 24))       # Heading
label.pack(pady=12, padx=10)

UsernameEntry = ctk.CTkEntry(master=frame, placeholder_text="Username")           #Username Entry Field
UsernameEntry.pack(pady=12, padx=10)

PasswordEntry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*") #Password Entry Field
PasswordEntry.pack(pady=12, padx=10)

def Login():                                                                      # Login logic
    Username = UsernameEntry.get()
    Password = PasswordEntry.get()
   #print("Hello, you username is " + Username + " and your password is " + Password + ".")  <- Debug Purposes

     

   # Made with reference to -> https://www.youtube.com/watch?v=3NEzo3CfbPg&t=318s

button = ctk.CTkButton(master=frame, text="Login", command=Login)                 # Login Button
button.pack(pady=12, padx=10)

root.mainloop()