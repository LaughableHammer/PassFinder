from UserInterface import UI
from UserInterface import LoginUI


def main():
    
    app = UI.PassFinder()
    app.goto(LoginUI.LoginUI())

    app.root.mainloop()


if __name__ == "__main__":
    main()