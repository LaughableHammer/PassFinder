import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    'include_files': ["/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/customtkinter"],
    'excludes': [],
    'includes': [],
    'optimize': 0
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this option for a GUI application on Windows

executables = [
    Executable('__main__.py', base=base, target_name='PassFinder', icon='/Users/kesarwani_ku/Documents/GitHub/PassFinder/Icon/PassFinder.ico')
]

setup(
    name='PassFinder',
    version='1.0',
    description='Password manager application',
    options={
        'build_exe': build_exe_options
    },
    executables=executables,
    author="Kushaagra Kesarwani",
)

#pyinstaller --noconfirm --onefile --windowed --icon "/Users/kesarwani_ku/Documents/GitHub/PassFinder/Icon/PassFinder.ico" --name "PassFinder" --add-data "/Users/kesarwani_ku/Documents/GitHub/PassFinder/TextFiles;TextFiles/" --add-data "/opt/homebrew/lib/python3.11/site-packages/customtkinter;customtkinter/" "/Users/kesarwani_ku/Documents/GitHub/PassFinder/__main__.py"