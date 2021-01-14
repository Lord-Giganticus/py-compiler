# py-compiler
* ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Lord-Giganticus/py-compiler/Python%20application?label=flak8%20check)
* ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Lord-Giganticus/py-compiler/CodeQL?label=CodeQL%20check)
a simple program to easily compile .py files using pyinstaller.
* Usage:
`py -3 py-compiler.py` or run the exe in releases.
* Requirements:
1. Python 3.x (3.9 for the exe)
2. pyinstaller `py -3 -m pip install pyinstaller`
3. Windows 7 or higher (due to use of `os.system('cmd /c')`,`*.write()` and `open()`.)
4. Windows 10 64 bit (for the exe file.)
