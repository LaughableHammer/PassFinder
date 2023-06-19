'''
    NOTE: 
    You have not commented any of this code. 
    Likewise you are using * as an import method, but are not 
    using all of its sub-modules. You should only import the 
    parts of a module you use. This will prevent bugs and over
    committing your memory. 
    
    Please make sure you are creating standard docstring for all
    your code. 
'''
from UserInterface import *
from UserInterface import UI, LoginUI


def main():
    
    app = UI.PassFinder()
    app.goto(LoginUI.LoginUI())

    app.root.mainloop()


if __name__ == "__main__":
    main()