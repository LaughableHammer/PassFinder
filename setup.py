import sys
import os
from cx_Freeze import setup, Executable


#excludefiles = [(os.path.abspath("./TextFiles/userlogindata.db"), "TextFiles/userlogindata.db")]

# Dependencies are automatically detected, but it might need fine tuning.
excludefiles = [os.path.abspath("TextFiles/userlogindata.db")]

build_exe_options = {
    "excludes": ["./TextFiles/userlogindata.db"],
    #"include_files": excludefiles,
    "packages": ['sqlite3'],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="PassFinder",
    version="0.1",
    description="My Password Manager!",
    options={"build_exe": build_exe_options},
    executables=[Executable("__main__.py", base=base)],
)