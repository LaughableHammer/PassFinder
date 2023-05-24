from UserInterface import UI, LoginUI2 as LoginUI

def main():
    print("Hello, World!")

    app = UI.PassFinder()

    LoginUI.loginUI(app)

    app.root.mainloop()

