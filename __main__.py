from UserInterface import UI, LoginUI # Import the first page of the application

def main():
    """Runs the application UI and goes to login page"""
    app = UI.PassFinder()  # Creating an instance of the PassFinder application
    app.goto(LoginUI.LoginUI())  # Navigating to the LoginUI frame

    app.root.mainloop()  # Starting the main event loop of the application

if __name__ == "__main__":
    main()
    