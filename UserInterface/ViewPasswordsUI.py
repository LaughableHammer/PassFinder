import customtkinter as ctk
import tkinter as tk

from PassfinderLogic import storepassword

from UserInterface import MainUI

from UserInterface.UI import Frame, PassFinder


class ViewPasswordsUI(Frame):

    def frame(self, app: PassFinder):

        frame = ctk.CTkFrame(master=app.root, corner_radius=15)

        frame.pack(pady=40, padx=50, fill="both", expand=True)


        label = ctk.CTkLabel(master=frame, text="Password Vault", font=("Helvetica", 28))

        label.pack(pady=(15, 3), padx=10)


        with open("TextFiles/username.txt", "r") as file:
            username = str(file.read())


        stored_passwords = storepassword.StorePassword().get_password(username)


        if stored_passwords:

            row = 0

            column = 0

            max_columns = 4

            button_width = 150

            button_height = 30

            button_padding = 10

            for app_name, password in stored_passwords:
                app_password = password

                button = ctk.CTkButton(frame, text=app_name, command=lambda name=app_name, pwd=password: tk.messagebox.showinfo(name, pwd))

                button.place(x=button_padding + column * (button_width + button_padding), y=button_padding + row * (button_height + button_padding))

                button.configure(width=button_width, height=button_height)

                column += 1

                if column == max_columns:

                    row += 1

                    column = 0

        else:

            print("No stored passwords.")


        back_button = ctk.CTkButton(

            frame, text="Go Back", command=lambda: app.goto(MainUI.MainUI())
        )

        back_button.pack(pady=10, padx=10)





# import customtkinter as ctk
# import tkinter as tk



# from PassfinderLogic import storepassword


# from UserInterface import LoginUI, ProfileUI, UI, MainUI


# from UserInterface.UI import Frame, PassFinder




# class ViewPasswordsUI(Frame):


#     def frame(self, app: PassFinder):


#         frame = ctk.CTkFrame(master=app.root, corner_radius=15)


#         frame.pack(pady=40, padx=50, fill="both", expand=True)



#         label = ctk.CTkLabel(


#             master=frame, text="Password Vault", font=("Helvetica", 28)
#         )


#         label.pack(pady=(15, 3), padx=10)



#         with open("TextFiles/username.txt", "r") as file:

#             username = str(file.read())


#         # tk.messagebox.showwarning(

#         #     "Warning", "Please remember, never share your password with anyone."
#         # )
        

#         stored_passwords = storepassword.StorePassword().get_password(username)


#         if stored_passwords:

#             # for app_name, password in stored_passwords:

#             #     print(f"App Name: {app_name}, Password: {password}")

#             for app_name, password in stored_passwords:
#                 app_password = password

#                 button = ctk.CTkButton(frame, text=app_name, command=lambda name=app_name, pwd=password: tk.messagebox.showinfo(name, pwd))

#                 button.pack(padx=10, pady=10)

#         else:

#             print("No stored passwords.")

        

#         back_button = ctk.CTkButton(

#             frame, text="Go Back", command=lambda: app.goto(MainUI.MainUI())
#         )


#         back_button.pack(pady=10, padx=10)

