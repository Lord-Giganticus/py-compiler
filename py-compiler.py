import os
import time
import subprocess

def process_exists(process_name): # From https://stackoverflow.com/a/29275361
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())
if process_exists('py-compiler.exe') == False or process_exists('py.exe') == True:
    if os.path.dirname(os.getcwd()) != os.path.dirname(__file__):
        print("py.exe is not running in the script's directory.")
        time.sleep(2)
        print('It is currently running in "'+os.getcwd()+'".')
        time.sleep(2)
        print("Changing directory into the script's direcory.")
        time.sleep(5)
        os.chdir(os.path.dirname(__file__))
if str(os.system('cmd /c pyinstaller -h')).endswith("'pyinstaller' is not recognized as an internal or external command,\noperable program or batch file.") == True:
    if str(os.system('cmd -c py -3 -m pip install pyinstaller')).endswith("'py' is not recognized as an internal or external command,\noperable program or batch file.") == True:
        print('python is not installed! Please go install it!')
        time.sleep(5)
        exit()
basename = os.path.basename(os.getcwd())
folders = [basename]
files = []
ico_files = []
for dir in os.listdir(os.getcwd()):
    if os.path.isdir(dir) == True:
        folders.append(dir)
print(str(folders[:]))
folder = input('Enter the EXACT name of the folder the py file you want to compile is in (note that the first folder is the folder py-compiler is in.):\n')
if folder == basename:
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file) == True and file.endswith('.py') == True:
            files.append(file)
else:
    os.chdir(folder)
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file) == True and file.endswith('.py') == True:
            files.append(file)
print(str(files[:]))
py_file = str(input('Enter the EXACT name of the py file you want to compile:\n'))
ico = int(input('Will your program have a icon?\n[1]Yes\n[2]No\n'))
if ico == 1:
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file) == True and file.endswith('.ico') == True:
            ico_files.append(file)
    print(str(ico_files[:]))
    ico_file = str(input('Enter the EXACT name of the ico file you want:\n'))
    name = int(input('Do you want your file to have a custom name?\n[1]Yes\n[2]No\n'))
    if name == 1:
        file_name = input('Enter the custom name you want(no spaces pls):\n')
        bat = open('compile.bat','w')
        bat.write('pyinstaller -F')
        bat.write(' -i '+ico_file)
        bat.write(' -n '+file_name)
        bat.write(' '+py_file)
        bat.close()
    else:
        bat = open('compile.bat','w')
        bat.write('pyinstaller -F')
        bat.write(' -i '+ico_file)
        bat.write(' '+py_file)
        bat.close()
elif ico == 2:
    name = int(input('Do you want your file to have a custom name?\n[1]Yes\n[2]No\n'))
    if name == 1:
        file_name = input('Enter the custom name you want(no spaces pls):\n')
        bat = open('compile.bat','w')
        bat.write('pyinstaller -F')
        bat.write(' -n',file_name)
        bat.write(' '+py_file)
        bat.close()
    elif name == 2:
        bat = open('compile.bat','w')
        bat.write('pyinstaller -F')
        bat.write(' '+py_file)
        bat.close()
    else:
        print("Improper choice. Crashing the program.")
        time.sleep(2)
        exit()
else:
    print("Improper choice. Crashing the program.")
    time.sleep(2)
    exit()
os.system('cmd /c compile.bat')
os.remove('compile.bat')
print("Complete. File is in the dist folder which is inside the folder you chose.")
time.sleep(10)
exit()