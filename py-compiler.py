import os
import time
try:
    from PyInstaller import *
except:
    print('pyinstaller is not installed. Attempting pip install.')
    time.sleep(2)
    os.system('cmd /c py -3 -m pip install pyinstaller')
    try:
        from PyInstaller import *
    except:
        print("Couldn't install pyinstaller! Check your internet connection and then rerun this program!")
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
        if os.path.isfile(file) == True and file.endswith('.py') == True and file != __file__:
            files.append(file)
else:
    os.chdir(folder)
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file) == True and file.endswith('.py') == True and file != __file__:
            files.append(file)
print(str(files[:]))
py_file = str(input('Enter the EXACT name of the py file you want to compile:\n'))
ico = input('Will your program have a icon?\n[1]Yes\n[2]No\n')
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
if ico == 1:
    bat.write(' -i',ico_file)
if name == 1:
    bat.write(' -n',file_name)
bat.write(' '+py_file)
bat.close()
os.system('cmd /c compile.bat')
os.remove('compile.bat')
if name == 1:
    print("Complete. File is in dist/"+file_name+'.exe')
else:
    os.chdir('dist')
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file) == True and file.startswith(os.path.splitext(py_file)) == True:
            new_name = str(os.path.splitext(file))
            print("Complete. File is in dist/"+new_name+'.exe')
time.sleep(10)
exit()