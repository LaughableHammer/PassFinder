from UserInterface import UI, LoginUI2 as LoginUI

def main():
    print("Hello, World!")

    app = UI.PassFinder()

    LoginUI.loginUI(app)

    app.root.mainloop()

if __name__ == '__main__':
    main()