from UserInterface import *  # Importing all modules from UserInterface
from UserInterface import UI, LoginUI

def main():
    app = UI.PassFinder()  # Creating an instance of the PassFinder application
    app.goto(LoginUI.LoginUI())  # Navigating to the LoginUI frame

    app.root.mainloop()  # Starting the main event loop of the application

if __name__ == "__main__":
    main()