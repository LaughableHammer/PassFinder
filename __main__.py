from UserInterface import *



def main():
    
    app = PassFinder()
    app.goto(LoginUI.LoginUI())

    app.root.mainloop()


if __name__ == "__main__":
    main()