from UserInterface import UI
from UserInterface import LoginUI


def main():
    print("Hello, World!")

    app = UI.PassFinder()
    app.goto(LoginUI.LoginUI())

    app.root.mainloop()


if __name__ == "__main__":
    main()
